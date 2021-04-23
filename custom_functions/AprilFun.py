def AprilFun(some_ip=None, is_ipv6=None, **kwargs):
    """
    demo
    
    Args:
        some_ip (CEF type: ip): Map any fields that contain an ip
        is_ipv6: duh!
    
    Returns a JSON-serializable object that implements the configured data paths:
        is_valid_ipv6
        valid_ip (CEF type: ip)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    outputs = '{"is_valid_ipv6":"true", "valid_ip":"111.22.33.44"}'
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
