from os import path
from flask import Flask, config
from flask import g
import sqlite3 as sql

def create_app():

    from .controller import controller
    

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'opa meu irmao como vai'

    app.register_blueprint(controller, url_prefix = "/")

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return app