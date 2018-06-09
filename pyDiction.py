import json, os
from time import sleep                                                          #for sleep() function
from difflib import get_close_matches                                           #to predict matching words if user gives wrong spelling

dictionaryData = json.load(open("DictionaryData.json"))                         #Loading the data containing words and their meanings/definitions

def resolveWord(word):                                                          #Return queried word from dictionaryData
        return dictionaryData[word]

def displayResult(meanings):                                                    #to display the output
    for count, meaning in enumerate(meanings, 1):
        print("[Meaning %d]: %s " %(count , meaning))

def handleSimilarity(query):                                                    #if users enter incorrect spelling, it will suggest similar words
    similarWords = get_close_matches(query, dictionaryData.keys(), cutoff = 0.75)

    if len(similarWords) > 0:
        sleep(1)
        print("Did you mean %s instead?" %(similarWords[0]))
        confirm = input("Enter Y for Yes any other key for No: ")

        if confirm.lower() == 'y':
            meanings = resolveWord(similarWords[0])
            displayResult(meanings)
    else:
        print('I am sorry, " %s " is not in my dictionary' %query)

def main():                                                                     #main method
        try:
            query = input("Enter word/phrase: ")
            print("\n")
            meanings = resolveWord(query.lower())
            displayResult(meanings)

        except KeyError as e:                                                   #if word is not found in dictionary KeyError exception is thrown
            handleSimilarity(query)                                             #it is handled by showing similar words to user


if __name__ == "__main__":
    repeat = 'Y'                                                                #repeat until user wants to end the process
    while repeat.lower() != 'n':
        main()
        repeat = input("\nPress N to exit any other key to continue: ")
        os.system('cls')                                                        #to clear screen
