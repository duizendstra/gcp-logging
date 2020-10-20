import logging
import sys 
from flask import Response

def cloud_function_python(request):
    
    sys.stderr.write("log to stderr")
    sys.stdout.write("log to stdout")

    print("log via print")

    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    return Response("", status=201)