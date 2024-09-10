from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class CompanyThirdPartyRepository:

    @staticmethod
    def find_by_brand_name(brand_name):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `company_third_party` WHERE brand_name like '%{}%' ;".format(brand_name))
        return db_conn.get_all(sql_str=sql_str)

    @staticmethod
    def insert(brand_name, third_party_type):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `company_third_party` ("
            "`brand_name`, `third_party_type`"
            ") VALUES ("
            "'{}',{}"
            ");"
            .format(brand_name, third_party_type))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def find_all():
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `company_third_party` ;")
        return db_conn.get_all(sql_str=sql_str)
