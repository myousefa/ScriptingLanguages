import requests
import argparse
import random
import time 
import math
import sys
import urllib2

default_port = 8080

# Process cmd line args
parser = argparse.ArgumentParser()
parser.add_argument('--url', type = str)
parser.add_argument('--rps', type = float)
parser.add_argument('--jitter', type = float)
args = parser.parse_args()

# Put them into usable fields
url = args.url
rps = args.rps
jitter = args.jitter

# Ensurinng jitter is in appropriate range of .1-1.0
if jitter < 0.1: 
    jitter = 0.1
elif jitter > 1:
    jitter = 1

lower_bound = rps*(1.0-jitter)
upper_bound = rps*(1.0+jitter)

print(jitter)
# ---------------------------------- Initial set up done ----------------------------------

# Generate Requests to url
while True:
    ji