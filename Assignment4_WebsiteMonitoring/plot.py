from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
import os

def RPR(data):
    """
    Requests Per Record
    This function calculates the neumber of requests
    that occured in each record by finding the diff between
    the current and the last record
    """
    res = []
    for rt,req_type in enumerate(data):
        record = []
        record.append(req_type[0])
        for i in range(1,len(req_type)):
            diff = data[rt][i] - data[rt][i-1]
            record.append(diff)
        res.append(record)
    return res



def grab_data():
    data = []
    data_200 = []
    data_404 = []
    data_500 = []
    rps = 0
    with open('data.tsv', 'r', buffering = 1) as tsvfile:
        for line in tsvfile:
            line = line.split()
            time = line[0]
            data_500.append(int(line[1]))
            data_200.append(int(line[2]))
            data_404.append(int(line[3]))
    # Remove first record
    data_200 = data_200[1:]
    data_404 = data_404[1:]
    data_500 = data_500[1:]

    data.append(data_200)
    data.append(data_404)
    data.append(data_500)
    
    # Currently, the data summates as it goes
    # Find the diff by each record
    data = RPR(data)
    
    # Set up for RPM
    rpm_200 = np.zeros( (len(data[0])//6),) 
    rpm_404 = np.zeros( (len(data[0])//6),) 
    rpm_500 = np.zeros( (len(data[0])//6),)
    rpm_data = np.array([rpm_200,rpm_404,rpm_500])

    for rt,req_type in enumerate(data):
        record_count = 0
        min_total = 0
        for i in range(len(req_type)):
            if(record_count == 6):
                #rpm_data[rt] = np.append(rpm_data[rt],min_total)
                #rpm_data[rt].append(min_total)
                #print()
                rpm_data[rt,int(float(i/60)*10)] = min_total
                min_total = 0
                record_count = 0
                min_total += req_type[i]
                record_count += 1
            else:
                min_total += req_type[i]
                record_count += 1
    
    rpm_data[0] = np.array(rpm_data[0])
    rpm_data[1] = np.array(rpm_data[1])
    rpm_data[2] = np.array(rpm_data[2])

    rps_data = rpm_data[:] // 60

    fig,ax = plt.subplots(1)

    plt.plot(rps_data[0],color='r')
    plt.plot(rps_data[1],color='g')
    plt.plot(rps_data[2],color='b')

    plt.xlabel('time (minutes)')
    plt.ylabel('RPS (in minutes)')
    plt.legend(('200s', '500s', '404s'))
    plt.savefig("graph2.png")
    
grab_data()