# # import addition
# # import pytest

# # def test_addition():
# #     assert addition.add_a_and_b(1,2) == 3
# #     assert addition.add_a_and_b(1,2) == 0
    
# # def test_subtraction():
# #     assert addition.subtract_a_and_b(2,1) == 1
# #     assert addition.subtract_a_and_b(2,1) == 10

# # # python -m pytest test-addition.py is the command to run the test
# import addition
# import pytest

# # More descriptive test function names
# def test_addition_1_plus_2():
#     assert addition.add_a_and_b(1, 2) == 3

# def test_addition_incorrect():
#     assert addition.add_a_and_b(1, 2) == 0

# def test_subtraction_2_minus_1():
#     assert addition.subtract_a_and_b(2, 1) == 1

# def test_subtraction_incorrect():
#     assert addition.subtract_a_and_b(2, 1) == 10

# # Consider parameterization for more comprehensive testing
# @pytest.mark.parametrize("a, b, expected", [
#     (1, 2, 3),
#     (3, 5, 8),
#     (-2, 3, 1), 
#     # Add more test cases here
# ])
# def test_addition_parameterized(a, b, expected):
#     assert addition.add_a_and_b(a, b) == expected 
import pytest
from addition import add_a_and_b, subtract_a_and_b 

# Parameterized tests for addition
@pytest.mark.parametrize("var1, var2, expected", [
    (1, 2, 3),
    (3, 5, 8),
    (-2, 3, 1)
   
    # Add more test cases here
])
def test_addition_parameterized(var1, var2, expected):
    assert add_a_and_b(var1, var2) == expected 

# Parameterized tests for subtraction
@pytest.mark.parametrize("var1, var2, expected", [
    (10, 5, 5),
    (5, 10, -5),
    (2, 2, 0),
    # Add more test cases here
])
def test_subtraction_parameterized(var1, var2, expected):
    assert subtract_a_and_b(var1, var2) == expected 
