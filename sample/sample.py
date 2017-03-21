from __future__ import print_function
import random
import wordApiCalls as words

class Cadavre_Exquis():
    def __init__(self):
        self.word_type = "adjective"
        self.sentence = ["The"]
        
    def check_progress(self):
        last_word = self.sentence[len(self.sentence)-1]
        if last_word.upper() == "THE":
            return "adjective"
        else:
            if self.word_type.upper() == "ADJECTIVE":
                return "noun"
            elif self.word_type.upper() == "NOUN":
                return "adverb"
            elif self.word_type.upper() == "ADVERB":
                return "verb"

    def add_to_sentence(self, word):
        self.sentence.append(word.lower())
        if self.word_type.upper() == "VERB":
            self.sentence.append("the")
        return print("Your sentence is: " + " ".join(self.sentence))

    def update_word_type(self):
        self.word_type = self.check_progress()


def main():
    game = Cadavre_Exquis()
    ask_start = raw_input("Would you like to start the sentence, or for the computer to start? "
                          "Type Y for you, C for computer, or E if you would like to exit. ")
    if ask_start.upper() == "Y":
        turn = True 
    elif ask_start.upper() == "C":
        turn = False
    elif ask_start.upper() == "E":
        return
    else:
        print("Looks like you haven't chosen a valid option. Try again.")
        return main()
    while len(game.sentence) < 8:
        if turn:
            ask_user = raw_input("Please choose a word. The word should be: " + game.word_type + ". ")
            if words.checkWord(str(ask_user), game.word_type):
                game.add_to_sentence(ask_user)
                turn = False
                game.update_word_type()
            else:
                print("Oops, looks like your word wasn't a " + game.word_type + ". Try again.")
        else:
            game.add_to_sentence(words.getRandomWord(game.word_type))
            turn = True
            game.update_word_type()
    repeat = raw_input("Would you like to play again? Y for yes, N for no. ")
    if repeat.upper() == 'Y':
        return main()
    else:
        print("Thanks for playing! Bye.")
                    
if __name__ == '__main__':
    main()
