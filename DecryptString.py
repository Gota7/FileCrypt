import sys
import os

PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

#Reverse
def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

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


def main(argv):

    #Define standard letters
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890-=[]\\;,./~!@#$%^&*()_+{}|:\"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    #Load key file
    keyFile = []
    with open(PATH + '/Decrypt.key', 'r') as txt:
        for line in txt.readlines():
            keyFile.append(line.rstrip())

    print(decrypt9(decrypt9(decrypt9(argv[0], keyFile[0], alpha), keyFile[0], alpha), keyFile[0], alpha))


if __name__ == "__main__":
    main(sys.argv[1:])

