# Instructions

```
docker build . -t bytewax:0.21.1
docker run -it -v $PWD:/home bytewax:0.20.1 bash

docker run -it -v ${PWD}/flows:/home bytewax:0.20.1 python -m bytewax.run basic/flow.py

# with kafka

docker run -it -e KAFKA_BROKERS -v ${PWD}/flows:/home --add-host broker:192.168.1.239 bytewax:0.20.1 python -m bytewax.run normalisation/flow.py
```
