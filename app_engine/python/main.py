import logging
from flask import Response
from flask import Flask

app = Flask(__name__)

@app.route('/')
def app_engine_python():
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    return Response("", status=201)
