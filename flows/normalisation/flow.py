import os
import json
import confluent_kafka

from bytewax.dataflow import Dataflow
from bytewax.connectors.kafka import KafkaSource, KafkaSink, SerializedKafkaSinkMessage
import bytewax.operators as op

import event.login
import event.system

brokers   = os.environ["KAFKA_BROKERS"].split(",")
flow      = Dataflow("normalisation")

source    = KafkaSource(brokers=brokers, topics=["raw"], starting_offset=confluent_kafka.OFFSET_BEGINNING)
sink      = KafkaSink(brokers=brokers, topic="normalised")

stream    = op.input("in", flow, source)
events    = op.map("extract", stream, lambda x: x.value.decode("utf-8"))
logins    = op.branch("filter_logins", events, event.login.recognise)
systems   = op.branch("filter_systems", logins.falses, event.system.recognise)
logins_n  = op.map("normalise_logins", logins.trues, event.login.normalise)
systems_n = op.map("normalise_systems", systems.trues, event.system.normalise)
combined  = op.merge("merge", logins_n, systems_n)
out       = op.map("message", combined, lambda x: SerializedKafkaSinkMessage(key=None, value=json.dumps(x)))

op.inspect("debug", out)
op.inspect("unmatched", systems.falses)

op.output("out", out, sink)
