def myfundemo(myip=None, someHost=None, **kwargs):
    """
    Args:
        myip (CEF type: ip): this is help text
        someHost (CEF type: hostname)
    
    Returns a JSON-serializable object that implements the configured data paths:
        myvalidatedIP (CEF type: ip)
        myvalidatedHost (CEF type: hostname)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {"myvalidatedIP" : myip, "myvalidatedHost" : someHost}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
