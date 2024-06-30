## Instructions

https://github.com/apache/kafka/tree/trunk/docker/examples

```
. deploy.env
docker compose -f kafka.compose.yml up -d
```
## Kafka Management
```
docker exec -it kafka-broker-1 bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --create --topic raw

```
## Run FLow
```
docker run -it -v $PWD:/home bytewax:0.20.1 python -m bytewax.run kafka/kafka.py
```
