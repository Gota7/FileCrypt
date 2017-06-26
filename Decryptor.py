import os
import sys

#Define PATH
PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

#Encrypt function for a string
def encrypt9(string, key, alpha):

    #Decrypted string
    newString = ""

    #Time for the for loops
    for letters in range(len(string)):
        for letters2 in range(len(alpha)):
            if string[letters] == alpha[letters2]:
                newString+=key[letters2]

    return reverse(newString)


#Decrypt function for a string
def decrypt9(string, key, alpha):

    string = reverse(string)

    #Decrypted string
    newString = ""

    #Time for the for loops
    for letters in range(len(string)):
        for letters2 in range(len(key)):
            if string[letters] == key[letters2]:
                newString+=alpha[letters2]

    return newString



#Reverse
def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

#Shove everything inside me
def decrypt(argv):

    input = argv
    print(input)


    #Define PATH
    PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")


    #Define standard letters
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890-=[]\\;,./~!@#$%^&*()_+{}|:\"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    #Load key file
    keyFile = []
    with open(PATH + '/Decrypt.key', 'r') as txt:
        for line in txt.readlines():
            keyFile.append(line.rstrip())

    outputString = decrypt9(decrypt9(decrypt9(input, keyFile[0], alpha), keyFile[0], alpha), keyFile[0], alpha)

    return outputString

def encrypt(argv):

    #Define standard letters
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890-=[]\\;,./~!@#$%^&*()_+{}|:\"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    #Load key file
    keyFile = []
    with open(PATH + '/Decrypt.key', 'r') as txt:
        for line in txt.readlines():
            keyFile.append(line.rstrip())

    return encrypt9(encrypt9(encrypt9(argv, keyFile[0], alpha), keyFile[0], alpha), keyFile[0], alpha)
