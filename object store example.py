"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'I_have_some_data' block
    I_have_some_data(container=container)

    return

def save_object_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('save_object_data() called')
    input_parameter_0 = "my_key"
    I_have_some_data__my_data = json.loads(phantom.get_run_data(key='I_have_some_data:my_data'))

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.save_object(key=input_parameter_0, value={'value': "'" + I_have_some_data__my_data + "'"}, auto_delete=True, container_id=container['id'])

    ################################################################################
    ## Custom Code End
    ################################################################################
    get_object_data(container=container)

    return

def get_object_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_object_data() called')
    input_parameter_0 = "my_key"

    get_object_data__value = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    data = phantom.get_object(key=input_parameter_0, container_id=container['id'])

    get_object_data__value = data[0]['value']['value']

    # clear object db
    phantom.clear_object(key=input_parameter_0,container_id=container['id'])

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='get_object_data:value', value=json.dumps(get_object_data__value))
    I_want_the_data(container=container)

    return

def I_have_some_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('I_have_some_data() called')
    input_parameter_0 = ""

    I_have_some_data__my_data = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    I_have_some_data__my_data = "hello world"

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='I_have_some_data:my_data', value=json.dumps(I_have_some_data__my_data))
    save_object_data(container=container)

    return

def I_want_the_data(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('I_want_the_data() called')
    get_object_data__value = json.loads(phantom.get_run_data(key='get_object_data:value'))

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug("========================================")
    phantom.debug("I got this: %s" % get_object_data__value)
    phantom.debug("========================================")

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