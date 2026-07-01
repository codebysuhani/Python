with open("sample.txt", "r") as f:
    data = f.read()
    print(data)  #no need to close file, its automaticaly get closed.


with open("sample.txt", "w") as f:
    newdata = f.write("new line")
    print(newdata) 