"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'cf_community_list_merge_1' block
    cf_community_list_merge_1(container=container)

    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_query_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'run_query_1' call
    formatted_data_1 = phantom.get_format_data(name='format_1__as_list')

    parameters = []
    
    # build parameters list for 'run_query_1' call
    for formatted_part_1 in formatted_data_1:
        parameters.append({
            'query': formatted_part_1,
            'command': "search",
            'display': "",
            'parse_only': "",
        })

    phantom.act(action="run query", parameters=parameters, assets=['esaabb100'], callback=run_query_1_callback, name="run_query_1")

    return

def run_query_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None):
    phantom.debug('run_query_1_callback() called')
    
    format_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
    format_comment(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """| savedsearch find_peers server={0}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_community_list_merge_1:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    run_query_1(container=container)

    return

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_2() called')
    
    template = """peer {2}

%%
*_communicated {1} with {0} with severity {3}_*
%%"""

    # parameter list for template variable replacement
    parameters = [
        "run_query_1:action_result.data.*.peer",
        "run_query_1:action_result.data.*.count",
        "artifact:*.cef.destinationHostName",
        "run_query_1:action_result.data.*.priority",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    prompt_1(container=container)

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "format_2:formatted_data.*",
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

def update_event_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_event_1() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'update_event_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.eventId', 'artifact:*.id'])
    formatted_data_1 = phantom.get_format_data(name='format_comment')

    parameters = []
    
    # build parameters list for 'update_event_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'owner': "",
                'status': "in progress",
                'comment': formatted_data_1,
                'urgency': "",
                'event_ids': container_item[0],
                'integer_status': "",
                'wait_for_confirmation': "",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act(action="update event", parameters=parameters, assets=['esaabb100'], name="update_event_1")

    return

def format_comment(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_comment() called')
    
    template = """There were {0} number of peers this server {1}communicated"""

    # parameter list for template variable replacement
    parameters = [
        "run_query_1:action_result.summary.total_events",
        "artifact:*.cef.destination",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_comment")

    update_event_1(container=container)

    return

def cf_community_list_merge_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_community_list_merge_1() called')
    
    container_data_0 = phantom.collect2(container=container, datapath=['artifact:*.cef.destinationAddress', 'artifact:*.cef.destinationHostName', 'artifact:*.id'])

    parameters = []

    container_data_0_0 = [item[0] for item in container_data_0]
    container_data_0_1 = [item[1] for item in container_data_0]

    parameters.append({
        'input_1': container_data_0_0,
        'input_2': container_data_0_1,
        'input_3': None,
        'input_4': None,
        'input_5': None,
        'input_6': None,
        'input_7': None,
        'input_8': None,
        'input_9': None,
        'input_10': None,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "community/list_merge", returns the custom_function_run_id
    phantom.custom_function(custom_function='community/list_merge', parameters=parameters, name='cf_community_list_merge_1', callback=format_1)

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