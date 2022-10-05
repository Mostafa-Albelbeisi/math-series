
from math_series.math_series import fibonacci, lucas, sum_series

#fibonacci#
def test_string():
    assert fibonacci("") == "You should add a number"

def fibonacci_zero():
    assert fibonacci(0) == 0

def fibonacci_one():
    assert fibonacci(1) == 1

def fibonacci_two():
    assert fibonacci(2) ==1

def fibonacci_three():
    assert fibonacci(3) ==2

def fibonacci_four():
    assert fibonacci(4) ==3

def fibonacci_five():
    assert fibonacci(5) ==5

def fibonacci_six():
    assert fibonacci(6) ==8

def fibonacci_seven():
    assert fibonacci(7) ==13





    #lucas#
def test_string():
    actual = lucas("test")
    expected = "You should add a number"
    assert actual == expected

def test_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_three():
   actual = lucas(3)
   expected = 4
   assert actual == expected 

def test_four():
   actual = lucas(4)
   expected = 7
   assert actual == expected 

def test_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected 


#sum series#
def test_fibonacci():
    assert sum_series(7) == 13

def test_lucas():
    assert sum_series(7,2,1) == 29