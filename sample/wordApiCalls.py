from wordnik import *
import en
import os

apiUrl = 'http://api.wordnik.com/v4'
apiKey = os.environ['WORDNIK_API_KEY']
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)
wordsApi = WordsApi.WordsApi(client)\


def checkWord(word, word_type):
    # takes a word and a desired word_type
    #queries a dictionary to check if the two agree
    # returns False or True based on the response
    is_word = wordApi.getDefinitions(word, partOfSpeech=word_type)
    if is_word == None:
        return False
    else:
        return True
    
def checkCorrectWord(word):
    # takes a word 
    #queries a dictionary to check the word_type
    # returns False or True based on the response
    return wordApi.getDefinitions(word)[0].partOfSpeech

    
def getRandomWord(word_type):
    # takes a word type
    # returns a random word that matches it in a str format
    random_word = wordsApi.getRandomWord(includePartOfSpeech=word_type).word
    if checkWord(random_word, word_type):
        if word_type.upper() == "VERB":
            try:
                return en.verb.past(random_word)
            except KeyError:
                return getRandomWord(word_type)
        else:
            return random_word
    else:
        return getRandomWord(word_type)

