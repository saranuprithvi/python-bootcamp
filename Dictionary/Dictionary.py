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
    elif len(get_close_matches(word , data.keys())) > 0:
        print("Did you mean %s ?" %get_close_matches(word,data.keys())[0])
        choice = input("Enter 'y' for yes and 'n' for no : ")
        if choice == "y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "You have entered wrong word !"
choice = "y"
while choice == "y":
    word = input("Enter word to search:")
    Dictionary_word = translate(word)
    if type(Dictionary_word) == list:
        for items in Dictionary_word:
            print(items)
    else:
        print(Dictionary_word)
    choice = input("Do you want to continue ? (y/n) ")
