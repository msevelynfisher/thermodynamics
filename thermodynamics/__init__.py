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


class FunctionalIndependenceError(Exception):
    """
    Raised when root-finding a function that is independent of the parameter.
    """
    def __init__(self):
        super(FunctionalIndependenceError, self).__init__(
            "function insensitive to independent variable during root-finding"
        )

class ConvergenceError(Exception):
    """Raised when the maximum number of iterations is exceeded."""
    def __init__(self, iters):
        super(ConvergenceError, self).__init__(
            "failed to converge within " + str(iters) + 'iterations'
        )

def seek(y, func, P, T, substance, eos = IDEAL_GAS, tol = 1e-6):
    """
    Finds either the temperature or pressure given the value of another
    state variable. Pass None as the value of the unknown parameter.
    """
    if P is None:
        f = lambda x: func(x, T, substance, eos) - y
    else:
        f = lambda x: func(P, x, substance, eos) - y
    x0 = 1
    f0 = f(x0)
    x1 = 2
    f1 = f(x1)
    
    if f0 == f1:
        raise FunctionalIndependenceError()
    
    i = 0
    imax = 1000
    while abs((x1 - x0)/x0) > tol and i < imax:
        x2 = x0 - (x1 -  x0) / (f1 - f0) * f0
        f2 = f(x2)
        x0, f0 = x1, f1
        x1, f1 = x2, f2
    if i == imax:
        raise ConvergenceError(imax)
    
    return x1