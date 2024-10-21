#!/usr/bin/sh

docker kill "frontendcoders" > /dev/null 2>&1;
docker run --rm --name frontendcoders -d -p 8501:8501 frontendcoders:latest
