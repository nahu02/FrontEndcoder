#!/usr/bin/sh

docker kill "frontendcoders" > /dev/null 2>&1;
docker run --rm --name frontendcoders -d --network host frontendcoders:latest
