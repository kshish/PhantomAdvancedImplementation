def L5_CF_Filter_List_py3(filter_items=None, list_obj=None, **kwargs):
    """
    Filtering nested lists. Makes the code cleaner.
    
    Args:
        filter_items: A comma seperated list of values for use in filtering the list of lists
        list_obj: A list of lists, because of the way Phantom handles components, if this is returned from another custom function, it will be triple nested.  For example:
            
            [
                [
                   ['a', 'b'],
                   ['c', 'd'],
                   ['e', 'f']
                ]
            ]
            
            As such we will take the first list element, which happens to be the nested list we are looking for but if this doesn't work for you, please feel free to edit this up to your needs. :)
    
    Returns a JSON-serializable object that implements the configured data paths:
        filtered_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    filtered_list = []
    
    # The filter terms should 
    temp_filter_items = filter_items[0].split(',')
    temp_filter_items = [obj.strip() for obj in temp_filter_items]
    
    # Iterate through and filter the nested list based on the filter items
    for term in temp_filter_items:
        temp_list = [obj for obj in list_obj[0] if term.strip() in obj]
        filtered_list.extend(temp_list)
    
    outputs = {'filtered_list': filtered_list}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
