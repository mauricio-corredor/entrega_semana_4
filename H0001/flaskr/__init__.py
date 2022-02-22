from flask import Flask

def create_app(config_name):
    app = Flask(__name__)   
    app.config['PROPAGATE_EXCEPTIONS'] = True   
    return app