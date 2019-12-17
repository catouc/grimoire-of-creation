'''
Golem template
'''

import datetime
import logging

import boto3

from workshop.Golem import Golem

logger = logging.getLogger(__name__)

class AWSInspector(Golem):
    '''Template class for a new golem setup
    '''
    
    def __init__(self, golem_id, golem_type, config):
        super().__init__(golem_id, golem_type, config)
        self.run()

    def run(self):
        print(f'{self.name} is running!')

    
