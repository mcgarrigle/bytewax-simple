# Instructions

```
docker build . -t bytewax:latest
docker run -it -v $PWD:/home bytewax:0.20.1 bash

docker run -it -v $PWD/flows/basic:/home bytewax:0.20.1 python -m bytewax.run basic.py
```
