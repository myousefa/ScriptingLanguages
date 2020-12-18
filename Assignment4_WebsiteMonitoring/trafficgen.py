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
parser.add_argument('--rps', type = int)
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

lower_bound = int(rps*(1.0-jitter))
upper_bound = int(rps*(1.0+jitter))

print(lower_bound)
print(upper_bound)
print(jitter)
# ---------------------------------- Initial set up done ----------------------------------

# Generate Requests to url
while True:
    start_time = time.time()
    jittery_rps = int(random.uniform(lower_bound,upper_bound))

    #this needs to be jittery rps
    for i in range(jittery_rps): 
        calculate_request = random.randint(0,100)
        try:
            if calculate_request in range(0,10):
                # generate 404 error
                urllib2.urlopen(url + "/404")
            elif calculate_request in range(10,20):
                # generate 500 error
                urllib2.urlopen(url + "/fail")
            else:
                # generate 200 type (Successful request)
                urllib2.urlopen(url)
        except urllib2.HTTPError:
            continue
    end_time = time.time()
    elapsed_time = 1-(end_time-start_time)
    # if elapsed_time > 0:
    #     time.sleep(elapsed_time)
    # else: 
    #     continue
    


