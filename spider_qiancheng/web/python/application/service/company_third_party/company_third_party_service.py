from spider.spider_qiancheng.web.python.domain.repository.company_third_party_repository import (
    CompanyThirdPartyRepository)
from spider.spider_qiancheng.web.python.domain.repository.qiancheng_job_repoisitory import QianchengJobRepository


def add_third_party(brand_name, third_party_type):
    # 新增第三方公司
    CompanyThirdPartyRepository.insert(brand_name, third_party_type)
    # 立即过滤job表，修改响应job的third_party_flag字段为1
    third_party_filter(brand_name)


def third_party_filter(brand_name):
    job_list = QianchengJobRepository.find_list(brand_name)
    for job in job_list:
        QianchengJobRepository.update_third_party_by_id(job[0])
        print('当前公司：' + str(job[1] + '当前岗位：' + str(job[2]) + '过滤完毕！！！' + '\n'))


def is_third_party(brand_name):
    if '某' in brand_name:
        return True
    result = CompanyThirdPartyRepository.find_by_brand_name(brand_name)
    if len(result) == 0:
        return False
    for job in result:
        if job[1] in brand_name:
            return True
    return True


def find_all_third_party_company():
    return CompanyThirdPartyRepository.find_all()


if __name__ == '__main__':
    pass
