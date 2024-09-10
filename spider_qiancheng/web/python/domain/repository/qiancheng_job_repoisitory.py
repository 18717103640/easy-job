from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class QianchengJobRepository:

    @staticmethod
    def find_job_by_brand_name_and_job_name(brand_name, job_name):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM qiancheng_job WHERE brand_name= '{}' and job_name= '{}';".format(brand_name, job_name))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def update(job, id):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE qiancheng_job "
            "SET salary_desc_min= '{}' ,salary_desc_max= '{}' ,salary_desc= '{}' ,"
            "city_name= '{}' ,area_district= '{}' ,business_district= '{}',location= '{}' ,"
            "brand_scale_name= '{}' ,brand_scale_min= '{}' ,brand_scale_max= '{}',"
            "brand_industry= '{}' ,job_degree= '{}' ,job_experience= '{}',brand_stage_name= '{}' ,"
            "exist_day= '{}' ,third_party_flag= '{}' ,source= '{}',welfareList= '{}' "
            "where id = '{}'"
            .format(job.salary_desc_min, job.salary_desc_max, job.salary_desc,
                    job.city_name, job.area_district, job.business_district, job.location,
                    job.brand_scale_name, job.brand_scale_min, job.brand_scale_max,
                    job.brand_industry, job.job_degree, job.job_experience, job.brand_stage_name,
                    job.exist_day, job.third_party_flag, job.source, job.welfareList,
                    id
                    ))
        results = db_conn.modify(sql_str=sql_str)
        return results

    @staticmethod
    def insert(job):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "INSERT INTO `qiancheng_job` ("
            "`brand_name` ,`job_name` ,`salary_desc_min` ,`salary_desc_max` ,`salary_desc` ,"
            "`city_name` ,`area_district` ,`business_district`,`location` ,`brand_scale_name` ,"
            "`brand_scale_min` ,`brand_scale_max` ,`brand_industry` ,`job_degree` ,`job_experience`,"
            "`brand_stage_name` ,`exist_day` ,`third_party_flag` ,`source` ,`welfareList`"
            ") VALUES ("
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}'"
            ");"
            .format(job.brand_name, job.job_name, job.salary_desc_min, job.salary_desc_max, job.salary_desc,
                    job.city_name, job.area_district, job.business_district, job.location, job.brand_scale_name,
                    job.brand_scale_min, job.brand_scale_max, job.brand_industry, job.job_degree, job.job_experience,
                    job.brand_stage_name, job.exist_day, job.third_party_flag, job.source, job.welfareList
                    ))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def find_list(brand_name):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_job` WHERE `brand_name` like '%{}%';"
                   .format(brand_name))
        results = db_conn.get_all(sql_str=sql_str)
        return results

    @staticmethod
    def update_third_party_by_id(id):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = (
            "UPDATE `qiancheng_job`  SET `third_party_flag` = 1 WHERE `id` = '{}';"
            .format(id))
        results = db_conn.insert(sql_str=sql_str)
        return results
