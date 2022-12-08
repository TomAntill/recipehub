from ..validation import httprequestexceptions

def guard_is_element_string(element):
    for e in element:
        if e is not str:
            return httprequestexceptions.error_message_guard_is_string

def guard_is_list_empty(list):
    if list.len(0):
        return httprequestexceptions.error_message_list_is_empty

