""" WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value. """

marks = {}

phy = int(input("enter marks of phy:"))
marks.update({"phy" : phy})

chem = int(input("enter marks of chem:"))
marks.update({"chem" : chem})

math = int(input("enter marks of math:"))
marks.update({"math" : math})

print(marks)