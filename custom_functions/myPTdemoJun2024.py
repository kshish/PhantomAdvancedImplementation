def myPTdemoJun2024(someIp=None, someString=None, **kwargs):
    """
    Here's details.... blah blah....
    
    Args:
        someIp (CEF type: ip): Map some IP values into this variable. This function will blah blah to this input var
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): This output var has the same value as input IP var
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    myIp=someIp
    myString=someString
    
    outputs = {"outputIP": myIp, "outputString": someString}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
