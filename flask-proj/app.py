from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def default_route():
    return os.getenv('ENV_VAR_TEST')
