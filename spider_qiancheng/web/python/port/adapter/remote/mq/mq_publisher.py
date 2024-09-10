import pika


class MQPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    # 暂时不使用exchange,降低复杂度
    def create_exchange(self, exchange_name):
        # self.channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
        self.channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    def create_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    #每次实例化会创建链接，发送消息后关闭连接
    def send_message(self, queue_name, message):
        self.channel.basic_publish(exchange='',
                                   routing_key=queue_name,
                                   body=message)
        # print(" [x] Sent %r" % message)
        self.close_connection()

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    publisher = MQPublisher()
    # exchange_name = 'lagou'
    # publisher.create_exchange(exchange_name)

    # 创建队列的动作，可以作为初始化，在项目启动时进行，如main服务。
    queue_name = 'lagou_job_list'
    publisher.create_queue(queue_name)

    message = "zuihou"
    publisher.send_message(queue_name, message)
    publisher.close_connection()
