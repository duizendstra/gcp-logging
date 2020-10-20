import logging
from flask import Response

def cloud_function_python(request):
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    return Response("", status=201)