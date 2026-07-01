""" Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming  in java. """


with open("practice_1.txt", "w") as f:
    f.write("Hi everyone.\nWe are learning file I/O\n")
    f.write("using Java.\nI like programming in Java.")