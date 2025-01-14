#!/usr/bin/env bash

docker build ./adapter -t sensors/adapter

docker swarm init

docker stack deploy -c stack.yml scd3