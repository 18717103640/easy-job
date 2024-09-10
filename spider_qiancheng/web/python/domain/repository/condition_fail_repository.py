from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class FailConditionRepository:

    @staticmethod
    def insert(fail_condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `qiancheng_condition_fail` (`condition`, `retry_times`) VALUES ('{}',{});"
            .format(fail_condition.condition, fail_condition.retry_times))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def find_one(fail_condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition_fail` WHERE `condition`= '{}';"
                   .format(fail_condition.condition))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def find_all():
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition_fail` ;")
        results = db_conn.get_all(sql_str=sql_str)
        print(type(results))  # 此处应该是元组
        return results

    @staticmethod
    def update_retry_times(fail_condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_condition_fail`  SET `retry_times` = {} WHERE `condition`= '{}';"
            .format(fail_condition.retry_times, fail_condition.condition))
        results = db_conn.insert(sql_str=sql_str)
        # if results is None or results != 1:
        #     print("updata condition_fail_record_entity fail" + ",condition_fail_record_entity:    " + str(
        #         condition_fail_record_entity.print_self()))
        #     exit()
        return results

    @staticmethod
    def delete_by_condition(condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "DELETE FROM `qiancheng_condition_fail`   WHERE `condition`= '{}';"
            .format(condition))
        results = db_conn.insert(sql_str=sql_str)
        # if results is None or results != 1:
        #     print("DELETE condition_fail_record_entity fail" + ",condition_fail_record_entity:    " + condition)
        #     exit()
        return results

    @staticmethod
    def find_all_fail_condition():
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_condition_fail` WHERE `retry_times` <=5;")
        results = db_conn.get_all(sql_str=sql_str)
        return results
