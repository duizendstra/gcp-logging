import logging
import sys 
from flask import Response

def cloud_function_python(request):
    
    sys.stderr.write("log to stderr")
    sys.stdout.write("log to stdout")

    print("log via print")

    logging.debug("logging.debug")
    logging.info("logging.info")

    logging.warning("logging.warning") 
    logging.error("logging.error")
    logging.exception("logging.exception") 
    logging.critical("logging.critical") 
 
    return Response("cloud_function_python", status=200)