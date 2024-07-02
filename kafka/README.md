## Instructions

https://github.com/apache/kafka/tree/trunk/docker/examples

```
vi /etc/hosts
   {IP ADDRESS} broker

. deployment.env
docker compose -f kafka.compose.yml up -d
```
## Kafka Management
```
docker exec -it kafka-broker-1 bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server broker:19092 --create --topic raw
/opt/kafka/bin/kafka-topics.sh --bootstrap-server broker:19092 --create --topic normalised

```
## Kafka Operations
```
# producer

docker exec -it kafka-broker-1 /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server broker:19092 --topic raw

```
