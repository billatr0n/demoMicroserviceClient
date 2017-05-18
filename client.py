#! usr/bin/env Python 2.7
"""This is an early implementation client \n to retrieve Configuration from a centralized server \n pip prerequisites: requests, yaml by doing pip install requests"""

import requests
import yaml


def perform_request_to_config_server(config_server_url, microservice, environment, branch):
    r = requests.get(config_server_url + '/' + branch + '/' + microservice + '-' + environment + '.yml',
                     auth=('admin', 'nimda'))
    construct_title('Fetching ' + environment + ' configuration for ' + microservice, '-')
    construct_title('Starting extracting configuration from the json response', '-')
    y = yaml.load(r.text)
    print y


def construct_title(title, delimiter):
    print delimiter * len(title)
    print title
    print delimiter * len(title)


perform_request_to_config_server("http://localhost:8888", "janus", "prod", "release-1.0.0")
