from spider.spider_qiancheng.web.python.domain.model.condition_fail import ConditionFail
from spider.spider_qiancheng.web.python.domain.repository.condition_fail_repository import FailConditionRepository


def insert_fail_condition(condition):
    fail_condition = ConditionFail(condition, 0)
    FailConditionRepository.insert(fail_condition)


def update_fail_condition_retry_times(condition_fail_record):
    print('当前condition================>' + condition_fail_record[1])
    print('当前retry_times================>' + str(condition_fail_record[2]))
    new_condition_fail_record_entity = ConditionFail(condition=condition_fail_record[1],
                                                     retry_times=condition_fail_record[2] + 1)
    FailConditionRepository.update_retry_times(new_condition_fail_record_entity)


def have_fail_condition():
    results = FailConditionRepository.find_all_fail_condition()
    if results is None or len(results) == 0:
        return False
    return True


def fail_condition_to_mysql(condition):
    print('******当前请求失败条件入库******')
    print('当前condition================>' + condition)
    new_condition_fail_record_entity = ConditionFail(condition, 0)
    results = FailConditionRepository.find_one(new_condition_fail_record_entity)
    if results is None or len(results) == 0:
        FailConditionRepository.insert(new_condition_fail_record_entity)
