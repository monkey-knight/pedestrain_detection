# -*- coding: utf-8 -*-

from detection.kafka_producer_consumer import KafkaProducerConsumer

if __name__ == "__main__":
    bootstrap_servers = "localhost:9092"
    topic = "camera1"
    kafka_producer_consumer = KafkaProducerConsumer(bootstrap_servers)
    message = input()
    kafka_producer_consumer.produce(topic, message)
    while True:
        res = kafka_producer_consumer.consume(topic)
        if res is not None:
            print(res)