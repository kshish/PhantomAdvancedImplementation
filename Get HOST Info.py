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
    formatted_data_1 = phantom.get_format_data(name='format_1__as_list')

    parameters = []
    
    # build parameters list for 'run_query_1' call
    for formatted_part_1 in formatted_data_1:
        parameters.append({
            'query': formatted_part_1,
            'display': "",
        })

    phantom.act(action="run query", parameters=parameters, assets=['esa100'], callback=format_2, name="run_query_1")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """%%
 | savedsearch myHostInfo myhost=\"{0}\"
%%"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destinationHostName",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    run_query_1(container=container)

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "format_2:formatted_data",
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

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_2() called')
    
    template = """%%
CPU: {0} wait time percent: {1}
%%"""

    # parameter list for template variable replacement
    parameters = [
        "run_query_1:action_result.data.*.cpu",
        "run_query_1:action_result.data.*.PercentWaitTime",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    post_data_1(container=container)

    return

def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('post_data_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'post_data_1' call
    formatted_data_1 = phantom.get_format_data(name='format_2__as_list')

    parameters = []
    
    # build parameters list for 'post_data_1' call
    for formatted_part_1 in formatted_data_1:
        parameters.append({
            'data': formatted_part_1,
            'host': "chris",
            'index': "from_phantom",
            'source': "Phantom",
            'source_type': "mylist",
        })

    phantom.act(action="post data", parameters=parameters, assets=['esa100'], callback=prompt_1, name="post_data_1")

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