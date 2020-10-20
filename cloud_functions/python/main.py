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

    return Response("cloud_function_python", status=200)