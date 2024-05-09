# Instructions

```
docker build . -t bytewax:latest
docker run -it -v $PWD:/home bytewax:latest bash
docker run -it -v $PWD:/home bytewax:latest python -m bytewax.run basic.py
```
