#WAF TO PRINT THE ELEMENT OF A LIST IN A SINGLE LINE.(list is the parameter)

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cities = ["dehradun", "haridwar", "haldwani", "roorke", "shrinagar"]

def elements(list):
    for val in list:
        print(val, end=" ")
    print("\n")

elements(num)
elements(cities)