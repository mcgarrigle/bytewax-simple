import os
import confluent_kafka

from bytewax.dataflow import Dataflow
from bytewax.connectors.kafka import KafkaSource, KafkaSink, SerializedKafkaSinkMessage
import bytewax.operators as op

from login import is_login, normalise_login

brokers   = os.environ["KAFKA_BROKERS"].split(",")
flow      = Dataflow("normalisation")

source    = KafkaSource(brokers=brokers, topics=["raw"], starting_offset=confluent_kafka.OFFSET_BEGINNING)
sink      = KafkaSink(brokers=brokers, topic="normalised")

stream    = op.input("in", flow, source)
events    = op.map("extract", stream, lambda x: x.value.decode("utf-8"))
logins    = op.filter("filter_logins", events, is_login)
processed = op.map("map", logins, normalise_login)
out       = op.map("out", processed, lambda x: SerializedKafkaSinkMessage(key=None, value=x))

op.inspect("debug", out)

op.output("normalised-out", out, sink)
