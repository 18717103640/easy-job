import random
from time import sleep
from urllib.parse import parse_qs

from DrissionPage import ChromiumPage
from DrissionPage._elements.chromium_element import ChromiumElement
from DrissionPage.errors import *

from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from spider.spider_qiancheng.web.python.port.adapter.enviroment.singleton_meta import SingletonMeta
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_platform_config


# 这个类只会实例化一次，但是，监听的数据包一直是初始化的那一个。
class DrissionPageHandler(metaclass=SingletonMeta):

    def __init__(self):
        try:
            logger.warning("DrissionPageHandler init ！！！")
            # 创建页面对象，并启动或接管浏览器
            self.page = ChromiumPage(10003)
            # 设置监听
            match_url = 'https://we.51job.com/api/job/search-pc'
            self.page.listen.start(match_url)
            # 请求base页面 默认条件都是所有
            self.page.get(DrissionPageHandler.get_real_url())
            res = self.page.listen.wait()

            # 先行设置城市区域街道，后面基本不会修改
            # 确定城市  这里以热门城市为例，基本够用，其他城市多一层click动作而已
            self.page.ele('全部城市').click()
            sleep(2)
            city = get_platform_config('qiancheng', 'city')
            if city != 0:
                self.page.ele(city).click()
                self.page.ele('#dilog').eles('tag:button')[1].click()  # 这里有时候会请求不到 应该是反爬虫，不适合经常修改，建议初始化就确定城市
                sleep(2)
                res = self.page.listen.wait()

            # 确定区域  城市确定后，区域自动加载
            area = get_platform_config('qiancheng', 'area')
            if area != 0:
                self.page.ele(area).click()
                sleep(1)
                res = self.page.listen.wait()

            # 确定街道  区域点击后，街道自动加载
            district = get_platform_config('qiancheng', 'district')
            if district != 0:
                self.page.ele(district).click()
                sleep(1)
                res = self.page.listen.wait()

            self.res_list = []

        except NoRectError:  # 应对跳转失败导致的一场
            logger.error("请求前程无忧出现异常，页面出现跳转！！！")
            exit()

    def response_listen(self, match_url):
        self.page.listen.start(match_url)

    def response_wait(self):
        res = self.page.listen.wait()
        self.res_list.append(res)

    def open_options(self):
        if self.page.ele('展开选项') is not None:
            if type(self.page.ele('展开选项')) is ChromiumElement:
                # 展开选项  文本: 展开选项（公司性质、公司规模、工作年限等） 后面不再展开
                self.page.ele('展开选项').click()

    def close_options(self):
        # 展开选项  文本: 展开选项（公司性质、公司规模、工作年限等） 后面不再展开
        self.page.ele('收起选项').click()

    @staticmethod
    def get_real_url():
        # 组装请求地址url
        prefix = get_platform_config('platform', 'prefix_parameter')
        base_url = get_platform_config('platform', 'base_url')
        return base_url + prefix

    def request_platform(self, condition, page_num=None):
        try:
            # 置空接口响应list
            self.res_list = []
            # 展开选项
            DrissionPageHandler().open_options()
            # 根据condition和page_num和页面互动
            DrissionPageHandler().click_with_base_page(condition, page_num=page_num)

            # 获取响应体
            body = self.res_list[-1].response.body
            logger.warning(body)

            # 获取condition对应body后 置空条件
            DrissionPageHandler().reset_page_null()

            # 处理html字符串异常
            if (type(body) is str
                    or body is None
                    or body.get('resultbody', None).get('job', None) is None):
                return {'job_data': None, 'url': None}

            return {'job_data': body, 'url': None}

        except NoRectError:  ## 应对跳转失败导致的一场
            logger.error("请求前程无忧出现异常，页面出现跳转！！！")
            exit()

    @staticmethod
    def extract_params(query_string):
        if query_string is None:
            return None
        # 移除开头的"&"符号
        query_string = query_string.lstrip('&')
        # 解析查询字符串并返回每个键对应的单个值
        return {k: v[0] for k, v in parse_qs(query_string).items()}

    def click_with_base_page(self, condition, page_num=None):
        parameters = DrissionPageHandler.extract_params(condition)
        if parameters is not None:

            # 常规条件处理
            DrissionPageHandler().common_parameter_click(parameters, 'salary')  # 月薪范围
            DrissionPageHandler().common_parameter_click(parameters, 'workYear')  # 工作年限
            DrissionPageHandler().common_parameter_click(parameters, 'degree')  # 学历要求
            DrissionPageHandler().common_parameter_click(parameters, 'companyType')  # 公司性质
            DrissionPageHandler().common_parameter_click(parameters, 'companySize')  # 公司规模

            # 特殊处理 工作类型 日期选项
            if parameters.get('jobterm', None) is not None:
                # 点击打开 工作类型 选项
                self.page.ele('工作类型').next().click()
                sleep(1)
                print(parameters['jobterm'])
                self.page.ele(parameters['jobterm']).click()
                sleep(1)
                DrissionPageHandler().response_wait()
            if parameters.get('issuedate', None) is not None:
                # 点击打开 日期选项
                self.page.ele('发布日期').click()
                sleep(1)
                self.page.ele(parameters['issuedate']).click()
                sleep(1)
                DrissionPageHandler().response_wait()
        # 处理分页
        if page_num is not None:
            if self.page.ele('#jump_page') is not None:
                if type(self.page.ele('#jump_page')) is ChromiumElement:
                    self.page.ele('#jump_page').clear()  # 清空元素
                    self.page.ele('#jump_page').input(page_num)  # 设置元素
                    self.page.ele('#jump_page').next(2).click()  # 跳转页面
                    sleep(1)
                    DrissionPageHandler().response_wait()

    def common_parameter_click(self, parameters, param_name):
        if parameters.get(param_name, None) is not None:
            self.page.ele(parameters[param_name]).click()
            sleep(1)
            DrissionPageHandler().response_wait()

    def reset_page_null(self):
        self.page.ele('月薪范围').next(1).ele('@text()=所有').click()
        self.page.ele('工作年限').next(1).ele('@text()=所有').click()
        self.page.ele('学历要求').next(1).ele('@text()=所有').click()
        self.page.ele('公司性质').next(1).ele('@text()=所有').click()
        self.page.ele('公司规模').next(1).ele('@text()=所有').click()


if __name__ == '__main__':
    condition = None
    result = DrissionPageHandler().request_platform(condition, 6)
    condition = '&salary=1.5-2万'
    result_0 = DrissionPageHandler().request_platform(condition, 2)
    print(result)
