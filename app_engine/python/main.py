import logging
import sys 
import json
import google.cloud.logging
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def app_engine_python():
    sys.stderr.write("log to stderr")
    sys.stdout.write("log to stdout")

    print("log via print")

    logging.debug("logging.debug")
    logging.info("logging.info")
    logging.warning("logging.warning") 
    logging.error("logging.error")
    logging.exception("logging.exception") 
    logging.critical("logging.critical") 


    # Uncomment and populate this variable in your code:
    PROJECT = 'gcp-log-examples'

    # Build structured log messages as an object.
    global_log_fields = {}

    # Add log correlation to nest all log messages
    # beneath request log in Log Viewer.
    trace_header = request.headers.get('X-Cloud-Trace-Context')

    if trace_header and PROJECT:
        trace = trace_header.split('/')
        global_log_fields['logging.googleapis.com/trace'] = (
        f"projects/{PROJECT}/traces/{trace[0]}")


    entry = dict(severity='DEFAULT',
             message='The log entry has no assigned severity level.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='DEBUG',
             message='Debug or trace information.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='INFO',
             message='Routine information, such as ongoing status or performance.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='NOTICE',
             message='Normal but significant events, such as start up, shut down, or a configuration change.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='WARNING',
             message='Warning events might cause problems.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='EMERGENCY',
             message='Error events are likely to cause problems.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='CRITICAL',
             message='Critical events cause more severe problems or outages.',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry))
    entry = dict(severity='ALERT',
             message='A person must take an action immediately',
             component='arbitrary-property',
             **global_log_fields)

    print(json.dumps(entry)) 
    entry = dict(severity='EMERGENCY',
             message='One or more systems are unusable.',
             component='arbitrary-property',
             **global_log_fields)
    print(json.dumps(entry))

    client = google.cloud.logging.Client()
    client.get_default_handler()
    client.setup_logging()

    logging.debug("logging.debug client")
    logging.info("logging.info client")
    logging.warning("logging.warning client") 
    logging.error("logging.error client")
    logging.exception("logging.exception client") 
    logging.critical("logging.critical client") 
    return Response("", status=201)
