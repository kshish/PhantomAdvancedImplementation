"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'l5_cf_retrieve_list_soar53_2' block
    l5_cf_retrieve_list_soar53_2(container=container)

    return

def l5_cf_retrieve_list_soar53_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_cf_retrieve_list_soar53_2() called")

    playbook_input_list_name = phantom.collect2(container=container, datapath=["playbook_input:list_name"])

    parameters = []

    # build parameters list for 'l5_cf_retrieve_list_soar53_2' call
    for playbook_input_list_name_item in playbook_input_list_name:
        parameters.append({
            "listName": playbook_input_list_name_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="PAI/L5_CF_Retrieve_List_SOAR53", parameters=parameters, name="l5_cf_retrieve_list_soar53_2", callback=l5_cf_create_containers_from_list_py3_soar53_3)

    return


def l5_cf_create_containers_from_list_py3_soar53_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_cf_create_containers_from_list_py3_soar53_3() called")

    l5_cf_retrieve_list_soar53_2__result = phantom.collect2(container=container, datapath=["l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents"])

    l5_cf_retrieve_list_soar53_2_data_listcontents = [item[0] for item in l5_cf_retrieve_list_soar53_2__result]

    parameters = []

    parameters.append({
        "container_label": "possibleMalware",
        "to_be_containerized": l5_cf_retrieve_list_soar53_2_data_listcontents,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="PAI/L5_CF_Create_Containers_From_List_py3_SOAR53", parameters=parameters, name="l5_cf_create_containers_from_list_py3_soar53_3")

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