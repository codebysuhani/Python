""" Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types) """

values = {9,"9.0"}
print(values)

values_1 = {
    ("float", 9.0),
    ("int", 9)
}
print(values_1)