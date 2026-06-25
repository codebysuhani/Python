#SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
#[1,4,9,16,25,36,49,64,81,100]

search = (1,4,9,16,25,36,49,64,81,100,36)

x = 36

i = 0
while i < len(search):
    if(search[i] == x):
        print("FOUND at index",i)
    else:
        print("finding...")
    i += 1

j = 0
for val in search:
    if(val == x):
        print("FOUND at index",j)
    else:
        print("finding...")
    j += 1