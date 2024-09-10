import pika


class MQReceiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def callback(self,ch, method, properties, body):
        print(" [x] Received %r" % body)

    def consumer(self,queue_name):
        # 设置队列的消费者
        self.channel.basic_consume(queue=queue_name,
                              on_message_callback=self.callback,
                              auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


if __name__ == '__main__':
    receiver = MQReceiver()
    queue_name='lagou_job_list'
    receiver.consumer(queue_name)
