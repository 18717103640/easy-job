from spider.spider_qiancheng.web.python.domain.repository.condition_repository import ConditionRepository
from spider.spider_qiancheng.web.python.domain.model.condition import Condition
import json

from spider.spider_qiancheng.web.python.port.adapter.service.result_data.job_list.job_list_service import find_total_count


def insert_condition(result, condition):
    res_count = 0
    # result_dict = json.loads(result)
    total_count = find_total_count(result)

    # 先查再插入,有就更新，没有就新增
    results = ConditionRepository.find_one(condition)
    if results is None or len(results) == 0:
        condition_entity = Condition(condition, res_count, total_count)
        ConditionRepository.insert(condition_entity)
        print('当前condition:     ' + condition + '        ,insert success')
    else:
        condition_entity = Condition(condition, res_count, total_count, id=results[0])
        ConditionRepository.update_condition(condition_entity)
        print('当前condition:     ' + condition + '        ,update success！！！')


def find_condition_by_total_count(condition_list):
    condition_entity_list = []
    for condition in condition_list:
        result = ConditionRepository.find_one_by_condition(condition)
        # 一些自定义条件可能数据库没有数据，会返回None
        if result is not None:
            total_count: int = result[3]
            if total_count > 15:
                condition = result[1]
                res_count = result[2]
                id = result[0]
                created_time = result[4]
                updated_time = result[5]

                new_condition_entity = Condition(
                    condition, res_count, total_count, id, created_time, updated_time)
                condition_entity_list.append(new_condition_entity)
    return condition_entity_list


def find_condition_count_by_today():
    results = ConditionRepository.find_condition_count_by_today()
    return results
