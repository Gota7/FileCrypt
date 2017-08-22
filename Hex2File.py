import sys, getopt, os
import binascii

PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

def main(argv):

   inputFile = []
   with open(PATH + '/DEC_output.txt', 'r') as txt:
       for line in txt.readlines():
           inputFile.append(line.rstrip())

   #Split input into hex chunks
   content = list(splitN(inputFile[0], 2))
   #print(chr(int(str(content[0]), 16)))
            
   #Write File
   with open(PATH + "/output.hex", 'w') as txt:
       for i, Contents in enumerate(content):
            txt.write(chr(int(str(content[i]), 16)))
       txt.close()


def splitN( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

if __name__ == "__main__":
   main(sys.argv[1:])
