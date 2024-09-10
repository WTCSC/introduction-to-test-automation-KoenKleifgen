import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(8) == True
  assert math_it_up.is_even(4) == True
  assert math_it_up.is_even(202) == True
  assert math_it_up.is_even(9) == False
  assert math_it_up.is_even(4534) == True
  assert math_it_up.is_even(823487) == False
  assert math_it_up.is_even(2) == True
  assert math_it_up.is_even(1) == False
  assert math_it_up.is_even(6) == True
  assert math_it_up.is_even(3) == False
  assert math_it_up.is_even(5) == False
  assert math_it_up.is_even(7) == False
  assert math_it_up.is_even(675398794) == True

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(8) != False
  assert math_it_up.is_odd(4) != False
  assert math_it_up.is_odd(9) != True
  assert math_it_up.is_odd(2) != False
  assert math_it_up.is_odd(1) != True
  assert math_it_up.is_odd(6) != False
  assert math_it_up.is_odd(3) != True
  assert math_it_up.is_odd(5) != True
  assert math_it_up.is_odd(7) != True
  assert math_it_up.is_odd(85435919) != True
  assert math_it_up.is_odd(41913567) != True
  assert math_it_up.is_odd(876354964) != False

def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([1, 34543, 46, 562, 9346, 23456, 8963, 978325, 8743, 6293, 876345, 9876235]) == 985238.16667
  assert math_it_up.mean([23, 45, 25, 85, 25, 83, 765, 25, 877]) == 217
  assert math_it_up.mean([3, 73, 3245, 25, 28, 765, 267, 29, 298, 368913465182795, 8747609758615988765018]) == 795237284320859500000

def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([1, 34543, 46, 562, 9346, 23456, 8963, 978325, 8743, 6293, 876345, 9876235]) == 9154.5
  assert math_it_up.median([23, 45, 25, 85, 25, 83, 765, 25, 877]) == 45
  assert math_it_up.median([3, 73, 3245, 25, 28, 765, 267, 29, 298, 368913465182795, 8747609758615988765018]) == 267


def test_mode():
  """
  Tests for the `mode` function
  """
  assert math_it_up.mode([1, 1, 34543, 46, 562, 9346, 23456, 8963, 978325, 8743, 6293, 876345, 9876235]) == 1
  assert math_it_up.mode([23, 45, 25, 85, 25, 83, 765, 23, 25, 877]) == 23
  assert math_it_up.mode([3, 73, 3245, 25, 28, 765, 267, 3245, 29, 298, 368913465182795, 8747609758615988765018]) == 3245
