from ansible.errors import AnsibleFilterError

def invalid(value):
    raise AnsibleFilterError('Invalid value: %s' % value)

def is_bool(value):
    if not isinstance(value, bool):
        invalid(value)
    return value

def is_int(value):
    if not isinstance(value, int):
        invalid(value)
    return value

def is_allowed(value, array):
    if not value in array:
        invalid(value)
    return value

def is_non_negative(value):
    if not value >= 0:
        invalid(value)
    return value

def is_positive(value):
    if not value > 0:
        invalid(value)
    return value

def is_zmq_endpoint(value):
    if not isinstance(value, str):
        invalid(value)
    return value

def to_bool(value):
    return 1 if is_bool(value) else 0

class FilterModule:
    def filters(self):
        return {
                'is_bool':         is_bool,
                'is_int':          is_int,
                'is_allowed':      is_allowed,
                'is_non_negative': is_non_negative,
                'is_positive':     is_positive,
                'is_zmq_endpoint': is_zmq_endpoint,
                'to_bool':         to_bool,
        }
