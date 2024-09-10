from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_common_config
from spider.spider_qiancheng.web.python.port.adapter.utils.dbutils import DBUtils


class DatabaseConfig:

    @staticmethod
    def get_db_conn():
        host = get_common_config('database', 'host')
        user = get_common_config('database', 'user')
        password = str(get_common_config('database', 'password'))
        db_name = get_common_config('database', 'db_name')
        return DBUtils(host=host, user=user,
                       password=password, db=db_name)
