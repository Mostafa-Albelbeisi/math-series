

def fibonacci(n):
    if type(n) != int:
        return "You should add a number"
    elif n == 0 or n == 1:
        return n
    num1 = 0
    num2 = 1
    sum = 0
    for n in range(2, n + 1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return sum

#lucas#
def lucas(n):
    if type(n) != int:
        return "You should add a number"
    if n == 0:
        return 2
    elif n == 1:
        return n
    num1 = 2
    num2 = 1
    sum = 0
    for x in range(2, n+1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return sum

#sum_series#
def sum_series(n, x = 0, y = 1):
    if type(n) != int:
        return "You should add a number"
    elif n == 0:
        return x

    elif n == 1:
        return y
    
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)


