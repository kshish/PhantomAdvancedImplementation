"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'splunk_query' block
    splunk_query(container=container)

    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_query_1() called')

    # collect data for 'run_query_1' call
    formatted_data_1 = phantom.get_format_data(name='splunk_query')

    parameters = []
    
    # build parameters list for 'run_query_1' call
    parameters.append({
        'query': formatted_data_1,
        'command': "",
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['esa100'], callback=Get_Query_Results, name="run_query_1")

    return

def splunk_query(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('splunk_query() called')
    
    template = """| savedsearch find_peers server={0}"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destination",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="splunk_query")

    run_query_1(container=container)

    return

def Get_Query_Results(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Get_Query_Results() called')
    
    action_results_data_0 = phantom.collect2(container=container, datapath=['run_query_1:action_result.data.*.peer', 'run_query_1:action_result.data.*.count', 'run_query_1:action_result.data.*.priority', 'run_query_1:action_result.parameter.context.artifact_id'], action_results=results )
    container_property_0 = [
        [
            container.get("id"),
        ],
    ]

    parameters = []

    action_results_data_0_0 = [item[0] for item in action_results_data_0]
    action_results_data_0_1 = [item[1] for item in action_results_data_0]
    action_results_data_0_2 = [item[2] for item in action_results_data_0]

    for item0 in container_property_0:
        parameters.append({
            'peer': action_results_data_0_0,
            'count': action_results_data_0_1,
            'priority': action_results_data_0_2,
            'container': item0[0],
        })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "PAI/L5_CF_Get_Query_Results_py3", returns the custom_function_run_id
    phantom.custom_function(custom_function='PAI/L5_CF_Get_Query_Results_py3', parameters=parameters, name='Get_Query_Results', callback=Filter_List)

    return

def Filter_List(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Filter_List() called')
    
    custom_function_result_0 = phantom.collect2(container=container, datapath=['Get_Query_Results:custom_function_result.data.results_list'], action_results=results )
    literal_values_0 = [
        [
            "critical, high",
        ],
    ]

    parameters = []

    custom_function_result_0_0 = [item[0] for item in custom_function_result_0]
    literal_values_0_0 = [item[0] for item in literal_values_0]

    parameters.append({
        'list_obj': custom_function_result_0_0,
        'filter_items': literal_values_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "PAI/L5_CF_Filter_List_py3", returns the custom_function_run_id
    phantom.custom_function(custom_function='PAI/L5_CF_Filter_List_py3', parameters=parameters, name='Filter_List', callback=Create_Containers_From_List)

    return

def Create_Containers_From_List(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Create_Containers_From_List() called')
    
    custom_function_result_0 = phantom.collect2(container=container, datapath=['Filter_List:custom_function_result.data.filtered_list'], action_results=results )
    literal_values_0 = [
        [
            "vipeer",
        ],
    ]

    parameters = []

    custom_function_result_0_0 = [item[0] for item in custom_function_result_0]

    for item0 in literal_values_0:
        parameters.append({
            'container_label': item0[0],
            'to_be_containerized': custom_function_result_0_0,
        })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "PAI/L5_CF_Create_Containers_From_List_py3", returns the custom_function_run_id
    phantom.custom_function(custom_function='PAI/L5_CF_Create_Containers_From_List_py3', parameters=parameters, name='Create_Containers_From_List')

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