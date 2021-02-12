def my_phabb(my_ip=None, **kwargs):
    """
    This is a dejmo of a custoj function
    
    Args:
        my_ip (CEF type: ip): chris wuz here
    
    Returns a JSON-serializable object that implements the configured data paths:
        hostName (CEF type: hostname): some host name value 
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    anyvar="chris.uz.here.com"
    outputs = {"hostName": anyvar}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
