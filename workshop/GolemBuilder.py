'''
A golem building golems! Neat.
'''

import threading

from jinja2 import Environment, PackageLoader

from workshop.Golem import Golem

class GolemBuilder(Golem):
    '''Small temaplting engine that creates all my boilerplate for a new golem.
    '''
    
    def __init__(self, golem_id, golem_name, golem_type, golem_config):
        super().__init__(golem_id, golem_name, golem_type, golem_config)

    def run(self):
        env = Environment(loader=PackageLoader('workshop', 'templates'))
        self.template = env.get_template('golem.py')
        print(self.template.render(golem_name=self.name))

