#!/bin/bash

podman build -t hellostreamlit -f Dockerfile .

podman run -d -p  8501:8501 --name streamlitstarter hellostreamlit

