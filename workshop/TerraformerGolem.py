'''
Terraform templating golem
'''

import threading

from Golem import Golem

class TerraformerGolem(Golem):
    '''Small temaplting engine that creates all my boilerplate for the tf code
    '''

    def run(self):
        print('Terraforming something!')
