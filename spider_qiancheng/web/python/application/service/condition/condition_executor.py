from spider.spider_qiancheng.web.python.application.service.condition.condition_handler import ConditionHandler
from spider.spider_qiancheng.web.python.application.service.condition.condition_service import insert_condition
from spider.spider_qiancheng.web.python.application.service.condition_fail.condition_fail_service import \
    update_fail_condition_retry_times, have_fail_condition, insert_fail_condition
from spider.spider_qiancheng.web.python.application.service.request_log.request_log_service import insert_request_log
from spider.spider_qiancheng.web.python.domain.repository.condition_fail_repository import FailConditionRepository
from spider.spider_qiancheng.web.python.domain.repository.condition_repository import ConditionRepository
# 由于模块跨度较大，无法使用相对引入，此处使用绝对导入
from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.service.drissionpage.drissionpage_handler import \
    DrissionPageHandler
from spider.spider_qiancheng.web.python.port.adapter.service.result_data.job_list.job_list_service import \
    handle_success_joblist_results
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_common_config, \
    get_platform_config


def generate_condition_count(condition_list):
    # 生成condition list
    logger.info('生成condition list: {}'.format(condition_list))

    # 获取平台最大请求数
    day_limit = int(get_platform_config('platform', 'day_limit'))
    logger.info('最大请求数-DAY_LIMIT: {}'.format(str(day_limit)))

    for index in range(0, len(condition_list)):
        # 反爬绕过
        if is_max_limit(day_limit):
            break

        # 打印condition日志
        condition = condition_list[index]
        print('current condition========================================>' + condition_list[index])
        print('current condition process========================================>' +
              str(index) + '/' + str(len(condition_list)))

        # condition去重
        condition_result = ConditionRepository.find_one(condition_list[index])
        if condition_result is None or len(condition_result) == 0:
            # 请求平台，获取数据
            result = DrissionPageHandler().request_platform(condition)
            job_result = result['job_data']
            # 记录请求
            insert_request_log(result=result['job_data'], condition=condition, url=result['url'])
            # 如果返回 None
            if job_result is None:
                logger.info('请求平台异常或没有数据！！！')
                insert_fail_condition(condition)
            else:
                logger.info('请求平台成功！！！')
                # 插入condition count
                insert_condition(job_result, condition)
                handle_success_joblist_results(result=result['job_data'])
    return condition_list


def execute_fail_condition():
    while True:
        results = FailConditionRepository.find_all_fail_condition()
        for condition_fail_record in results:
            condition = condition_fail_record[1]
            # 请求平台，获取数据
            result = DrissionPageHandler().request_platform(condition)
            job_result = result['job_data']
            # 记录请求
            insert_request_log(result=result['job_data'], condition=condition, url=result['url'])
            # 如果返回 None
            if job_result is None:
                logger.info('请求平台异常或没有数据！！！')
                insert_fail_condition(condition)
                #  retry_times+1
                update_fail_condition_retry_times(condition_fail_record)
            else:
                logger.info('请求平台成功！！！')
                # 插入condition count
                insert_condition(job_result, condition)
                handle_success_joblist_results(result=result['job_data'])
                # 删除这条条件失败记录
                FailConditionRepository.delete_by_condition(condition_fail_record[1])

        # 如果失败条件重试五次仍然失败就放弃
        if not have_fail_condition():
            break


def is_max_limit(day_limit):
    today_conditions = ConditionRepository.find_today_end_condition()
    if len(today_conditions or []) == day_limit:
        logger.info('今日已达最大请求数！！！，请切换账号和ip后，重启服务。')
        return True
    return False


if __name__ == '__main__':
    pass
