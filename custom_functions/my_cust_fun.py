def my_cust_fun(my_var1=None, my_ip=None, **kwargs):
    """
    blah blah
    
    Args:
        my_var1: map in something that my function can handle
        my_ip (CEF type: ip): more meaningful help here
    
    Returns a JSON-serializable object that implements the configured data paths:
        my_outvar1
        my_ip_out (CEF type: ip)
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    my_outvar1=my_var1
    my_ip_out=my_ip
    outputs = {"my_outvar1":my_outvar1, "my_ip_out":my_ip}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
