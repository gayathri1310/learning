with open("names.txt","r") as f:
    names = f.read().split()

for i, name in enumerate(names):
    print(f"{i+1}. {name}")
