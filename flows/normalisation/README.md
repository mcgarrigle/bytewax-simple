## Instructions

Setup kafka broker (see ../kafka/README.md)
```
cat fixtures/access.log | ../kafka/kafka.sh producer --topic raw
. deploy.env
docker compose -f flow.compose.yml up
```
