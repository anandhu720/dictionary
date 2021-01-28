import json
from difflib import *


data = json.load(open("data.jason.txt"))

def translator(word):        # translator is the user-defined function for find meaning of the searched word.
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word , data.keys() ,)) >0:
        print(  "did you mean %s instead of %s .\n " % (get_close_matches(word, data.keys())[0] , word))
        word = get_close_matches(word , data.keys())[0]
        x = input("if you mean it please click y else click n :   ")
        x = x.lower()
        if x == "y":
            return data[word]
        elif x == "n":
            return "the word doesn't exist . please cross-check it :"
        else:
            return "i can't understand the command :"
    else:
        return  "entered word has no meaning . please check in once more ! "

while True:
    word = input("enter the word:  ")
    output = translator(word)
    if type(output) == list:
        for i in output:
            print("* ",i)
    else:
        print(output)
