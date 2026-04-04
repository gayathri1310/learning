f = open("sample.txt", "r+")
print(f.read())
f.write("\nAdding new line by using write method")
f.close()