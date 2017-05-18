#! usr/bin/env Python 2.7
"""This is an early implementation jsonParser \nto retrieve Configuration
from a centralized server \nif the configuration format is json"""
import json


def parse_json(json_to_be_parsed):
    data = json.loads(json_to_be_parsed)
    print "Name : " + data['propertySources'][0]['name']
    print "ENABLE_SMS : " + data['propertySources'][0]['source']['ENABLE_SMS']
    print "ENV : " + data['propertySources'][0]['source']['ENV']
    print "LOGLEVEL : " + data['propertySources'][0]['source']['LOGLEVEL']
    print "DB_URL : " + data['propertySources'][0]['source']['DB_URL']

