"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'format_1' block
    format_1(container=container)

    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_query_1() called')

    # collect data for 'run_query_1' call
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'run_query_1' call
    parameters.append({
        'query': formatted_data_1,
        'command': "search",
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['esaabb100'], name="run_query_1")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """earliest=-2h \"{0}\" NOT host=\"{0}\"        
| stats count, first(dest_priority) as priority first(severity) as severity by dest, src
        | where src=\"{0}\" OR dest=\"{0}\"
        | eval peer = if(dest = \"{0}\", src, dest)
        | eval priority = coalesce(priority, severity)
        | sort - count
        | table peer priority count"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destinationHostName",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    run_query_1(container=container)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return