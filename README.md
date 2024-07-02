# Instructions

```
docker build . -t bytewax:0.21.1
docker run -it -v $PWD:/home bytewax:0.20.1 bash

docker run -it -v $PWD/flows/basic:/home bytewax:0.20.1 python -m bytewax.run basic.py
```
