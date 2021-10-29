"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'string_to_uppercase_1' block
    string_to_uppercase_1(container=container)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_1() called")

    template = """find_peers server=\"{0}\"\n"""

    # parameter list for template variable replacement
    parameters = [
        "string_to_uppercase_1:custom_function_result.data.uppercase_string"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    run_query_1(container=container)

    return


def string_to_uppercase_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("string_to_uppercase_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destination","artifact:*.id"])

    parameters = []

    # build parameters list for 'string_to_uppercase_1' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "input_string": container_artifact_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/string_to_uppercase", parameters=parameters, name="string_to_uppercase_1", callback=format_1)

    return


def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("run_query_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_1 = phantom.get_format_data(name="format_1")

    parameters = []

    if format_1 is not None:
        parameters.append({
            "query": format_1,
            "command": "savedsearch",
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="run_query_1", assets=["esabwrev"], callback=run_query_1_callback)

    return


def run_query_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("run_query_1_callback() called")

    
    prompt_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    l5_cf_get_query_results_py3_4(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = "admin"
    message = """here's the list\n\n{0} priority: {1} count:{2}"""

    # parameter list for template variable replacement
    parameters = [
        "run_query_1:action_result.data.*.peer",
        "run_query_1:action_result.data.*.priority",
        "run_query_1:action_result.data.*.count"
    ]

    # responses
    response_types = [
        {
            "prompt": "Update event?",
            "options": {
                "type": "list",
                "choices": [
                    "Yes",
                    "No"
                ],
            },
        },
        {
            "prompt": "comment:",
            "options": {
                "type": "message",
            },
        }
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, response_types=response_types, callback=decision_1)

    return


def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["prompt_1:action_result.summary.responses.0", "==", "Yes"]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        update_event_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


def update_event_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_event_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    prompt_1_result_data = phantom.collect2(container=container, datapath=["prompt_1:action_result.summary.responses.1","prompt_1:action_result.parameter.context.artifact_id"], action_results=results)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.notable_id","artifact:*.id"])

    parameters = []

    # build parameters list for 'update_event_1' call
    for prompt_1_result_item in prompt_1_result_data:
        for container_artifact_item in container_artifact_data:
            if container_artifact_item[0] is not None:
                parameters.append({
                    "status": "in progress",
                    "comment": prompt_1_result_item[0],
                    "urgency": "critical",
                    "event_ids": container_artifact_item[0],
                    "context": {'artifact_id': container_artifact_item[1]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update event", parameters=parameters, name="update_event_1", assets=["esabwrev"])

    return


def playbook_create_events_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_create_events_1() called")

    l5_cf_get_query_results_py3_4__result = phantom.collect2(container=container, datapath=["l5_cf_get_query_results_py3_4:custom_function_result.data.results_list"])

    l5_cf_get_query_results_py3_4_data_results_list = [item[0] for item in l5_cf_get_query_results_py3_4__result]

    inputs = {
        "mylist": l5_cf_get_query_results_py3_4_data_results_list,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "chris/create events", returns the playbook_run_id
    playbook_run_id = phantom.playbook("chris/create events", container=container, inputs=inputs)

    return


def l5_cf_get_query_results_py3_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_cf_get_query_results_py3_4() called")

    id_value = container.get("id", None)
    run_query_1_result_data = phantom.collect2(container=container, datapath=["run_query_1:action_result.data.*.peer","run_query_1:action_result.data.*.priority","run_query_1:action_result.data.*.count","run_query_1:action_result.parameter.context.artifact_id"], action_results=results)

    run_query_1_result_item_0 = [item[0] for item in run_query_1_result_data]
    run_query_1_result_item_1 = [item[1] for item in run_query_1_result_data]
    run_query_1_result_item_2 = [item[2] for item in run_query_1_result_data]

    parameters = []

    parameters.append({
        "peer": run_query_1_result_item_0,
        "priority": run_query_1_result_item_1,
        "count": run_query_1_result_item_2,
        "container": id_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/L5_CF_Get_Query_Results_py3", parameters=parameters, name="l5_cf_get_query_results_py3_4", callback=playbook_create_events_1)

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