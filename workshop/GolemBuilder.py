'''
A golem building golems! Neat.
'''

import logging

from jinja2 import Environment, PackageLoader

from workshop.Golem import Golem

logger = logging.getLogger(__name__)

class GolemBuilder(Golem):
    '''Small temaplting engine that creates all my boilerplate for a new golem.
    '''
    
    def __init__(self, golem_id, golem_type, golem_config):
        super().__init__(golem_id, golem_type, golem_config)
        try:
            self.golem_name= self.config['golem_name']
        except KeyError:
            raise
        self.run()

    def run(self):
        env = Environment(loader=PackageLoader('workshop', 'templates'))
        self.template = env.get_template('golem.py')
        folder = '/'.join(__file__.split('/')[:-1])
        with open(f'{folder}/{self.golem_name}.py', 'w+') as f:
            f.write(self.template.render(golem_name=self.golem_name))

