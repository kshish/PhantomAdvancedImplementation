def L5_CF_Get_Query_Results(peer=None, priority=None, count=None, container=None, **kwargs):
    """
    Args:
        peer (CEF type: *)
        priority (CEF type: *)
        count (CEF type: *)
        container (CEF type: phantom container id)
    
    Returns a JSON-serializable object that implements the configured data paths:
        results_list (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import re
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(container)
    phantom.debug(type(container))
    list_name = "temp_peer_list_%s" % container
    
    # You need the container object in order to update it.
    update_container = phantom.get_container(container)
    
    # Get the data node of the container
    data = phantom.get_container(container)['data']
    data.update({"peer_list":list_name})
    phantom.update(update_container, {'data':data} )
    phantom.remove_list(list_name)
    
    for i in range(0,len(peer)):
        phantom.add_list(list_name, [peer[i],priority[i],count[i]])
    
    # The actual list is in slot 3 of the tuple returned by phantom.get_list()
    results_list = phantom.get_list(list_name)[2]
    phantom.debug(results_list)
    outputs = {'results_list': results_list}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
