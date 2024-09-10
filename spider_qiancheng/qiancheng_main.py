from spider.spider_qiancheng.web.python.application.service.condition.condition_constants import ConditionConstants
from spider.spider_qiancheng.web.python.application.service.condition.condition_executor import \
    generate_condition_count, \
    execute_fail_condition
from spider.spider_qiancheng.web.python.application.service.condition.condition_handler import ConditionHandler
from spider.spider_qiancheng.web.python.application.service.task.task_executor import generate_task, execute_task
from spider.spider_qiancheng.web.python.application.service.task_fail.task_fail_service import execute_task_fail
from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.service.init_service import init_queue
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_common_config


def qiancheng_application():
    # 初始化init动作
    init_queue()

    # 初始化condition list
    condition_list = ConditionHandler.generate_condition_customize(parameters=ConditionConstants.PARAMETER_INTERVIEW,
                                                                   parameter_num=1)

    # 第1步  生成condition count
    logger.info("生成condition count 开始")
    generate_condition_count(condition_list=condition_list)
    logger.info("生成condition count 结束")

    # 第2步  执行 失败condition
    logger.info("执行失败condition 开始")
    execute_fail_condition()
    logger.info("执行失败condition 结束")

    # 第3步  生成task
    logger.info("生成task 开始")
    task_id = get_common_config('task', 'id')

    generate_task(condition_list, task_id)
    logger.info("生成task 结束")

    # 第4步  执行task
    logger.info("执行task 开始")
    task_id = get_common_config('task', 'id')
    execute_task(task_id)
    logger.info("执行task 结束")

    # 第5步  执行失败task
    logger.info("执行失败task 开始")
    execute_task_fail(task_id)
    logger.info("执行失败task 结束")


if __name__ == '__main__':
    qiancheng_application()
