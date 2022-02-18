def someDemo(myIp=None, myHostname=None, myString=None, **kwargs):
    """
    Good description goes here
    
    Args:
        myIp (CEF type: ip): Enter or map an IP address
        myHostname (CEF type: host name): map a hostname value
        myString: map any value
    
    Returns a JSON-serializable object that implements the configured data paths:
        myoutIP (CEF type: ip): Some IP output from cf
        someValue: any data type
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    outputs= {"myoutIP" : myIp, "someValue" : "Chris wuz here"}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
