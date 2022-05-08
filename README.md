# Distributed System HW2 : Benchmark Kafka

成大資訊系 分散式系統 作業2: Benchmark kafka

## Homework requirements

* 敘述實驗環境
* 建立Kafka Cluster
* 執行Benchmark
* **優化傳遞Record的平均Latency**
* 報告思路與紀錄過程

## Kafka Cluster set up

此次作業使用Docker-compose來建立kafka cluster。

```shell
docker-compose up -d
```

進入kafka server

```shell
docker exec -it kafka_kafka_1 /bin/bash
```

所有可以使用的cp-kafka內建指令都在`../../bin`底下，可以用`ls ../../bin | grep kafka`來查看。

建立consumer

```shell
kafka-console-consumer --bootstrap-server kafka:9092 --from-beginning --topic my-first-topic
```

建立producer

```shell
kafka-console-producer --broker-list kafka:9092 --topic my-first-topic
```

就可以用producer傳message(record)給consumer了。

## Python

也可以用python來對kafka做操作

```shell
pip install kafka-python
```

使用方式可以參考`producer.py`和`consumer.py`
