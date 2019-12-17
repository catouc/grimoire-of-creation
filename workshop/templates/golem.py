'''
Golem template
'''

import logging

from workshop.Golem import Golem

logger = logging.getLogger(__name__)

class {{golem_name}}(Golem):
    '''Template class for a new golem setup
    '''
    
    def __init__(self, golem_id, golem_type, golem_config):
        super().__init__(golem_id, golem_type, golem_config)
        # insert additional init code here
        self.run()

    def run(self):
        print(f'{self.name} is running!')
