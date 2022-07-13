def sampleCF(someString=None, someIp=None, **kwargs):
    """
    this is a demo
    
    Args:
        someString: Provide some string
        someIp (CEF type: ip)
    
    Returns a JSON-serializable object that implements the configured data paths:
        myoutIp (CEF type: ip)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}

    # Write your custom code here...
    myvar = ""   
    myvar = someIp
    outputs = {"myoutIp": myvar}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
