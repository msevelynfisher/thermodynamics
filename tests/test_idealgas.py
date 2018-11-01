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
    
    Vmol_predicted = td.Vmol_PT(P, T, substance, td.eos.IDEAL_GAS)
    Vmol_true = 0.0249434
    assert relative_error(Vmol_predicted, Vmol_true) < 1e-5
    
    Umol_predicted = td.Umol_PT(P, T, substance, td.eos.IDEAL_GAS)
    Umol_true = 6236
    assert relative_error(Umol_predicted, Umol_true) < 1e-3
    
    Hmol_predicted = td.Hmol_PT(P, T, substance, td.eos.IDEAL_GAS)
    Hmol_true = 8730
    assert relative_error(Hmol_predicted, Hmol_true) < 1e-3
    
    Smol_predicted = td.Smol_PT(P, T, substance, td.eos.IDEAL_GAS)
    Smol_true = -149.2
    assert relative_error(Smol_predicted, Smol_true) < 1e-3
