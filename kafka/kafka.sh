#!/bin/bash

# docker exec -it kafka-broker-1 bash
# /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server broker:19092 --topic raw

function run {
  docker exec -i kafka-broker-1 $@
}

# kafka.sh consumer --topic raw --from-beginning

function command_consumer {
  run /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server ${KAFKA_BOOTSTRAP} $@
}

# kafka.sh producer --topic raw

function command_producer {
  run /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server ${KAFKA_BOOTSTRAP} $@
}

# kafka.sh topics --create --topic raw

function command_topics {
  run /opt/kafka/bin/kafka-topics.sh --bootstrap-server ${KAFKA_BOOTSTRAP} $@
}

command=$1
shift
command_$command $@
