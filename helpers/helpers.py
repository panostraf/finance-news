import os
from collections import defaultdict
import json
import datetime
import re

def number_of_files(path="./data/articles/"):
    count = 0
    dir_path = path
    for path in os.scandir(dir_path):
        if path.is_file():
            count += 1 
    print(count)
    return count

def convert_date(dt_str):
    '''
    Input str date from scrapped articles to Y-m-d
    '''
    months ={
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
    }
    try:
        # use regex to extract date
        found = re.search('[A-Za-z]{3}\s[0-9]{2},\s[0-9]{4}',str(dt_str))
        
        found = found[0].lower()
        found = found.replace(',','')
        found = found.split()

        month_ = str(months[found[0]]).strip()
        if len(month_)<2:
            month_ = '0' + month_
        day_   = str(found[1]).strip()
        year_  = str(found[2]).strip()

        date = f"{year_}-{month_}-{day_}"
        # return datetime.datetime.strptime(date,"%Y-%m-%d")
        return date
    except AttributeError:
        return dt_str

if __name__=='__main__':
    number_of_files()