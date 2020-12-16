import datetime
import csv
import sys
import os 

def sol():
    
    read_tsv = csv.reader(open("sample.tsv"), delimiter="\t")
    ids = {}
    for i in read_tsv:
        i = i[0].split()

        checkin_date_str = i[1].split('-')
        checkin_date = datetime.datetime(int(checkin_date_str[0]),int(checkin_date_str[1]),int(checkin_date_str[2]))
        i[1] = checkin_date

        checkout_data_str = i[2].split("-")
        checkout_date = datetime.datetime(int(checkout_data_str[0]),int(checkout_data_str[1]),int(checkout_data_str[2]))
        i[2] = checkout_date

        ids[i[0]] = i[1:len(i)]
    overlap(ids)


def overlap(ids):
    keys = list(ids.keys())
    for idx in range(len(ids)):
        if(idx+1 == len(ids)):
            break
        curr = ids[keys[idx]]
        next = ids[keys[idx+1]]

        if(curr[1] >= next[0]):
            # Find the matching thing between them
            for res in curr[2:-1]:
                if(res in next[2:-1]):
                    print(res,"\t",keys[idx],"\t",keys[idx+1])
            
sol()
