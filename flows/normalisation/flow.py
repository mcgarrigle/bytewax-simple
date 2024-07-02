import os
import confluent_kafka

from bytewax.dataflow import Dataflow
from bytewax.connectors.kafka import KafkaSource, KafkaSink, SerializedKafkaSinkMessage
import bytewax.operators as op

from login import normalise_login

brokers   = os.environ["KAFKA_BROKERS"].split(",")
flow      = Dataflow("normalisation")

source    = KafkaSource(brokers=brokers, topics=["raw"], starting_offset=confluent_kafka.OFFSET_BEGINNING)
sink      = KafkaSink(brokers=brokers, topic="normalised")

stream    = op.input("raw-in", flow, source)
events    = op.map("extract-events", stream, lambda x: x.value.decode("utf-8"))
processed = op.map("map", events, normalise_login)
out       = op.map("out", processed, lambda x: SerializedKafkaSinkMessage(key=None, value=x))

# op.inspect("debug", out)

op.output("normalised-out", out, sink)
