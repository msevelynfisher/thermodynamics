"""
Utilities for performing calculations pertaining to thermodynamics.
"""


from .constant import *
from .eos import IDEAL_GAS
from .parameter import *

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


def Vmol_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns molar volume."""
    return eos.Vmol_PT(P, T, substance)

def Umol_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns molar internal energy."""
    return eos.Umol_PT(P, T, substance)

def Hmol_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns molar enthalpy."""
    return eos.Hmol_PT(P, T, substance)

def Smol_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns molar entropy relative to (1 Pa, 1 K)."""
    return eos.Smol_PT(P, T, substance)


def V_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns specific volume."""
    mw = get_parameter(substance, 'molecular-weight')
    Vmol = eos.Vmol_PT(P, T, substance)
    return Vmol / mw

def U_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns specific internal energy."""
    mw = get_parameter(substance, 'molecular-weight')
    Umol = eos.Umol_PT(P, T, substance)
    return Vmol / mw

def H_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns specific enthalpy."""
    mw = get_parameter(substance, 'molecular-weight')
    Hmol = eos.Hmol_PT(P, T, substance)
    return Vmol / mw

def S_PT(P, T, substance, eos = IDEAL_GAS):
    """Returns specific entropy relative to (1 Pa, 1 K)."""
    mw = get_parameter(substance, 'molecular-weight')
    Smol = eos.Smol_PT(P, T, substance)
    return Vmol / mw
