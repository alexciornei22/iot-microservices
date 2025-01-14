#!/usr/bin/env bash

export SCD_DVP=$(PWD)/mosquitto:$(PWD)/grafana/dashboards:$(PWD)/grafana/provisioning

docker build ./adapter -t sensors/adapter --no-cache

docker swarm init

docker swarm deploy -c stack.yml scd3