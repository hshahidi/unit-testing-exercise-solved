import pytest
import YieldAverage_Solved
from YieldAverage_Solved import YieldAverage


""" 
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
Contains elements between 0 and 1 and NULL types values.
Should return list with NULL types removed.
"""
def test_should_convert_blank_inputs():
    wafer_lot_3 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, None, 0.5432, 0.0002, 0.1098, 0.125, 0.4321, 
    None, 0.5678, 0.365, None, 0.2386, 0.156, 0.6543, 0.0123, 0.3356, 0.3456, 0.219, 0.4567, 0.1898]
    
    wafer_lot_3_expected = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.5432, 0.0002, 0.1098, 0.125, 0.4321,
    0.5678, 0.365, 0.2386, 0.156, 0.6543, 0.0123, 0.3356, 0.3456, 0.219, 0.4567, 0.1898]

    assert wafer_lot_3_expected == assess_wafer_yield(wafer_lot_3)


""" 
Contains all percent values that are between 0 and 100.
Should return the converted decimal equivalents while rounded to four decimal places.
"""
def test_should_convert_percents_into_decimals():
    wafer_lot_4 = [37.2, 12, 64.38, 18, 53, 0.777, 29, 42, 91, 10, 5, 68.01, 83, 25.312, 49, 36, 20, 1.5678, 57, 71, 13, 97, 45, 60, 14]

    wafer_lot_4_expected = [0.372, 0.12, 0.6438, 0.18, 0.53, 0.777, 0.29, 0.42, 0.91, 0.1, 0.05, 0.6801, 0.83, 0.2531, 0.49, 0.36, 
    0.2, 0.0157, 0.57, 0.71, 0.13, 0.97, 0.45, 0.6, 0.14]

    assert wafer_lot_4_expected == assess_wafer_yield(wafer_lot_4)


""" 
Contains random string values. 
Should return the converted string values to their float equivalents. 
"""
def test_should_convert_string_inputs():
    wafer_lot_5 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, "0.9876", 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, "0.9456", "0.7890", 0.7567, 0.8901]

    wafer_lot_5_expected = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, 0.9456, 0.7890, 0.7567, 0.8901]

    assert wafer_lot_5_expected == assess_wafer_yield(wafer_lot_5)


"""
Contains elements that are less than zero.
Should throw an error statement.
"""
def test_should_raise_error_for_less_than_0():
    wafer_lot_6 = [-0.4567, -0.7890, -0.1234, -0.5678, -0.8901, -0.2345, -0.6789, -0.9012, -0.3456, -0.7890]

    with pytest.raises(ValueError, match= "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        assess_wafer_yield(wafer_lot_6)

"""
Contains elements that are more than zero.
Should return an error statement.
"""
def test_should_raise_error_for_greater_than_100():
    wafer_lot_7 = [112.45, 117.89, 124.00, 130, 145.11, 150, 162, 175, 180, 192, 205, 210,
    225, 230, 242, 256, 267, 275, 280, 298, 305, 312, 327.34, 335, 349.45]

    with pytest.raises(ValueError, match= "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        assess_wafer_yield(wafer_lot_7)


""" 
Contains an empty wafer lot.
Should return an error statement.
"""
def test_throws_error_when_lot_is_empty():
    wafer_lot_8 = []

    with pytest.raises(ValueError, match = "Error: Wafer lot is empty."):
        assess_wafer_yield(wafer_lot_8)

""" 
Contains more than 25 elements.
Should return an error statement.
"""
def test_error_count_larger_than_25():
    wafer_lot_9 = [0.7654, 0.2981, 0.6743, 0.1245, 0.9098, 0.5123, 0.7890, 0.3456, 0.6789, 0.4321,
    0.9876, 0.1098, 0.8765, 0.5432, 0.2109, 0.6543, 0.3210, 0.9876, 0.5678, 0.2345,
    0.8765, 0.4321, 0.7890, 0.1234, 0.5678, 0.8765, 0.9876, 0.5432, 0.2109, 0.6543]

    with pytest.raises(ValueError, match = "Error: Wafer lot exceeds limit of 25 wafers."):
        assess_wafer_yield(wafer_lot_9)


"""
Expected result should round down to four decimal places.
Wafer lot contains decimals that are four decimal places in length.
"""
def test_return_rounded_down_average():
    wafer_lot_1 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, 0.9456, 0.7890, 0.7567, 0.8901]

    expected_result = lot_yield_average(wafer_lot_1)
    assert expected_result == 0.7919

"""
Expected result should round up to four decimal places.
Wafer lot contains decimals that are five decimal places in length.
"""
def test_return_rounded_up_average():
    wafer_lot_2 = [0.92346, 0.86784, 0.84568, 0.98764, 0.73213, 0.87893, 0.84329, 0.87653, 0.1098, 0.97654,
    0.73212, 0.53453, 0.56786, 0.87654, 0.98765, 0.94567, 0.78905, 0.79878, 0.65437, 0.61233,
    0.87655, 0.94563, 0.78904, 0.75673, 0.89012]

    expected_result = lot_yield_average(wafer_lot_2)
    assert expected_result == 0.7920

"""
Expected result should round up to four decimal places.
Wafer lot contains varying lengths of decimals, valid input is between 0 and 1 inclusive.
"""
def test_varying_lengths_of_decimal_returns_rounded_up_average():
    wafer_lot_3 = [0.34, 0.5678, 0.3456, 0.987, 0.4321, 0.6789, 0.5432, 0.876, 0.1098, 0.8765,
    0.41, 0.2345, 0.5678, 0.8765, 1, 0.6, 0.70, 0.0987, 0.6543, 0.0123,
    0.870, 0, 0.7890, 0.4500, 0.8901]

    expected_result = lot_yield_average(wafer_lot_3)
    assert expected_result == 0.5564

"""
Expected result should average all valid inputs and convert blank wafer inputs.
Wafer lot contains decimals between 0 and 1 inclusive and blank wafer inputs.
"""
def test_convert_blank_inputs():
    wafer_lot_4 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, None, 0.5432, 0.0002, 0.1098, 0.125,
    0.4321, None, 0.5678, 0.365, None, 0.2386, 0.156, 0.6543, 0.0123,
    0.3356, 0.3456, 0.219, 0.4567, 0.1898]

    expected_result = lot_yield_average(wafer_lot_4)
    assert expected_result == 0.3432


"""
Expected result shoud average all valid inputs.
Wafer lot contains less than 25 inputs.
"""
def test_average_lot_with_less_than_25():
    wafer_lot_5 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.6789, 0.5432, 0.8765, 0.1098, 0.8765,
    0.4321, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456]

    expected_result = lot_yield_average(wafer_lot_5)
    assert expected_result == 0.5616


"""
Expected result should throw error for exceeding lot limit.
Wafer lot contains more than 25 inputs.
"""
def test_throws_error_for_exceeding_limit_of_25():
    wafer_lot_6 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.6789, 0.5432, 0.8765, 0.1098, 0.8765,
    0.4321, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456, 0.7890, 0.0987, 0.6543, 0.0123,
    0.8765, 0.3456, 0.7890, 0.4567, 0.8901, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456]

    with pytest.raises(ValueError, match = "Error: Wafer lot exceeds limit of 25 wafers."):
        lot_yield_average(wafer_lot_6)


"""
Expected result should average all original and converted inputs. 
Wafer lot contains some percent inputs, convert these percents into their decimal equivalent.
"""
def test_average_all_converted_inputs():
    wafer_lot_7 = [37.2, 12, 64.38, 18, 53, .777, 29, 42, 91, 10, 5, 68.01, 83, 25.312, 49, 36, 20, 1.5678, 57, 71, 13, 97, 45, 60, 14]

    expected_result = lot_yield_average(wafer_lot_7)
    assert expected_result == 0.4317


"""
Expected result should average all the inputs that are in decimal format.
Wafer lot contains some input strings that should be converted.
"""
def test_converts_all_string_inputs():
    wafer_lot_8 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
    0.7321, 0.5345, 0.5678, 0.8765, "0.9876", 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
    0.8765, "0.9456", "0.7890", 0.7567, 0.8901]

    expected_result = lot_yield_average(wafer_lot_8)
    assert expected_result == 0.7919


"""
Expected result should throw error statement.
Wafer lot contains inputs greater than 100.
"""
def test_throws_error_for_inputs_greater_than_100():
    wafer_lot_9 = [112.45, 117.89, 124.00, 130, 145.11, 150, 162, 175, 180, 192, 205, 210,
    225, 230, 242, 256, 267, 275, 280, 298, 305, 312, 327.34, 335, 349.45]

    with pytest.raises(ValueError, match = "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        lot_yield_average(wafer_lot_9)

"""
Expected result should throw error statement.
Wafer lot contains inputs that are less than 0. 
"""
def test_throws_error_for_inputs_less_than_0():
    wafer_lot_10 = [-0.9234, -0.8678, -0.8456, -0.9876, -0.7321, -0.8789, -0.8432, -0.8765, -0.1098, -0.9765,
    -0.7321, -0.5345, -0.5678, -0.8765, -0.9876, -0.9456, -0.7890, -0.7987, -0.6543, -0.6123,
    -0.8765, -0.9456, -0.7890, -0.7567, -0.8901]

    with pytest.raises(ValueError, match = "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        lot_yield_average(wafer_lot_10)


"""
Expected result is an error statement when an empty list is passed.
"""
def test_throws_error_when_lot_is_empty():
    wafer_lot_11 = []
    
    with pytest.raises(ValueError, match = "Error: Wafer lot is empty."):
        lot_yield_average(wafer_lot_11)