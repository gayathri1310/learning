a = int(input("enter a number: "))

b = int(input("enter another number: "))
try:
    c = a / b
    print("the result is: ", c)
except :
    print("you cannot divide a number by zero")