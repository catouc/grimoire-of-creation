'''
Class that represents the golem API, contains methods to create update and
destroy golems.
'''

import logging

from flask import request
from flask_restful import Resource

from workshop.GolemBuilder import GolemBuilder
from workshop.AWSHunter import AWSHunter

logger = logging.getLogger(__name__)

golems = {}


class Golem_API(Resource):
    '''Golems are meant to be created and mindlessly work for it's creator.
    '''
    def get(self, golem_id):
        return golems[golem_id]

    def delete(self, golem_id):
        del golems[golem_id]
        return '', 204

    def put(self, golem_id):
        json_data = request.get_json(force=True)
        golem = {
            'name': json_data['golem_name'],
            'type': json_data['golem_type'],
            'config': json_data['golem_config']
        }
        golems[golem_id] = golem
        return golem, 201


class Golems_API(Resource):
    '''A master can never be sure what his creations are really up to
    '''
    def get(self):
        # cursor = get_db_cursor()
        # cursor.execute('SELECT * FROM golems')
        # golems = cursor.fetchall()
        return golems

    def post(self):
        json_data = request.get_json(force=True)
        golem = {
            'type': json_data['golem_type'],
            'config': json_data['golem_config']
        }
        golem_id = len(golems)
        if golem['type'] == 'GolemBuilder':
            if golem['config'].get('golem_name'):
                GolemBuilder(
                    golem_id,
                    golem['type'],
                    golem['config']
                )
            else:
                return '`golem_name` missing inside of the golem config!', 402
        if golem['type'] == 'AWSHunter':
            AWSHunter(
                golem_id,
                golem['type'],
                golem['config']
            )
        golems[golem_id] = golem
        return golem, 201
