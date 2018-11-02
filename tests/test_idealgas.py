import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import thermodynamics as td
import thermodynamics.unit as u

def relative_error(predicted, true):
    return abs((predicted - true) / true)

def test_idealgas():
    P = 100 * u.kPa
    T = 300 * u.K
    substance = {
        'specific-heat-ratio': 1.4
    }
    parameters = [
        (td.Vmol_PT, 0.0249434),
        (td.Umol_PT, 6236),
        (td.Hmol_PT, 8730),
        (td.Smol_PT, -149.2)
    ]
    
    for function, value in parameters:
        
        # Forward
        value_predicted = function(P, T, substance, td.eos.IDEAL_GAS)
        assert relative_error(value_predicted, value) < 1e-3
        
        # Backward, Pressure
        try:
            P_predicted = td.seek(
                value_predicted, function, None, T, substance, td.eos.IDEAL_GAS
            )
            assert relative_error(P_predicted, P) < 1e-3
        except td.FunctionalIndependenceError:
            pass
        
        # Backward, Temperature
        try:
            T_predicted = td.seek(
                value_predicted, function, P, None, substance, td.eos.IDEAL_GAS
            )
            assert relative_error(T_predicted, T) < 1e-3
        except FunctionalIndependenceError:
            pass
