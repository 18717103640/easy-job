import json

from spider.spider_qiancheng.web.python.application.service.condition import condition_service
from spider.spider_qiancheng.web.python.application.service.request_log.request_log_service import insert_request_log
from spider.spider_qiancheng.web.python.application.service.task.task_service import insert_task, should_stop, \
    update_status, find_by_task_id_and_status
from spider.spider_qiancheng.web.python.application.service.task_fail.task_fail_service import insert_fail_task
from spider.spider_qiancheng.web.python.domain.model.task_fail import TaskFail
from spider.spider_qiancheng.web.python.domain.repository.task_repository import TaskRepository
from spider.spider_qiancheng.web.python.port.adapter.service.drissionpage.drissionpage_handler import DrissionPageHandler
from spider.spider_qiancheng.web.python.port.adapter.service.result_data.job_list.job_list_service import \
    handle_success_joblist_results, find_job_list


def generate_task(condition_list, task_id):
    # 过滤total_count =0的条件，并按照total_count降序排序
    condition_entity_list = condition_service.find_condition_by_total_count(condition_list)
    condition_entity_list_sorted = sorted(condition_entity_list, key=lambda x: x.total_count, reverse=True)

    # 生成新的任务队列
    for condition_entity in condition_entity_list_sorted:
        insert_task(task_id, condition_entity, condition_entity_list_sorted)


def handle_page_request(results):
    for task in results:
        # 每次执行task，检测是否触发反爬限制请求数
        if should_stop(id=task[0]):
            exit()
        else:
            # 更新task状态
            update_status(task)
            current_page, page = task[4], task[5]
            # 循环执行任务分页
            for page_num in range(current_page, page + 1):
                # 请求平台，获取数据result
                result = DrissionPageHandler().request_platform(condition=task[2], page_num=page_num)
                # 插入请求日志
                insert_request_log(result=result['job_data'], condition=task[2], url=result['url'])
                # 请求失败  todo 目前拉勾失败的情况不知道，需要针对性写代码
                if result['job_data'] is None:
                    print('当前返回结果JsonData为None')
                    print(result)
                    task_fail_entity = TaskFail(task_id=task[1], condition=task[2], current_page=page_num, retry_time=0)
                    # 记录失败task
                    insert_fail_task(task_fail_entity)

                # 请求成功
                else:
                    # 处理请求成功
                    handle_success_joblist_results(result=result['job_data'])
                    # 存在condition很多分页，task对应分页没数据的情况  由于前面的程序统一处理了没数据的情况，基本上走不到这里。
                    # result_dict = json.loads(result['job_data'])
                    result_dict = result['job_data']
                    job_list = find_job_list(result_dict)
                    if job_list is None or len(job_list) == 0:
                        break

                # 执行完一页就更新当前页
                if page_num != page:
                    TaskRepository().update_current_page(page_num + 1, task_id=task[1], condition=task[2])
        # 当这个条件执行完毕，需要设置task status为2（已完成）
        TaskRepository().update_status(2, task_id=task[1], condition=task[2])


def execute_task(task_id):
    # 不存在一个正在执行的task，从零开始
    result = find_by_task_id_and_status(task_id, status=1)
    # 首次执行
    if len(result) == 0:
        results = TaskRepository().find_by_task_id(task_id)
        handle_page_request(results)

    # 存在一个正在执行的task
    if len(result) == 1:
        results = TaskRepository().find_by_task_id(task_id)
        condition_list = []
        for result_one in results:
            condition_list.append(result_one[2])

        new_results = results[condition_list.index(result[0][2]):len(results)]
        handle_page_request(new_results)
    # 存在一个正在执行的task，说明程序有bug，需要紧急修复
    if len(result) > 2:
        print('当前程序存在bug，请修复')
        exit()


if __name__ == '__main__':
    pass
