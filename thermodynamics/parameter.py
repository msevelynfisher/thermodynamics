"""
For extracting parameters from a dictionary of substance properties.
"""

class MissingParameterError(Exception):
    """Raised when a parameter of a substance is required but not supplied."""
    def __init__(self, substance, parameter):
        self.substance = substance
        self.parameter = parameter
        message = "'" + parameter + "' is a required parameter"
        super(MissingParameterError, self).__init__(message)

def get_parameter(substance, parameter):
    if parameter not in substance:
        raise MissingParameterError(substance, parameter)
    else:
        return substance[parameter]