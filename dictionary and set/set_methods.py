collection = set()
collection.add(1)
collection.add(2)
collection.add(5)
collection.add(1)  #ignore duplicate value
collection.add("suhu")
collection.add((1, 2, 3))

#collection.add([1, 2, 3])

print(collection)
print(len(collection))

collection.remove(5)
print(collection)

collection.clear()  #clear all elements of set
print(len(collection))

subject = {"phy", "chem", "bio", "math", "comp.", "hindi", "eng"}
print(subject.pop())
print(subject.pop())