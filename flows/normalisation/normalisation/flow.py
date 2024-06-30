from bytewax.dataflow import Dataflow
import bytewax.operators as op
from bytewax.connectors.kafka import operators as kop
from bytewax.connectors.stdio import StdOutSink

import confluent_kafka

from login import normalise_login

flow = Dataflow("kafka-example")
brokers = ["broker:19092"]

stream = kop.input("kafka-in", flow, brokers=brokers, topics=["raw"], starting_offset=confluent_kafka.OFFSET_BEGINNING)
events = op.map("extract-event", stream.oks, lambda x: x.value.decode("utf-8"))
processed = op.map("map", events, normalise_login)

op.output("out", processed, StdOutSink())
