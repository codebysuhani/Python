#WAF that replace all occurrences of “java” with “python” in practice_1 file.

with open("practice_1.txt", "r") as f:
    data = f.read()

    newdata = data.replace("Java", "Python")
    print(newdata)

    with open("practice_1.txt", "w") as f:
        f.write(newdata)