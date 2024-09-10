from spider.spider_qiancheng.web.python.port.adapter.remote.mq.mq_publisher import MQPublisher
from spider.spider_qiancheng.web.python.port.adapter.utils.config_utils import get_platform_config


def init_queue():
    # 创建队列
    publisher = MQPublisher()
    queue_name = get_platform_config('platform', 'name') + '_' + get_platform_config('channel', 'name')
    publisher.create_queue(queue_name)
