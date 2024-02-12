import pytest
import YieldAverage_Solved
from YieldAverage_Solved import assess_wafer_yield

"""
Wafer Lot 1: 
Contains wafer lot of yields that are four decimal places long.
Should return all elements.
"""
def test_should_pass_acceptable_wafer_lot():
    wafer_lot_1 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765, 0.7321, 0.5345, 0.5678, 
    0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123, 0.8765, 0.9456, 0.7890, 0.7567, 0.8901]

    wafer_lot_1_expected = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765, 
    0.7321, 0.5345, 0.5678, 0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,0.8765, 0.9456, 0.7890, 0.7567, 0.8901]

    assert wafer_lot_1_expected == assess_wafer_yield(wafer_lot_1)

"""
Wafer Lot 2:
Contains wafer lot of acceptable elements that are 0 and 1 inclusive.
Should return all elements.
"""
def test_contains_0_and_1():
    wafer_lot_2 = [0.34, 0.5678, 0.3456, 0.987, 0.4321, 0.6789, 0.5432, 0.876, 0.1098, 0.8765, 0.41, 0.2345, 
    0.5678, 0.8765, 1, 0.6, 0.70, 0.0987, 0.6543, 0.0123, 0.870, 0, 0.7890, 0.4500, 0.8901]

    wafer_lot_2_expected = [0.34, 0.5678, 0.3456, 0.987, 0.4321, 0.6789, 0.5432, 0.876, 0.1098, 0.8765, 0.41, 0.2345, 
    0.5678, 0.8765, 1, 0.6, 0.70, 0.0987, 0.6543, 0.0123, 0.870, 0, 0.7890, 0.4500, 0.8901]

    assert wafer_lot_2_expected == assess_wafer_yield(wafer_lot_2)
    

"""
Wafer Lot 3:
Contains elements between 0 and 1 and NULL types values.
Should return list with NULL types removed.
"""
def test_should_ignore_blank_inputs():
    wafer_lot_3 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, None, 0.5432, 0.0002, 0.1098, 0.125, 0.4321, 
    None, 0.5678, 0.365, None, 0.2386, 0.156, 0.6543, 0.0123, 0.3356, 0.3456, 0.219, 0.4567, 0.1898]
    
    wafer_lot_3_expected = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.5432, 0.0002, 0.1098, 0.125, 0.4321,
    0.5678, 0.365, 0.2386, 0.156, 0.6543, 0.0123, 0.3356, 0.3456, 0.219, 0.4567, 0.1898]

    assert wafer_lot_3_expected == assess_wafer_yield(wafer_lot_3)


""" 
Wafer Lot 4:
Contains all percent values that are between 0 and 100.
Should return the converted decimal equivalents while rounded to four decimal places.
"""
def test_should_convert_percents_into_decimals():
    wafer_lot_4 = [37.2, 12, 64.38, 18, 53, 0.777, 29, 42, 91, 10, 5, 68.01, 83, 25.312, 49, 36, 20, 1.5678, 57, 71, 13, 97, 45, 60, 14]

    wafer_lot_4_expected = [0.372, 0.12, 0.6438, 0.18, 0.53, 0.777, 0.29, 0.42, 0.91, 0.1, 0.05, 0.6801, 0.83, 0.2531, 0.49, 0.36, 
    0.2, 0.0157, 0.57, 0.71, 0.13, 0.97, 0.45, 0.6, 0.14]

    assert wafer_lot_4_expected == assess_wafer_yield(wafer_lot_4)


""" 
Wafer Lot 5:
Contains random string values. 
Should return the converted string values to their float equivalents. 
"""
def test_should_ignore_string_inputs():
    wafer_lot_5 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, "0.9876", 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, "0.9456", "0.7890", 0.7567, 0.8901]

    wafer_lot_5_expected = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, 0.9456, 0.7890, 0.7567, 0.8901]

    assert wafer_lot_5_expected == assess_wafer_yield(wafer_lot_5)


"""
Wafer Lot 6:
Contains elements that are less than zero.
Should throw an error statement.
"""
def test_should_raise_error_for_less_than_0():
    wafer_lot_6 = [-0.4567, -0.7890, -0.1234, -0.5678, -0.8901, -0.2345, -0.6789, -0.9012, -0.3456, -0.7890]

    with pytest.raises(ValueError, match= "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        assess_wafer_yield(wafer_lot_6)

"""
Wafer Lot 7:
Contains elements that are more than zero.
Should return an error statement.
"""
def test_should_raise_error_for_greater_than_100():
    wafer_lot_7 = [112.45, 117.89, 124.00, 130, 145.11, 150, 162, 175, 180, 192, 205, 210,
    225, 230, 242, 256, 267, 275, 280, 298, 305, 312, 327.34, 335, 349.45]

    with pytest.raises(ValueError, match= "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        assess_wafer_yield(wafer_lot_7)


""" 
Wafer Lot 8:
Contains an empty wafer lot.
Should return an error statement.
"""
def test_throws_error_when_lot_is_empty():
    wafer_lot_8 = []

    with pytest.raises(ValueError, match = "Error: Wafer lot is empty."):
        assess_wafer_yield(wafer_lot_8)

""" 
Wafer Lot 9:
Contains more than 25 elements.
Should return an error statement.
"""
def test_error_count_larger_than_25():
    wafer_lot_9 = [0.7654, 0.2981, 0.6743, 0.1245, 0.9098, 0.5123, 0.7890, 0.3456, 0.6789, 0.4321,
    0.9876, 0.1098, 0.8765, 0.5432, 0.2109, 0.6543, 0.3210, 0.9876, 0.5678, 0.2345,
    0.8765, 0.4321, 0.7890, 0.1234, 0.5678, 0.8765, 0.9876, 0.5432, 0.2109, 0.6543]

    with pytest.raises(ValueError, match = "Error: Wafer lot exceeds limit of 25 wafers."):
        assess_wafer_yield(wafer_lot_9)





