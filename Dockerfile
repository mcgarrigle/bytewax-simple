# Start from a debian slim with python support
FROM python:3.11-slim-bullseye
# Setup a workdir where we can put our dataflow
WORKDIR /home
# Install bytewax and the dependencies you need here
RUN pip install bytewax==0.18.0
# Set PYTHONUNBUFFERED to any value to make python flush stdout,
# or you risk not seeing any output from your python scripts.
ENV PYTHONUNBUFFERED 1
CMD ["python", "-m", "bytewax.run", "dataflow"]
