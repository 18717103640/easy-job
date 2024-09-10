import random
from time import sleep
from urllib.parse import parse_qs

from DrissionPage import ChromiumPage
from DrissionPage.errors import *

from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_platform_config


def request_platform(condition, page_num=None):
    try:
        # 组装请求地址url
        prefix = get_platform_config('platform', 'prefix_parameter')
        base_url = get_platform_config('platform', 'base_url')
        real_url = base_url + prefix

        # 创建页面对象，并启动或接管浏览器
        page = ChromiumPage()
        # 设置监听
        match_url = 'https://we.51job.com/api/job/search-pc'
        page.listen.start(match_url)
        # 请求base页面 默认条件都是所有
        page.get(real_url)
        # 根据condition和page_num和页面互动
        click_with_base_page(page, condition, page_num=1)
        # 等待响应
        res = page.listen.wait()
        # 获取响应体
        body = res.response.body
        result = {'job_data': body, 'url': real_url}
        sleep(random.uniform(6, 12))
    except NoRectError:  ## 应对跳转失败导致的一场
        logger.error("请求前程无忧出现异常，爷处出现跳转！！！")
        result = {'job_data': None, 'url': real_url}

    return result


def extract_params(query_string):
    if query_string is None:
        return None
    # 移除开头的"&"符号
    query_string = query_string.lstrip('&')
    # 解析查询字符串并返回每个键对应的单个值
    return {k: v[0] for k, v in parse_qs(query_string).items()}


def click_with_base_page(page, condition, page_num=None):
    # 确定城市  这里以热门城市为例，基本够用，其他城市多一层click动作而已
    page.ele('全部城市').click()
    sleep(2)
    city = get_platform_config('qiancheng', 'city')
    if city != 0:
        page.ele(city).click()
        page.ele('#dilog').eles('tag:button')[1].click()  # 这里有时候会请求不到 应该是反爬虫，不适合经常修改，建议初始化就确定城市
        sleep(3)

    # 确定区域  城市确定后，区域自动加载
    area = get_platform_config('qiancheng', 'area')
    if area != 0:
        page.ele(area).click()
        sleep(3)

    # 确定街道  区域点击后，街道自动加载
    district = get_platform_config('qiancheng', 'district')
    if district != 0:
        page.ele(district).click()
        sleep(3)

    parameters = extract_params(condition)
    if parameters is not None:
        # 展开选项  文本: 展开选项（公司性质、公司规模、工作年限等）
        page.ele('展开选项（公司性质、公司规模、工作年限等）').click()
        # 常规条件处理
        common_parameter_click(page, parameters, 'salary')  # 月薪范围
        common_parameter_click(page, parameters, 'workYear')  # 工作年限
        common_parameter_click(page, parameters, 'degree')  # 学历要求
        common_parameter_click(page, parameters, 'companyType')  # 公司性质
        common_parameter_click(page, parameters, 'companySize')  # 公司规模

        # 特殊处理 工作类型 日期选项
        if parameters.get('jobterm', None) is not None:
            # 点击打开 工作类型 选项
            page.ele('工作类型').next().click()
            sleep(5)
            print(parameters['jobterm'])
            page.ele(parameters['jobterm']).click()
            sleep(5)
        if parameters.get('issuedate', None) is not None:
            # 点击打开 日期选项
            page.ele('发布日期').click()
            sleep(2)
            page.ele(parameters['issuedate']).click()
            sleep(2)
    # 处理分页
    if page_num is not None:
        page.ele('#jump_page').clear()  # 清空元素
        page.ele('#jump_page').input(page_num)  # 设置元素
        page.ele('#jump_page').next(2).click()  # 跳转页面



def common_parameter_click(page, parameters, param_name):
        if parameters.get(param_name, None) is not None:
            page.ele(parameters[param_name]).click()
        sleep(2)


if __name__ == '__main__':
    pass
