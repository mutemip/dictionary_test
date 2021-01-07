from difflib import get_close_matches
import json


file = json.load(open('data.json'))

def meaning(word):
    word = word.lower()
    if word in file:
        return file[word]
    elif len(get_close_matches(word, file.keys())) > 0:
        mp = input("Did you mean %s ? Enter y if yes and n if no: " % get_close_matches(word, file.keys())[0])
        if mp == "y":
            return file[get_close_matches(word, file.keys())[0]]
        elif mp == "n":
            return "This word is not available please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "This word is not available!"


word = (input("Enter a word: "))

output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)