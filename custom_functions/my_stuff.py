def my_stuff(my_stuff_input=None, my_stuff_other=None, **kwargs):
    """
    this is a comment
    
    Args:
        my_stuff_input (CEF type: ip): Provide a CEF field  that has an ip address or list in it
        my_stuff_other
    
    Returns a JSON-serializable object that implements the configured data paths:
        my_stuff_output (CEF type: hostname)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputs = '{"my_stuff_output" : "ACME-0001"}'
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
