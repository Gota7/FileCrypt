from random import shuffle

word = "abcdefghijklmnopqrstuvwxyz1234567890-=[]\\;,./~!@#$%^&*()_+{}|:\"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

print(shuffle_word(word))
