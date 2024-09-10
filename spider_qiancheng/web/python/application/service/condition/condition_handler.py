from spider.spider_qiancheng.web.python.port.adapter.enviroment.logging_config import logger
from urllib.parse import quote
from spider.spider_qiancheng.web.python.application.service.condition.condition_constants import ConditionConstants


class ConditionHandler:

    @staticmethod
    def generate_condition_customize(parameters, parameter_num):

        if parameter_num > len(parameters):
            logger.error('自定义parameter_num超出最大值！！！')

        salary_list = parameters['salary']  # 月薪范围
        workYear_list = parameters['workYear']  # 工作年限
        degree_list = parameters['degree']  # 学历要求
        companyType_list = parameters['companyType']  # 公司性质
        companySize_list = parameters['companySize']  # 公司规模
        jobterm_list = parameters['jobterm']  # 工作类型
        issuedate_list = parameters['issuedate']  # 日期选项

        parameter_dict_list = []
        parameter_dict_customize_list = []
        parameter_dict = {}

        for salary in salary_list:
            for workYear in workYear_list:
                for degree in degree_list:
                    for companyType in companyType_list:
                        for companySize in companySize_list:
                            for jobterm in jobterm_list:
                                for issuedate in issuedate_list:
                                    parameter_dict['salary'] = salary
                                    parameter_dict['workYear'] = workYear
                                    parameter_dict['degree'] = degree
                                    parameter_dict['companyType'] = companyType
                                    parameter_dict['companySize'] = companySize
                                    parameter_dict['jobterm'] = jobterm
                                    parameter_dict['issuedate'] = issuedate
                                    parameter_dict_new = parameter_dict.copy()
                                    # 注意：上面的代码在每次循环中都使用了 copy() 方法来保证每个字典的独立性，
                                    # 因为字典是引用类型，直接添加可能会导致所有字典指向同一个内存位置。
                                    parameter_dict_list.append(parameter_dict_new)

        zero_num = len(parameters) - parameter_num
        for parameter_dict in parameter_dict_list:
            count = 0
            for parameter_value in parameter_dict.values():
                if parameter_value == '0':
                    count += 1
            if count == zero_num:
                parameter_dict_customize_list.append(parameter_dict)

        return ConditionHandler.generate_condition_str(parameter_dict_customize_list)

    @staticmethod
    def generate_condition(parameters):
        salary_list = parameters['salary']  # 月薪范围
        workYear_list = parameters['workYear']  # 工作年限
        degree_list = parameters['degree']  # 学历要求
        companyType_list = parameters['companyType']  # 公司性质
        companySize_list = parameters['companySize']  # 公司规模
        jobterm_list = parameters['jobterm']  # 工作类型
        issuedate_list = parameters['issuedate']  # 日期选项

        parameter_dict_list = []
        parameter_dict = {}

        for salary in salary_list:
            for workYear in workYear_list:
                for degree in degree_list:
                    for companyType in companyType_list:
                        for companySize in companySize_list:
                            for jobterm in jobterm_list:
                                for issuedate in issuedate_list:
                                    parameter_dict['salary'] = salary
                                    parameter_dict['workYear'] = workYear
                                    parameter_dict['degree'] = degree
                                    parameter_dict['companyType'] = companyType
                                    parameter_dict['companySize'] = companySize
                                    parameter_dict['jobterm'] = jobterm
                                    parameter_dict['issuedate'] = issuedate
                                    parameter_dict_new = parameter_dict.copy()
                                    # 注意：上面的代码在每次循环中都使用了 copy() 方法来保证每个字典的独立性，
                                    # 因为字典是引用类型，直接添加可能会导致所有字典指向同一个内存位置。
                                    parameter_dict_list.append(parameter_dict_new)

        return ConditionHandler.generate_condition_str(parameter_dict_list)

    @staticmethod
    def generate_condition_str(parameter_dict_list):
        condition_list = []
        for parameter in parameter_dict_list:
            request_parameter_str = ""
            for key in parameter.keys():
                if parameter[key] != '0':
                    request_parameter_str = request_parameter_str + '&' + key + '=' + str(parameter[key])
            condition_list.append(request_parameter_str)

        # 使用列表推导式添加前缀
        # new_condition = [prefix + s for s in condition]
        # return new_condition
        return condition_list


if __name__ == '__main__':
    condition_list = ConditionHandler.generate_condition_customize(ConditionConstants.MY_PARAMETER_0, 1)
    for condition in condition_list:
        print(condition)
