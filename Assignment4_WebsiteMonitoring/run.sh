#!/bin/bash
python timeserver.py & python trafficgen.py --url http://localhost:8080 --rps 2 --jitter -2