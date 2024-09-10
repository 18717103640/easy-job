import yaml

from spider.spider_qiancheng.web.python.port.adapter.utils.config_constans import ConfigConstans


def get_common_config(model_key, key):
    with open(ConfigConstans.common_config_location, 'r', encoding='utf-8') as stream:
        try:
            config = yaml.safe_load(stream)
            return config[model_key][key]
        except yaml.YAMLError as exc:
            print(exc)
            return None


def get_platform_config(model_key, key):
    with open(ConfigConstans.platform_config_location, 'r', encoding='utf-8') as stream:
        try:
            config = yaml.safe_load(stream)
            return config[model_key][key]
        except yaml.YAMLError as exc:
            print(exc)
            return None


if __name__ == '__main__':
    pass
