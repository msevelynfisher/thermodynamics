"""
Contains unit conversions. Multiplying a number by its unit converts it to SI.
Dividing a number by a unit converts from SI to that unit.
"""

# Pressure

Pa = 1
kPa = 1e3
MPa = 1e6
GPa = 1e9

# Temperature

class __C:
    def __rmul__(self, other):
        return other + 273.15
    def __rtruediv__(self, other):
        return other - 273.15

C = __C()
K = 1

# Energy

J = 1
kJ = 1e3
MJ = 1e6
GJ = 1e9

# Power

W = 1
kW = 1e3
MW = 1e6
GW = 1e9

# Time

s = 1
mn = 60
hr = 60 * mn
