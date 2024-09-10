import json

from spider.spider_qiancheng.web.python.domain.model.qiancheng_job_source import QianChengJobSource
from spider.spider_qiancheng.web.python.domain.repository.qiancheng_job_source_repository import JobSourceRepository
from spider.spider_qiancheng.web.python.port.adapter.utils.list_utils import ListUtils


def insert_job_source(job):
    job_name = job['jobName'] if 'jobName' in job else None,
    company_name = job['fullCompanyName'] if 'fullCompanyName' in job else None,
    # 去重，存在就更新，不存在就插入
    job_source_result = JobSourceRepository.find_by_job_name_and_company_name(job_name, company_name),

    # 构建对象
    job_source = QianChengJobSource()   ## 这里添加','号，job_source类型会从class变成元组tuple

    job_source.jobName = job['jobName'] if 'jobName' in job else None,
    job_source.fullCompanyName = job['fullCompanyName'] if 'fullCompanyName' in job else None,
    job_source.jobId = job['jobId'] if 'jobId' in job else None,
    job_source.jobTags = ListUtils.list_to_string(job['jobTags']) if 'jobTags' in job else None,
    job_source.jobAreaString = job['jobAreaString'] if 'jobAreaString' in job else None,

    job_source.provideSalaryString = job['provideSalaryString'] if 'provideSalaryString' in job else None,
    job_source.workYearString = job['workYear'] if 'workYear' in job else None,
    job_source.degreeString = job['degreeString'] if 'degreeString' in job else None,
    job_source.companyIndustryType1Str = job['companyIndustryType1Str'] if 'companyIndustryType1Str' in job else None,
    job_source.companyIndustryType2Str = None  # 实际请求没有这个参数，或者有时候是没有的

    job_source.lon = job['lon'] if 'lon' in job else None,
    job_source.lat = job['lat'] if 'lat' in job else None,
    job_source.jobHref = job['jobHref'] if 'jobHref' in job else None,
    job_source.jobDescribe = job['jobDescribe'].replace('\n', ', ').strip() if 'jobDescribe' in job else None,
    job_source.companyHref = job['companyHref'] if 'companyHref' in job else None,

    job_source.termStr = job['termStr'] if 'termStr' in job else None,
    job_source.jobWelfareCodeDataList = (ListUtils.list_dict_to_string(job['jobWelfareCodeDataList'], 'chineseTitle')
                                         if 'jobWelfareCodeDataList' in job and 'chineseTitle' in job else None),
    job_source.jobSalaryMax = job['jobSalaryMax'] if 'jobSalaryMax' in job else None,
    job_source.jobSalaryMin = job['jobSalaryMin'] if 'jobSalaryMin' in job else None,

    job_source.source = json.dumps(job)

    if job_source_result:
        JobSourceRepository.update(job_source, job_name, company_name)
    else:
        job_source.companyName = job['fullCompanyName'] if 'fullCompanyName' in job else None,  # companyName
        job_source.job_name = job['jobName'] if 'jobName' in job else None,  # job_name
        JobSourceRepository.insert(job_source)


if __name__ == '__main__':
    job_source_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(job_source_result[0])
