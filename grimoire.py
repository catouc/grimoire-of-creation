'''
A powerful book containing all kinds of utility golems ready to server for
their new master.
'''

from flask import Flask
from flask_restful import Api

from workshop import Golem_API

app = Flask(__name__)
api = Api(app)

api.add_resource(Golem.Golems, '/golems')
api.add_resource(Golem.Golem, '/golem/<golem_id>')

if __name__ == "__main__":
    app.run(debug=True)
