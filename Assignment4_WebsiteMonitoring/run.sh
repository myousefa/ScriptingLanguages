#!/bin/bash
python timeserver.py & 
python trafficgen.py --url http://localhost:8080 --rps 2 --jitter -2 & 
python collector.py --interval 10 --url http://localhost:8080/stats --time 10