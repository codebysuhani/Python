#WAP TO FIND THE FACTORIAL OF FIRST n NUMBERS.(using for)

fact = 1
i = 1
n = 5

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)


fact = 1
i = 1
n = 3

while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)