"""
Contains the ideal gas equation of state.
"""


import math
from ..constant import *
from ..parameter import *


class __IDEAL_GAS:
    
    def Vmol_PT(self, P, T, substance):
        """Returns molar volume."""
        return GAS_CONSTANT * T / P
    
    def Umol_PT(self, P, T, substance):
        """Returns molar internal energy."""
        g = get_parameter(substance, 'specific-heat-ratio')
        cvmol = GAS_CONSTANT / (g - 1)
        return cvmol * T
    
    def Hmol_PT(self, P, T, substance):
        """Returns molar enthalpy."""
        g = get_parameter(substance, 'specific-heat-ratio')
        cpmol = g / (g - 1) * GAS_CONSTANT
        return cpmol * T
    
    def Smol_PT(self, P, T, substance):
        """Returns molar entropy relative to (1 Pa, 1 K)."""
        g = get_parameter(substance, 'specific-heat-ratio')
        cv = GAS_CONSTANT / (g - 1)
        Vmol = self.Vmol_PT(P, T, substance)
        return GAS_CONSTANT * math.log(Vmol) - cv * math.log(T)


IDEAL_GAS = __IDEAL_GAS()
