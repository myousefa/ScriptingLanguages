import requests
import argparse
import random
import time 
import math
import urllib2
import os 
import sys
import json
import csv

default_port = 8080
out_file = 'data.tsv'

# Process cmd line args
parser = argparse.ArgumentParser()
parser.add_argument('--interval', type = int, default = 10)
parser.add_argument('--url', type = str)
parser.add_argument('--time_running', type = int, default = 60)
args = parser.parse_args()

# Put them into usable fields
interval = args.interval
time_running  = args.time_running

while(time_running > 0):
    with open(out_file, "w", buffering = 1) as tsvfile:
        while True:
            stats = requests.get('http://localhost:8080/stats').text[:-1]
            tab_deliminator = '\t'.join([str(n) for n in stats.split() if n.isdigit()])
            tsvfile.write("{0}\n".format(tab_deliminator))
            if time_running == 0: 
                break
            else:
                time_running-=1
                time.sleep(interval)