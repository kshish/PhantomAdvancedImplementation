"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'parse_list' block
    parse_list(container=container)

    return

def parse_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("parse_list() called")

    playbook_input_list_name = phantom.collect2(container=container, datapath=["playbook_input:list_name"])

    playbook_input_list_name_values = [item[0] for item in playbook_input_list_name]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug("parse_list input = {}".format(playbook_input_list_name))
    sta, msg, read_list__peer_list = phantom.get_list(list_name=playbook_input_list_name_values[0] )
    for server in read_list__peer_list:
        if server[2] in ["critical","high"]:
            phantom.debug("%s is priority %s" % (server[0],server[2]))
            status, message, cid = phantom.create_container(name="Possible server malware", label="events")
            #phantom.set_severity(cid, "high")
            phantom.add_artifact(container=cid, raw_data={}, cef_data={"sourceAddress":server[0]}, label="infection", name="Possibly infected host", severity="high", artifact_type="host")
    

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