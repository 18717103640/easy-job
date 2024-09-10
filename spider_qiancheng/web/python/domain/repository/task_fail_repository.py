from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class FailTaskRepository:

    @staticmethod
    def insert(boss_task_fail_entity):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `qiancheng_task_fail` (`task_id`, `condition`, `current_page`, `retry_time`) VALUES ('{}','{}','{}','{}');"
            .format(
                boss_task_fail_entity.task_id,
                boss_task_fail_entity.condition,
                boss_task_fail_entity.current_page,
                boss_task_fail_entity.retry_time))
        results = db_conn.insert(sql_str=sql_str)
        if results == 1:
            print("insert task_fail success" + ",task_fail_entity:    " + str(
                boss_task_fail_entity.print_self()))
        return results

    @staticmethod
    def find_by_task_id_and_condition_current_page(task_id, condition, current_page):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "SELECT * FROM `qiancheng_task_fail` WHERE `task_id`= '{}' AND `condition` = '{}' AND `current_page` = '{}';"
            .format(task_id, condition, current_page))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def find_all_fail_condition(task_id):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_task_fail` WHERE `task_id`= '{}' AND `retry_time` <=5;"
                   .format(task_id))
        results = db_conn.get_all(sql_str=sql_str)
        return results

    @staticmethod
    def delete_by_task_id_and_condition(task_id, condition, current_page):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "DELETE FROM `qiancheng_task_fail`   WHERE `task_id`= '{}' and `condition`= '{}' and `current_page`= '{}';"
            .format(task_id, condition, current_page))
        results = db_conn.insert(sql_str=sql_str)

        return results

    @staticmethod
    def update_retry_time(retry_time, task_id, condition, current_page):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_task_fail`  SET `retry_time` = {} WHERE `task_id`= '{}' and `condition`= '{}' and `current_page`= '{}';"
            .format(retry_time, task_id, condition, current_page))
        results = db_conn.insert(sql_str=sql_str)
        return results
