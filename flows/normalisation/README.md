## Instructions

Setup kafka broker (see ../kafka/README.md)
```
. deploy.env
cat fixtures/access.log | ../kafka/kafka.sh producer --topic raw
docker compose -f flow.compose.yml up
```
