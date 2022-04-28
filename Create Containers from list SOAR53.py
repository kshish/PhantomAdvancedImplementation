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

    phantom.custom_function(custom_function="PAI/L5_CF_Retrieve_List_SOAR53", parameters=parameters, name="l5_cf_retrieve_list_soar53_2", callback=l5_cf_retrieve_list_soar53_2_callback)

    return


def l5_cf_retrieve_list_soar53_2_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_cf_retrieve_list_soar53_2_callback() called")

    
    debug_4(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    filter_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def l5_cf_create_containers_from_list_py3_soar53_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_cf_create_containers_from_list_py3_soar53_3() called")

    filtered_cf_result_0 = phantom.collect2(container=container, datapath=["filtered-data:filter_2:condition_1:l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents"])

    filtered_cf_result_0_data_listcontents = [item[0] for item in filtered_cf_result_0]

    parameters = []

    parameters.append({
        "container_label": "possiblemalware",
        "to_be_containerized": filtered_cf_result_0_data_listcontents,
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


def debug_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_4() called")

    l5_cf_retrieve_list_soar53_2__result = phantom.collect2(container=container, datapath=["l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents","l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents[0]"])
    l5_cf_retrieve_list_soar53_2_data = phantom.collect2(container=container, datapath=["l5_cf_retrieve_list_soar53_2:custom_function_result.data.*.priority"])
    l5_cf_retrieve_list_soar53_2_data_listcontents = phantom.collect2(container=container, datapath=["l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents.*.priority","l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents.*"])

    l5_cf_retrieve_list_soar53_2_data_listcontents = [item[0] for item in l5_cf_retrieve_list_soar53_2__result]
    l5_cf_retrieve_list_soar53_2_data_listcontents_0_ = [item[1] for item in l5_cf_retrieve_list_soar53_2__result]
    l5_cf_retrieve_list_soar53_2_data___priority = [item[0] for item in l5_cf_retrieve_list_soar53_2_data]
    l5_cf_retrieve_list_soar53_2_data_listcontents___priority = [item[0] for item in l5_cf_retrieve_list_soar53_2_data_listcontents]
    l5_cf_retrieve_list_soar53_2_data_listcontents__ = [item[1] for item in l5_cf_retrieve_list_soar53_2_data_listcontents]

    parameters = []

    parameters.append({
        "input_1": l5_cf_retrieve_list_soar53_2_data_listcontents,
        "input_2": l5_cf_retrieve_list_soar53_2_data___priority,
        "input_3": l5_cf_retrieve_list_soar53_2_data_listcontents___priority,
        "input_4": l5_cf_retrieve_list_soar53_2_data_listcontents__,
        "input_5": l5_cf_retrieve_list_soar53_2_data_listcontents_0_,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_4")

    return


def filter_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_2() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["high", "in", "l5_cf_retrieve_list_soar53_2:custom_function_result.data.listContents.priority"]
        ],
        name="filter_2:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        l5_cf_create_containers_from_list_py3_soar53_3(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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