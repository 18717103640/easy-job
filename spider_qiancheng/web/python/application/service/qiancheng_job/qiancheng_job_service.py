from spider.spider_qiancheng.web.python.domain.model.qiancheng_job import QianchengJob
from spider.spider_qiancheng.web.python.domain.repository.qiancheng_job_repoisitory import QianchengJobRepository
from spider.spider_qiancheng.web.python.port.adapter.utils.list_utils import ListUtils
from spider.spider_qiancheng.web.python.application.service.company_third_party.company_third_party_service import \
    is_third_party
import datetime
from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.remote.mq.mq_publisher import MQPublisher
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_platform_config
import json


def find_job_by_brand_name_and_job_name(brand_name, job_name):
    return QianchengJobRepository().find_job_by_brand_name_and_job_name(brand_name, job_name)


def update_job(my_job, id):
    QianchengJobRepository().update(my_job, id)


def insert_qiancheng_job(job):
    my_job = QianchengJob(
        brand_name=job['fullCompanyName'] if 'fullCompanyName' in job else None,
        job_name=job['jobName'] if 'jobName' in job else None,

        salary_desc_min=int(job['jobSalaryMin']) // 1000 if job['jobSalaryMin'] else None,
        salary_desc_max=int(job['jobSalaryMax']) // 1000 if job['jobSalaryMax'] else None,
        salary_desc=job['provideSalaryString'] if 'provideSalaryString' in job else None,  # 8千-1.2万


        city_name=job['jobAreaLevelDetail']['cityString']
        if 'jobAreaLevelDetail' in job and job['jobAreaLevelDetail'].get('cityString', None) else job['jobAreaString'],  # 三元运算符
        area_district=job['jobAreaLevelDetail']['districtString']
        if 'jobAreaLevelDetail' in job and job['jobAreaLevelDetail'].get('districtString', None) else job['jobAreaString'],  # 三元运算符
        business_district=job['jobAreaLevelDetail']['landMarkString']
        if 'jobAreaLevelDetail' in job and job['jobAreaLevelDetail'].get('landMarkString', None) else None,  # 三元运算符
        location=None,  # 这里是详细地址，智联列表页没有，需要详情页，暂设置为none

        brand_scale_name=job['companySizeString'] if 'companySizeString' in job else None,  # 150-500人
        brand_scale_min=None,  # todo 需要自己切割
        brand_scale_max=None,  # todo 需要自己切割

        brand_industry=job['companyIndustryType1Str'] if 'companyIndustryType1Str' in job else None,
        job_degree=job['degreeString'] if 'degreeString' in job else None,
        job_experience=job['workYearString'] if 'workYearString' in job else None,
        brand_stage_name=None,  # 无

        exist_day=None,  # todo 自己算的
        third_party_flag=0,  # todo 自己算的
        source=2,  # 固定为1 lagou
        welfareList=ListUtils.list_dict_to_string(job['jobWelfareCodeDataList'], 'chineseTitle')
        if 'jobWelfareCodeDataList' in job and 'chineseTitle' in job else None,

    )

    ##字段特殊处理
    # scale
    if None == job['companySizeString']:
        my_job.brand_scale_min = 0
        my_job.brand_scale_max = 0

    else:
        brand_scale_name = job['companySizeString']
        if "-" in brand_scale_name:
            my_job.brand_scale_min = brand_scale_name.split("-")[0]
            my_job.brand_scale_max = brand_scale_name.split("-")[1].replace("人", "")
        if "以上" in brand_scale_name:
            my_job.brand_scale_min = 10000
            my_job.brand_scale_max = ''
        if "以下" in brand_scale_name:
            my_job.brand_scale_min = ''
            my_job.brand_scale_max = 20

    brand_name = job['fullCompanyName'] if 'fullCompanyName' in job else None
    job_name = job['jobName'] if 'jobName' in job else None

    # 1 过滤数据 第三方公司  默认值0 正常 1 第三方
    flag = is_third_party(brand_name)
    if flag:
        my_job.third_party_flag = 1

    # source  数据来源(0=boss;1=lagou;2=智联招聘;3=前程无忧)
    my_job.source = 3

    # 发送mq，用于汇总job
    publisher = MQPublisher()
    # 序列化
    job_dict = my_job.to_dict()
    message = json.dumps(job_dict)
    queue_name = get_platform_config('platform', 'name') + '_' + get_platform_config('channel', 'name')
    publisher.send_message(queue_name, message)
    logger.info('发送mq成功，message:{}'.format(message))

    # 3 计算存活天数  根据数据库表 job
    # 查询数据库，避免重复插入
    old_job = find_job_by_brand_name_and_job_name(brand_name, job_name)

    if old_job:
        my_job.exist_day = compute_exist_day(old_job)
        update_job(my_job, id=old_job[0])
    else:
        my_job.exist_day = 1  # 给个默认值1
        QianchengJobRepository().insert(my_job)


def compute_exist_day(old_job):
    today_date_str = str(datetime.date.today())
    updated_date = datetime.datetime.strptime(str(old_job[-1])[0:10], "%Y-%m-%d")
    today_date = datetime.datetime.strptime(today_date_str[0:10], "%Y-%m-%d")
    diff_days = (today_date - updated_date).days
    if diff_days != 0:  # 此处可以使用redis set集合去重，不过不想引入redis，导致更加复杂
        exist_day_old = old_job[17]
        return int(exist_day_old) + diff_days
    else:
        return old_job[17]


if __name__ == '__main__':
    number = 12000

    # 通过整数除法得到前两位数字
    first_two_digits = number // 1000

    print(first_two_digits)  # 输出: 12
