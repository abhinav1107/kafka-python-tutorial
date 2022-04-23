# kafka-python-tutorial
learning how kafka producer consumer works. WIP

simply run
```commandline
docker-compose up --build -d
```

this should start some containers
```commandline
$ docker-compose ps
     Name                   Command               State                                   Ports
--------------------------------------------------------------------------------------------------------------------------------
kafka-consumer   python3 app.py -m consumer       Up      9092/tcp
kafka-producer   python3 app.py                   Up      9092/tcp
kafka-ui         /bin/sh -c java $JAVA_OPTS ...   Up      0.0.0.0:8080->8080/tcp,:::8080->8080/tcp
kafka1           /etc/confluent/docker/run        Up      0.0.0.0:9092->9092/tcp,:::9092->9092/tcp
kafka2           /etc/confluent/docker/run        Up      9092/tcp, 0.0.0.0:9093->9093/tcp,:::9093->9093/tcp
kafka3           /etc/confluent/docker/run        Up      9092/tcp, 0.0.0.0:9094->9094/tcp,:::9094->9094/tcp
zoo1             /etc/confluent/docker/run        Up      0.0.0.0:2181->2181/tcp,:::2181->2181/tcp, 2888/tcp, 3888/tcp
zoo2             /etc/confluent/docker/run        Up      2181/tcp, 0.0.0.0:2182->2182/tcp,:::2182->2182/tcp, 2888/tcp, 3888/tcp
zoo3             /etc/confluent/docker/run        Up      2181/tcp, 0.0.0.0:2183->2183/tcp,:::2183->2183/tcp, 2888/tcp, 3888/tcp
```

check the logs:
```commandline
$ docker-compose logs --tail=1 -f
Attaching to kafka-consumer, kafka-producer, kafka-ui, kafka2, kafka1, kafka3, zoo3, zoo2, zoo1
kafka-consumer    | 2022-04-23 16:34:02,264 INFO consumer: Consumed event from topic myapp-topic: key = awalther     value = f3ec2e94-c50a-4d32-8daa-a89fc2a9127d:alarm clock
kafka-ui          | 2022-04-23 16:33:55,356 DEBUG [kafka-admin-client-thread | adminclient-2] c.p.k.u.s.ClustersMetricsScheduler: Metrics updated for cluster: dockerlocal
kafka2            | [2022-04-23 16:32:32,069] INFO [Broker id=2] Add 50 partitions and deleted 0 partitions from metadata cache in response to UpdateMetadata request sent by controller 1 epoch 1 with correlation id 3 (state.change.logger)
kafka-producer    | 2022-04-23 16:34:02,263 INFO producer: Produced event to topic myapp-topic: key = awalther     value = f3ec2e94-c50a-4d32-8daa-a89fc2a9127d:alarm clock
kafka1            | [2022-04-23 16:32:35,604] INFO [GroupCoordinator 1]: Assignment received from leader rdkafka-c818def6-10e1-4460-b9c8-e225550caaa0 for group myapp for generation 1. The group has 1 members, 0 of which are static. (kafka.coordinator.group.GroupCoordinator)
kafka3            | [2022-04-23 16:32:32,093] INFO [Broker id=3] Add 50 partitions and deleted 0 partitions from metadata cache in response to UpdateMetadata request sent by controller 1 epoch 1 with correlation id 4 (state.change.logger)
zoo1              | [2022-04-23 16:32:55,402] INFO Committing global session 0x200015504ef0002 (org.apache.zookeeper.server.quorum.LearnerSessionTracker)
zoo3              | [2022-04-23 16:32:55,402] INFO Committing global session 0x200015504ef0002 (org.apache.zookeeper.server.quorum.LeaderSessionTracker)
zoo2              | [2022-04-23 16:32:55,402] INFO Committing global session 0x200015504ef0002 (org.apache.zookeeper.server.quorum.LearnerSessionTracker)
kafka-consumer    | 2022-04-23 16:34:03,264 INFO consumer: Waiting...
kafka-consumer    | 2022-04-23 16:34:04,265 INFO consumer: Waiting...
kafka-consumer    | 2022-04-23 16:34:05,265 INFO consumer: Waiting...
kafka-consumer    | 2022-04-23 16:34:06,266 INFO consumer: Waiting...
kafka-consumer    | 2022-04-23 16:34:07,266 INFO consumer: Waiting...
kafka-consumer    | 2022-04-23 16:34:08,267 INFO consumer: Waiting...
```

that's it for now.