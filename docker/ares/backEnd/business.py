def get_data():
    with open('names.txt', 'r') as file:
        names = file.read().splitlines()
        return names