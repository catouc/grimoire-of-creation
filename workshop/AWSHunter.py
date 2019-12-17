'''
Golem template
'''

import csv
import datetime
import threading
import json

import boto3

from workshop.Golem import Golem

class AWSHunter(Golem):
    '''AWSHunter is a golem that hunts down all the API events of a single role
    '''

    def __init__(self, golem_id, golem_type, config):
        super().__init__(golem_id, golem_type, config)
        self.session = boto3.Session()
        self.client = self.session.client('cloudtrail')
        if self.config.get('StartTime'):
            self.starttime = self.config.get('StartTime')
            self.stoptime = self.config.get('StopTime')
        else:
            self.stoptime = datetime.datetime.utcnow()
            self.starttime = self.stoptime - datetime.timedelta(minutes=15)
        self.run()

    def run(self):
        events = []
        for e in self.generate_data():
            user = e['userIdentity']
            if user['type'] == 'AssumedRole':
                issuer = user['sessionContext']['sessionIssuer']['arn']
            else:
                issuer = None
            events.append({
                'eventTime': e['eventTime'],
                'eventName': e['eventName'],
                'eventSource': e['eventSource'],
                'readOnly': e['readOnly'],
                'issuer': issuer,
                'errorCode': e.get('errorCode'),
                'errorMessage': e.get('errorMessage')
            })
        with open('/tmp/cloudtrail.csv', 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(events[0].keys())
            for event in events:
                csvwriter.writerow(event.values())

    
    def generate_data(self):
        paginator = self.client.get_paginator('lookup_events')
        for e in paginator.paginate(
                StartTime=self.starttime, EndTime=self.stoptime):
            for event in e['Events']:
                raw = json.loads(event['CloudTrailEvent'])
                raw['readOnly'] = event['ReadOnly']
                yield raw

     
