"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_temp_custom_lists' block
    get_temp_custom_lists(container=container)

    return

def get_temp_custom_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_temp_custom_lists() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "location": "/decided_list?_filter_name__startswith=\"temp\"",
        "verify_certificate": False,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_temp_custom_lists", assets=["http"], callback=delete_lists)

    return


def delete_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_lists() called")

    get_temp_custom_lists_result_data = phantom.collect2(container=container, datapath=["get_temp_custom_lists:action_result.data.*.parsed_response_body"], action_results=results)

    get_temp_custom_lists_result_item_0 = [item[0] for item in get_temp_custom_lists_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    # phantom.debug(get_temp_custom_lists_result_data)
    
    for item in get_temp_custom_lists_result_item_0[0]['data']:
        # phantom.debug(item['name'])
        phantom.remove_list(item['name'])

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return