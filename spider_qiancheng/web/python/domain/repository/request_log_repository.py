from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class RequestLogRepository:

    @staticmethod
    def insert(request_log):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `request_log` (`platform`, `task_id`, `user_id`, `condition`, `url`, `ip`, `source_data`) "
            "VALUES ('{}','{}','{}','{}','{}','{}','{}');"
            .format(request_log.platform, request_log.task_id, request_log.user_id, request_log.condition,
                    request_log.url, request_log.ip, request_log.source_data))
        results = db_conn.insert(sql_str=sql_str)
        return results
