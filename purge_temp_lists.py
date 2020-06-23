"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'get_temp_lists' block
    get_temp_lists(container=container)

    return

def get_temp_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_temp_lists() called')

    # collect data for 'get_temp_lists' call

    parameters = []
    
    # build parameters list for 'get_temp_lists' call
    parameters.append({
        'location': "decided_list?_filter_name__startswith=\"temp\"",
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act("get data", parameters=parameters, assets=['rest'], callback=remove_temp_lists, name="get_temp_lists")

    return

def remove_temp_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('remove_temp_lists() called')
    results_data_1 = phantom.collect2(container=container, datapath=['get_temp_lists:action_result.data.*.response_body'], action_results=results)
    results_item_1_0 = [item[0] for item in results_data_1]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(results_item_1_0)
    for item in results_item_1_0[0]['data']:
        phantom.remove_list(item['name'])

    ################################################################################
    ## Custom Code End
    ################################################################################

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return