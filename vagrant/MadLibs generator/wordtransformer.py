# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    else:
        return word[0]
# TESTS 
# print word_transformer('NOUN')
# print word_transformer('VERB')
# print word_transformer('test')
# print word_transformer(' 456')