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

K = 1
class __C:
    def __rmul__(self, other):
        return other + 273.15 * K
    def __rtruediv__(self, other):
        return other - 273.15 * K
C = __C()

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

# Moles

mol = 1
particles = 1.0 / 6.0221409e+23

# Volume

m3 = 1

# Molar properties

m3_mol = m3 / mol
J_mol = J / mol
J_molK = J / (mol * K)

# Mass

kg = 1
g = 1e-3

# Specific properties

m3_kg = m3 / kg
J_kg = J / kg
J_kgK = J / (kg * K)