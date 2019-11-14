'''
Golem template
'''

import threading

from Golem import Golem

class {{golem_name}}Golem(Golem):
    '''Template class for a new golem setup
    '''

    def run(self):
        print(f'{self.name} is running!')
