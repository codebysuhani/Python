student = {
    "name" : "Tanu",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,
    }
}

print(list(student.keys()))
print(len(student))    #or print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])


