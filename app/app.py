#!/usr/bin/env python

import argparse
import logging
import sys
import os
import time


def run_producer(broker_servers, kafka_topic, log):
    from confluent_kafka import Producer
    from random import choice
    import uuid

    def delivery_callback(err, msg):
        if err:
            log.error('Message delivery failed: {}'.format(err))
        else:
            log.info("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    p = Producer({'bootstrap.servers': broker_servers})
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    while True:
        for _ in range(4):
            user_id = choice(user_ids)
            product = choice(products)
            item_uuid = str(uuid.uuid4())
            p.produce(kafka_topic, '{}:{}'.format(item_uuid, product), user_id, callback=delivery_callback)
        p.poll(2000)
        p.flush()
        time.sleep(10)


def run_consumer(broker_servers, kafka_topic, log):
    from confluent_kafka import Consumer, OFFSET_BEGINNING

    conf = {
        'bootstrap.servers': broker_servers,
        'group.id': 'myapp',
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'
    }
    c = Consumer(conf)

    def reset_offset(c, partitions):
        for p in partitions:
            p.offset = OFFSET_BEGINNING
        c.assign(partitions)

    c.subscribe([kafka_topic], on_assign=reset_offset)
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                log.info("Waiting...")
            elif msg.error():
                log.error(str(msg.error()))
            else:
                log.info("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        c.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices=('producer', 'consumer'), default='producer')
    parser.add_argument('-t', '--topic', type=str, default='myapp-topic')
    args = parser.parse_args()
    logger = logging.getLogger(args.mode)
    logger.setLevel(logging.INFO)
    logger_handler = logging.StreamHandler()
    logger.addHandler(logger_handler)
    logger_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'))
    brokers = os.environ.get('KAFKA_BROKERS', None)
    if not brokers or not brokers.strip():
        logger.exception("Environment variable KAFKA_CLUSTERS_BOOTSTRAP_SERVERS not set or empty. Exiting")
        sys.exit(1)
    else:
        logger.info("Bootstrap servers are {}".format(brokers))
    logger.info("Sleeping for 10 seconds before starting this app...")
    time.sleep(10)
    logger.info("Sleep over...")
    if args.mode == 'consumer':
        logger.info("Starting Consumer...")
        run_consumer(brokers, args.topic, logger)
    else:
        logger.info("Starting Producer...")
        run_producer(brokers, args.topic, logger)
