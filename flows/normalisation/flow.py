import os
import confluent_kafka

from bytewax.dataflow import Dataflow
import bytewax.operators as op
from bytewax.connectors.kafka import KafkaSource, KafkaSink, KafkaSinkMessage
from bytewax.connectors.stdio import StdOutSink

from login import normalise_login

brokers   = os.environ["KAFKA_BROKERS"].split(",")
flow      = Dataflow("normalisation")

source    = KafkaSource(brokers=brokers, topics=["raw"], starting_offset=confluent_kafka.OFFSET_BEGINNING)
stream    = op.input("raw-in", flow, source)
events    = op.map("extract-events", stream, lambda x: x.value.decode("utf-8"))
processed = op.map("map", events, normalise_login)

op.output("normalised-out", processed, StdOutSink())
