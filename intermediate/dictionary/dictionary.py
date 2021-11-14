import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        print("Word not found!")

word = input("Please enter the word you want to search: ")
output = translate(word)
print(output)
