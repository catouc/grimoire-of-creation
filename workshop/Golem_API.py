'''
Class that represents the golem API, contains methods to create update and
destroy golems.
'''

from flask import request
from flask_restful import Resource, reqparse

from workshop.Golem import Golem

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
            'type': json_data['golem_type']
        }
        golems[golem_id] = golem
        return golem, 201


class Golems_API(Resource):
    '''A master can never be sure what his creations are really up to
    '''
    def get(self):
        return golems

    def post(self):
        json_data = request.get_json(force=True)
        golem = {
            'name': json_data['golem_name'],
            'type': json_data['golem_type']
        }
        golem_id = len(golems)
        Golem(golem_id, json_data['golem_name'], json_data['golem_type'], {})
        golems[golem_id] = golem
        return golem, 201
