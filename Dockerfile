# Start from a debian slim with python support
FROM python:3.11-slim-bullseye
# Setup a workdir where we can put our dataflow
WORKDIR /home
RUN apt-get update && apt-get install -y git
# Install bytewax and the dependencies you need here
RUN pip install bytewax==0.20.1 confluent_kafka==2.4.0
# Set PYTHONUNBUFFERED to any value to make python flush stdout,
# or you risk not seeing any output from your python scripts.
ENV PYTHONUNBUFFERED 1
CMD ["python", "-m", "bytewax.run", "dataflow"]
