#WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.
#HINT:USE LIST AND INDEX AS PARAMETER

value = [ "a", "b", "c", "d", "e"]

def print_list(list, idx=0):
    if(idx == len(list)):
        return 0
    print(list[idx])
    print_list(list, idx+1)

print_list(value)