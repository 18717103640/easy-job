from spider.spider_qiancheng.web.python.port.adapter.enviroment.database_config import DatabaseConfig


class JobSourceRepository:

    @staticmethod
    def find_by_job_name_and_company_name(job_name, company_name):
        db_conn = DatabaseConfig.get_db_conn()
        sql_str = ("SELECT * FROM `qiancheng_job_source` WHERE `jobName`= '{}' and `fullCompanyName`='{}';"
                   .format(job_name, company_name))
        results = db_conn.get_one(sql_str=sql_str)
        return results

    @staticmethod
    def insert(JobSource):
        db_conn = DatabaseConfig.get_db_conn()

        sql_str = (
            "INSERT INTO `qiancheng_job_source` ("
            "`jobName` ,`fullCompanyName` ,`jobId` ,`jobTags` ,`jobAreaString` ,"
            "`provideSalaryString` ,`workYearString` ,`degreeString`,`companyIndustryType1Str` ,`companyIndustryType2Str` ,"
            "`lon` ,`lat` ,`jobHref` ,`jobDescribe` ,`companyHref`,"
            "`termStr` ,`jobWelfareCodeDataList` ,`jobSalaryMax` ,`jobSalaryMin` ,`source`"
            ") VALUES ("
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}'"
            ");"
            .format(
                JobSource.jobName, JobSource.fullCompanyName, JobSource.jobId,
                JobSource.jobTags, JobSource.jobAreaString,
                JobSource.provideSalaryString, JobSource.workYearString,
                JobSource.degreeString, JobSource.companyIndustryType1Str,
                JobSource.companyIndustryType2Str,
                JobSource.lon, JobSource.lat, JobSource.jobHref,
                JobSource.jobDescribe, JobSource.companyHref,
                JobSource.termStr, JobSource.jobWelfareCodeDataList, JobSource.jobSalaryMax,
                JobSource.jobSalaryMin, JobSource.source

            ))
        results = db_conn.insert(sql_str=sql_str)
        return results

    @staticmethod
    def update(JobSource, job_name, company_name):
        db_conn = DatabaseConfig.get_db_conn()
        sql_template = """
                UPDATE `qiancheng_job_source`
                SET
                    `jobId` = '{jobId}',
                    `jobTags` = '{jobTags}',
                    `jobAreaString` = '{jobAreaString}',
                    
                    `provideSalaryString` = '{provideSalaryString}',
                    `workYearString` = '{workYearString}',
                    `degreeString` = '{degreeString}',
                    `companyIndustryType1Str` = '{companyIndustryType1Str}',
                    `companyIndustryType2Str` = '{companyIndustryType2Str}',
                    
                    `lon` = '{lon}',
                    `lat` = '{lat}',
                    `jobHref` = '{jobHref}',
                    `jobDescribe` = '{jobDescribe}',
                    `companyHref` = '{companyHref}',
                    
                    `termStr` = '{termStr}',
                    `jobWelfareCodeDataList` = '{jobWelfareCodeDataList}',
                    `jobSalaryMax` = '{jobSalaryMax}',
                    `jobSalaryMin` = '{jobSalaryMin}',
                    `source` = '{source}'
                WHERE
                    `jobName` = '{jobName}' AND
                    `fullCompanyName` = '{fullCompanyName}';
                """
        # 打印SQL语句以检查
        sql_statement = sql_template.format(
            jobId=JobSource.jobId,
            jobTags=JobSource.jobTags, jobAreaString=JobSource.jobAreaString,
            provideSalaryString=JobSource.provideSalaryString, workYearString=JobSource.workYearString,
            degreeString=JobSource.degreeString, companyIndustryType1Str=JobSource.companyIndustryType1Str,
            companyIndustryType2Str=JobSource.companyIndustryType2Str,
            lon=JobSource.lon, lat=JobSource.lat, jobHref=JobSource.jobHref,
            jobDescribe=JobSource.jobDescribe, companyHref=JobSource.companyHref,
            termStr=JobSource.termStr, jobWelfareCodeDataList=JobSource.jobWelfareCodeDataList,
            jobSalaryMax=JobSource.jobSalaryMax,
            jobSalaryMin=JobSource.jobSalaryMin, source=JobSource.source, jobName=job_name,
            fullCompanyName=company_name
        )
        results = db_conn.modify(sql_statement)
        return results
