#WAP to check if a list contain a palindrome of elements.(Hint:use copy()method)

list = [1, 2 , 3 , 2 , 1]
list_1 = list.copy()
list_1.reverse()
print(list)
print(list_1)

if(list == list_1):
    print("List contain palindrome elements")
else:
    print("List do not contain palindrome elements") 