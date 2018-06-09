# pyDiction

[pyDiction](https://github.com/Shubh96/pyDiction) is a dictionary developed using [Python](https://www.python.org/) programming language version 3.6.1 in [Anaconda](https://anaconda.org/anaconda/python) environment. To build the dictionary a complete data set has been used, which is a [JSON](https://www.json.org/) file containing words as key and their corresponding meanings or definitions as Values, hence making a key-value pair, similar to [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) data structure in Python.

## Code Snippets
The code is very simple to understand though, just a few things that need to be noted are the ones I have included here.

    dictionaryData = json.load(open("DictionaryData.json"))
This line loads the JSON file into the scope of the code as a python dictionary into the variable *dictionaryData*.

    for count, meaning in enumerate(meanings, 1):
	    print("[Meaning %d]: %s " %(count , meaning))
In the above code ```enumerate``` acts as an iterator that traverses over the ```meanings``` list, and prints it out in the next line.

    similarWords = get_close_matches(query, dictionaryData.keys(), cutoff  =  0.75)
 The above line is the key in this entire code. The purpose for which this line is kept here is that, if user mistakenly enters some incorrect spelling of a word, then instead of having the user to repeat the entire process again, the dictionary automatically suggests a word which is close to the entered word.
	This is done with the help of the ```get_close_match()``` function, to which three parameters are passed, the last one being an optional argument.

In the above code, ```query``` is the first parameter that I have passed, which is the word that the user enters to find the meaning, the second argument passed is ```dictionary.keys()``` which is a list containing the words from the ```dictionaryData``` against which the word entered by the user will be matched for finding similarity. ```cutoff``` is the third parameter passed to the function, which specifies the degree  of strictness to which the match will be examined. Here, I have used 0.75 as the cutoff, but it can be set to any other value as per the need.

    except  KeyError  as e:
	    handleSimilarity(query)

In the main function, the above ```try-except```  block has been used in order to handle the ```KeyError``` which is generated if a particular key is not found in the ```dictionaryData```. Hence, it is handled by using the ```handleSimilarity``` method which checks for a similar match, if found then it returns that match else it responds by giving a *not found* message. 
