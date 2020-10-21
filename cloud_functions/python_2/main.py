import json

from flask import Response


def cloud_function_python(request):
    PROJECT = 'gcp-log-examples'

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

    return Response("cloud_function_python", status=200)