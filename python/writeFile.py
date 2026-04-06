"""
Write a program to create a text file and write some content to it.
Using file functions like write and open.
"""
file_name = "example.txt"

f = open(file_name, "w")
f.write("Writing some content to the file.")
f.close() 
