import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # Get the close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead " %get_close_matches(word,data.keys())[0])
    else:
        print("Word not found!")

word = input("Please enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

