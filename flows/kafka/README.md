## Instructions

https://github.com/apache/kafka/tree/trunk/docker/examples

```
vi /etc/hosts
   {IP ADDRESS} broker

. deploy.env
docker compose -f kafka.compose.yml up -d
```
## Kafka Management
```
docker exec -it kafka-broker-1 bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --create --topic raw
/opt/kafka/bin/kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --create --topic normalised

```
## Run FLow
```
docker run -it -v $PWD:/home --add-host broker:192.168.1.239 bytewax:0.20.1 python -m bytewax.run kafka/kafka.py

# producer

docker exec -it kafka-broker-1 bash
/opt/kafka/bin/kafka-console-producer.sh --bootstrap-server broker:19092 --topic raw

docker run -it --add-host broker:192.168.1.239 apache/kafka:latest /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server broker:19092 --topic raw
```
