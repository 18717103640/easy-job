from spider.spider_qiancheng.web.python.domain.repository.task_fail_repository import FailTaskRepository
from spider.spider_qiancheng.web.python.port.adapter.service.drissionpage.drissionpage_handler import DrissionPageHandler
from spider.spider_qiancheng.web.python.port.adapter.service.result_data.job_list.job_list_service import \
    handle_success_joblist_results


def insert_fail_task(task_fail):
    result = FailTaskRepository().find_by_task_id_and_condition_current_page(
        task_id=task_fail.task_id, condition=task_fail.condition, current_page=task_fail.current_page)
    if result is None:
        FailTaskRepository().insert(task_fail)


def execute_task_fail(task_id):
    while True:
        # 查询所有任务
        results = FailTaskRepository().find_all_fail_condition(task_id)
        for task_fail_record in results:
            result = DrissionPageHandler().request_platform(condition=task_fail_record[2], page_num=task_fail_record[3])
            # 如果请求失败
            if result['job_data'] is None:
                print('当前返回结果JsonData为None')
                #  retry_time+1
                FailTaskRepository().update_retry_time(
                    retry_time=task_fail_record[4] + 1, task_id=task_fail_record[1], condition=task_fail_record[2],
                    current_page=task_fail_record[3]
                )

            # 如果请求成功
            else:
                handle_success_joblist_results(result=result['job_data'])
                # 删除这条条件失败记录
                FailTaskRepository().delete_by_task_id_and_condition(
                    task_id, condition=task_fail_record[2], current_page=task_fail_record[3]
                )

        # 如果失败条件重试五次仍然失败就放弃
        if not have_fail_task(task_id):
            break


def have_fail_task(task_id):
    results = FailTaskRepository().find_all_fail_condition(task_id)
    if results is None or len(results) == 0:
        return False
    return True
