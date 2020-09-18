def ChrisFun(myIpVar=None, my=None, **kwargs):
    """
    Demo
    
    Args:
        myIpVar (CEF type: ip): more helpful text here
        my: blah lbah
    
    Returns a JSON-serializable object that implements the configured data paths:
        myOutput (CEF type: ip): myOutput description
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
