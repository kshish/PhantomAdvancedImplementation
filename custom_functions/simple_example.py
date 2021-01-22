def simple_example(myip=None, myhost=None, mysomething=None, **kwargs):
    """
    demo
    
    Args:
        myip (CEF type: ip): better help text
        myhost (CEF type: hostname)
        mysomething
    
    Returns a JSON-serializable object that implements the configured data paths:
        myIpOut (CEF type: ip)
        myHostOut (CEF type: hostname)
        mySomethingOut
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    myIpOut=myip
    myHostOut=myhost
    mySomethingOut=mysomething

    outputs = {"myIpOut": myIpOut, "myHostOut": myHostOut, "mySomethingOut": mySomethingOut }
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
