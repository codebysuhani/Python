#WAF TO FIND THE FACTORIAL OF n.(n is the parameter)


def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_factorial(5)