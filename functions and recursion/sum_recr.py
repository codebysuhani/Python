#WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST n NATURAL NUMBERS.


def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1)+n

sum = calc_sum(10)
print(sum)