'''
Base implementation of the golems that will be started in a separate thread.
'''

class Golem(object):
    '''Golems are meant to be created and mindlessly work for it's creator.
    '''

    def __init__(self, golem_id, golem_type, golem_config):
        self.id = golem_id
        self.type = golem_type
        self.config = golem_config
