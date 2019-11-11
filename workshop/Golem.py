'''
Base implementation of the golems that will be started in a separate thread.
'''

import threading
import time


class Golem(object):
    '''Golems are meant to be created and mindlessly work for it's creator.
    '''

    def __init__(self, golem_id, golem_name, golem_type, golem_config):
        self.id = golem_id
        self.name = golem_name
        self.type = golem_type
        self.config = golem_config
        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()

    def run(self):
        '''Main loop of a golem, will either run continuously on a background
        task or execute one task.
        '''
        print('Template task')
