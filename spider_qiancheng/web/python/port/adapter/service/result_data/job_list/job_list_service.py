from spider.spider_qiancheng.web.python.application.service.qiancheng_job.qiancheng_job_service import \
    insert_qiancheng_job
from spider.spider_qiancheng.web.python.application.service.qiancheng_job_source.qiancheng_job_source_service import \
    insert_job_source
from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger


def find_total_count(result_dict):
    return result_dict['resultbody']['job']['totalcount']


def find_job_list(result_dict):
    return result_dict['resultbody']['job']['items']


def handle_success_joblist_results(result):
    print(type(result))
    # success
    # result_dict = json.loads(result)
    job_list = find_job_list(result)
    total_count = find_total_count(result)
    logger.info('当前condition totalCount: {}'.format(total_count))
    if total_count != 0 and job_list is not None:
        print(job_list)
        for job in job_list:
            # 插入平台job_source
            insert_job_source(job)
            logger.info('插入 job source success！！！')
            # 插入平台job,可独立用于可视化，全量同步job
            insert_qiancheng_job(job)
            logger.info('插入 job success！！！')



if __name__ == '__main__':
    pass
