"""
Demonstrates using the container data dictionary to persist data. Alternative to creating artifacts (UI visible) or save_object(potential key name conflicts with other playbooks.)
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'write_container_data' block
    write_container_data(container=container)

    return

"""
save string to container data

"""
def write_container_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('write_container_data() called')
    input_parameter_0 = "my_data_2"
    input_parameter_1 = "More Stuff"

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    #input_parameter_0 is the key
    #input_parameter_1 is the value
    data = phantom.get_container(container['id'])['data']
    data.update({input_parameter_0:input_parameter_1})
    phantom.update(container, {'data':data} )

    ################################################################################
    ## Custom Code End
    ################################################################################
    get_container_data(container=container)

    return

def get_container_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_container_data() called')
    input_parameter_0 = "my_data_2"

    get_container_data__container_data = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    get_container_data__container_data = phantom.get_container(container['id'])['data'][input_parameter_0]
    
    phantom.debug('=========================')
    phantom.debug(get_container_data__container_data)
    phantom.debug('=========================')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='get_container_data:container_data', value=json.dumps(get_container_data__container_data))

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