def myfun(someip=None, myhost=None, **kwargs):
    """
    comments in code
    
    Args:
        someip (CEF type: ip): This function will do something with an ip
        myhost (CEF type: hostname)
    
    Returns a JSON-serializable object that implements the configured data paths:
        ipresult (CEF type: hash)
        another
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {"ipresult": someip, "another": "someval" }
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
