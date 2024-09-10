from spider.spider_qiancheng.web.python.application.service.condition.condition_handler import ConditionHandler
from spider.spider_qiancheng.web.python.domain.model.condition import Condition
from spider.spider_qiancheng.web.python.domain.model.task import Task
from spider.spider_qiancheng.web.python.domain.repository.task_repository import TaskRepository
from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.utils.page_utils import PageUtils
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_platform_config, get_common_config


def generate_task_condition_list(my_parameter, parameter_num):
    return ConditionHandler.generate_condition_customize(my_parameter, parameter_num)


def insert_task(task_id, condition_entity, condition_entity_list):
    # 先查询是否存在相同任务，再插入
    result = TaskRepository().find_one(task_id, condition_entity.condition)
    page_num = PageUtils.get_page_num(condition_entity.total_count, 20)
    total_page = page_num if page_num <= 50 else 50

    if result is None or len(result) == 0:
        new_task_entity = Task(
            task_id=task_id, condition=condition_entity.condition, status=0, current_page=2, page=total_page,
            order=condition_entity_list.index(condition_entity))
        TaskRepository().insert(new_task_entity)


def should_stop(id):
    task_id = get_common_config('task', 'id')
    day_limit = get_platform_config('platform', 'day_limit')
    stop_id = generate_task_stop_id(task_id, day_limit)
    if id == stop_id:
        return True
    return False


def find_by_task_id_and_status(task_id, status):
    return TaskRepository().find_by_task_id_and_status(task_id, status)


def update_status(task):
    TaskRepository().update_status(1, task_id=task[1], condition=task[2])


def should_stop_by_request_log():
    # todo
    pass


def find_stop_id_by_tasks(results, day_limit):
    count = 0
    for task in results:
        for page_num in range(task[4], task[5] + 1):
            count += 1
            if count == day_limit:
                return str(task[0])


def generate_task_stop_id(task_id, day_limit):
    task_result = TaskRepository().find_by_task_id_and_status(task_id, status=1)
    task_list = TaskRepository().find_by_task_id(task_id)

    if len(task_result) == 0:
        return find_stop_id_by_tasks(task_list, day_limit)
    elif len(task_result) == 1:
        condition_list = []
        for task in task_list:
            condition_list.append(task[2])
        new_results = task_list[condition_list.index(task_result[0][2]):len(task_list)]
        return find_stop_id_by_tasks(new_results, day_limit)
    else:
        logger.error('当前程序存在bug，请修复')
        exit()


if __name__ == '__main__':
    pass
