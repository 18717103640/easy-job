from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class ConditionRepository:
    @staticmethod
    def find_today_end_condition():
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition` WHERE to_days(`created_time`) = to_days(now());")
        results = db_conn.get_all(sql_str=sql_str)
        return results

    @staticmethod
    def find_one(condition_str):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition` WHERE `condition`= '{}';"
                   .format(condition_str))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def insert(condition_entity):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `qiancheng_condition` (`condition`, `res_count`, `total_count`) VALUES ('{}',{},{});"
            .format(condition_entity.condition, condition_entity.res_count, condition_entity.total_count))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def update_condition(condition_entity):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_condition`  SET `condition` = '{}', `res_count` = '{}', `total_count` = '{}' WHERE `id` = '{}';"
            .format(condition_entity.condition, condition_entity.res_count, condition_entity.total_count,
                    condition_entity.id))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def find_one_by_condition(condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition` WHERE `condition`= '{}';"
                   .format(condition))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def find_condition_count_by_today():
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition` WHERE to_days(`created_time`) = to_days(now());")
        results = db_conn.get_all(sql_str=sql_str)
        return results


if __name__ == '__main__':
    pass
