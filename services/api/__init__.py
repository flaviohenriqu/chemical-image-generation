# services/__init__.py
import os

import connexion
import logging


def create_app(script_info=None):

    # instantiate the app
    con_app = connexion.FlaskApp(__name__, specification_dir='docs/')
    con_app.add_api('api.yaml', options={'swagger_url': '/docs'})

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    con_app.app.config.from_object(app_settings)

    return con_app

