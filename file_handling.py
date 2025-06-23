try:
    with open("logs.txt" , "r")  as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found")


with open ("file2.txt" , "w") as file:
    file.write("Hello world")


import json

with open("sample.json") as file:
    data = json.load(file)
    print(data)

