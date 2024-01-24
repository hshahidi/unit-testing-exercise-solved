import pytest
import YieldAverage_Solved
from YieldAverage_Solved import wafer_yield_count

"""
Wafer Lot 1:
Expected result is number of valid inputs.
Wafer lot contains maximum number of accepted inputs. 
"""
wafer_lot_1 = [0.8742, 0.2351, 0.6704, 0.1289, 0.9437, 0.5123, 0.7890, 0.3456, 0.6789, 0.4321,
0.9876, 0.1098, 0.8765, 0.5432, 0.2109, 0.6543, 0.3210, 0.9876, 0.5678, 0.2345,
0.8765, 0.4321, 0.7890, 0.1234, 0.5678]
def test_lot_count_1():
    expected_result = wafer_yield_count(wafer_lot_1)
    assert expected_result == 25

"""
Wafer Lot 2:
Expected result is number of valid inputs. 
Wafer lot contains some string inputs that should be ignored.
"""
wafer_lot_2 = ["0.8742", "0.2351", "0.6704", 0.1289, 0.9437, 0.5123, 0.7890, 0.3456, 0.6789, 0.4321,
0.9876, "0.1098", "0.8765", 0.5432, 0.2109, 0.6543, "0.3210", 0.9876, 0.5678, 0.2345,
0.8765, 0.4321, 0.7890, 0.1234, 0.5678]
def test_lot_count_2():
    expected_result = wafer_yield_count(wafer_lot_2)
    assert expected_result == 19


"""
Wafer Lot 3:
Expected result is error statement for exceeding lot size.
Wafer lot contains more than 25 inputs.
"""
wafer_lot_3 = [0.7654, 0.2981, 0.6743, 0.1245, 0.9098, 0.5123, 0.7890, 0.3456, 0.6789, 0.4321,
0.9876, 0.1098, 0.8765, 0.5432, 0.2109, 0.6543, 0.3210, 0.9876, 0.5678, 0.2345,
0.8765, 0.4321, 0.7890, 0.1234, 0.5678, 0.8765, 0.9876, 0.5432, 0.2109, 0.6543]
def test_lot_count_3():
    with pytest.raises(ValueError, match = "Error: Lot exceeds limit of 25 wafers."):
        wafer_yield_count(wafer_lot_3)


"""
Wafer Lot 4:
Expected result is number of valid inputs.
Wafer lot contains less than 25 inputs.
"""
wafer_lot_4 = [0.4567, 0.7890, 0.1234, 0.5678, 0.8901, 0.2345, 0.6789, 0.9012, 0.3456, 0.7890]
def test_lot_count_4():
    expected_result = wafer_yield_count(wafer_lot_4)
    assert expected_result == 10

"""
Wafer Lot 5:
Expected result throws error statement for invalid input.
Wafer lot contains negative numbers
"""
wafer_lot_5 = [-0.4567, -0.7890, -0.1234, -0.5678, -0.8901, -0.2345, -0.6789, -0.9012, -0.3456, -0.7890]
def test_lot_count_5():
    with pytest.raises(ValueError, match = "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."):
        wafer_yield_count(wafer_lot_5)

"""
Wafer Lot 6:
Expected result should count all valid inputs and ignore blank wafer inputs.
Wafer lot contains decimals between 0 and 1 inclusive and blank wafer inputs.
"""
wafer_lot_6 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, None, 0.5432, 0.0002, 0.1098, 0.125,
0.4321, None, 0.5678, 0.365, None, None, 0.2386, 0.156, 0.6543, 0.0123,
0.3356, 0.3456, 0.219, 0.4567, 0.1898]
def test_lot_count_6():
    expected_result = wafer_yield_count(wafer_lot_6)
    assert expected_result == 21
