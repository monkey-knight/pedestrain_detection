# -*- coding: utf-8 -*-

from kafka import KafkaProducer
from kafka import KafkaConsumer


class KafkaProducerConsumer:
    """
    KafkaProducerConsumer类能够向kafka指定的topic发送消息，从kafka指定的topic接受消息
    """
    def __init__(self, bootstrap_servers):
        self.__producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.__consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)

    def produce(self, topic, value, key=None, partition=None, timestamp_ms=None):
        """
        向kafka指定的topic主题发送消息value。
        :param topic: 消息发送的目的topic
        :param value: 消息的内容
        :param key: 消息对应的关键字
        :param partition: topic的分组
        :param timestamp_ms: 时间戳
        :return:
        """
        value = bytes(value, encoding="utf-8")
        self.__producer.send(topic, value, key, partition, timestamp_ms)
        self.__producer.flush()

    def consume(self, topic):
        """
        从kafka指定的topic中拿取数据
        :param topic:
        :return:
        """
        self.__consumer.subscribe(topic)
        message = self.__consumer.poll(timeout_ms=5)
        return message
