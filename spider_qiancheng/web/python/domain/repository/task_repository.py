from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class TaskRepository:

    @staticmethod
    def insert(boss_task_entity):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `qiancheng_task` (`task_id`, `condition`, `status`,`current_page`, `page`, `order`) VALUES ('{}','{}','{}','{}','{}','{}');"
            .format(
                boss_task_entity.task_id,
                boss_task_entity.condition,
                boss_task_entity.status,
                boss_task_entity.current_page,
                boss_task_entity.page,

                boss_task_entity.order))
        results = db_conn.insert(sql_str=sql_str)
        if results == 1:
            print("insert task success" + ",task_entity:    " + str(boss_task_entity.print_self()))
        return results

    @staticmethod
    def find_one(task_id, condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_task` WHERE `task_id`= '{}' and `condition`= '{}';"
                   .format(task_id, condition))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def find_by_task_id_and_status(task_id, status):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_task` WHERE `task_id`= '{}' and `status`= '{}';"
                   .format(task_id, status))
        results = db_conn.get_all(sql_str=sql_str)
        return results

    @staticmethod
    def find_by_task_id(task_id):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_task` WHERE `task_id`= '{}' AND `status`<2 ORDER BY `order` ASC;"
                   .format(task_id))
        results = db_conn.get_all(sql_str=sql_str)
        return results

    @staticmethod
    def update_current_page(current_page, task_id, condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_task`  SET `current_page` = '{}' WHERE `task_id` = '{}' AND `condition` = '{}';"
            .format(current_page, task_id, condition))
        results = db_conn.insert(sql_str=sql_str)
        if results == 1:
            print("updata task current_page SUCCESS")
        return results

    @staticmethod
    def update_status(status, task_id, condition):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_task`  SET `status` = '{}' WHERE `task_id` = '{}' AND `condition` = '{}';"
            .format(status, task_id, condition))
        results = db_conn.insert(sql_str=sql_str)
        if results == 1:
            print("updata task status SUCCESS")
        return results
