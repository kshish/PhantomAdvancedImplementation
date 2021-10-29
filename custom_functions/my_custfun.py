def my_custfun(myIP=None, userName=None, **kwargs):
    """
    demo
    
    Args:
        myIP (CEF type: ip): map a valid IP address into here
        userName (CEF type: user name)
    
    Returns a JSON-serializable object that implements the configured data paths:
        ipAndUserInfo (CEF type: hash): calculated hash
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {"ipAndHash":"a78bc87c"}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
