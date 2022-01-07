def MyCustomJanuarySOAR50(anIp=None, somevalue=None, **kwargs):
    """
    this is a demo
    
    Args:
        anIp (CEF type: ip): Please map an ip value into this input
        somevalue
    
    Returns a JSON-serializable object that implements the configured data paths:
        myoutIP (CEF type: ip)
        someValue
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {"myoutIP" : anIp, "someValue" : somevalue}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
