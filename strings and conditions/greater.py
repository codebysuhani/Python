#WAP to find the greatest of 3 numbers entered by the user. 
num_1 = int(input("Enter 1st number:"))
num_2 = int(input("Enter 2nd number:"))
num_3 = int(input("Enter 3rd number:"))

if(num_1 >= num_2  and  num_1 >= num_3):
    print("Greatest number is",num_1)
if(num_2 >= num_1  and  num_2 >= num_3):
    print("Greatest number is",num_2)
else:
    print("Greatest number is",num_3)