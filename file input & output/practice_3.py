#Search if the word “learning” exists in the file or not.

def check_for_word():
    word = "learning"
    with open("practice_1.txt", "r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("FOUND")
    else:
        print("NOT FOUND")


check_for_word()