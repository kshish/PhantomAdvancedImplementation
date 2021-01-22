"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'format_query' block
    format_query(container=container)

    # call 'block_ip_1' block
    block_ip_1(container=container)

    return

def run_my_query(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_my_query() called')

    # collect data for 'run_my_query' call
    formatted_data_1 = phantom.get_format_data(name='format_query')

    parameters = []
    
    # build parameters list for 'run_my_query' call
    parameters.append({
        'query': formatted_data_1,
        'command': "search",
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['esa100'], callback=run_my_query_callback, name="run_my_query")

    return

def run_my_query_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('run_my_query_callback() called')
    
    format_list(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
    format_3(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def format_query(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_query() called')
    
    template = """earliest=-60m index=main {0} NOT host={0} | stats count  by dest"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destination",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_query")

    run_my_query(container=container)

    return

def format_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_list() called')
    
    template = """%%
destination {0} communicated {1} times
%%"""

    # parameter list for template variable replacement
    parameters = [
        "run_my_query:action_result.data.*.dest",
        "run_my_query:action_result.data.*.count",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_list")

    prompt_1(container=container)

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "format_list:formatted_data.*",
    ]

    #responses:
    response_types = [
        {
            "prompt": "",
            "options": {
                "type": "message",
            },
        },
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, response_types=response_types)

    return

def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_3() called')
    
    template = """There were {0} servers communicated with"""

    # parameter list for template variable replacement
    parameters = [
        "run_my_query:action_result.summary.total_events",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    add_comment_set_label_set_sensitivity_1(container=container)

    return

def add_comment_set_label_set_sensitivity_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_set_label_set_sensitivity_1() called')

    formatted_data_1 = phantom.get_format_data(name='format_3')

    phantom.comment(container=container, comment=formatted_data_1)

    phantom.set_label(container=container, label="test")

    phantom.set_sensitivity(container=container, sensitivity="amber")

    return

def block_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('block_ip_1() called')

    parameters = []

    phantom.act(action="block ip", parameters=parameters, name="block_ip_1")

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