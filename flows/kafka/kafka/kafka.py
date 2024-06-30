import time

import bytewax.operators as op
from bytewax.connectors.kafka import operators as kop
from bytewax.connectors.stdio import StdOutSink
from bytewax.dataflow import Dataflow

flow = Dataflow("kafka-example")

brokers = ["broker:19092"]

# stream = op.input("kafka-in", flow, KafkaSource(brokers, ["raw"]))
stream = kop.input("kafka-in", flow, brokers=brokers, topics=["raw"])
# double = op.map("double", stream, times_two)
out = op.map("map", stream.oks, lambda x: x)

op.output("out", out, StdOutSink())
