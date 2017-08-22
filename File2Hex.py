import sys, getopt, os
import binascii

PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

def main(argv):
   print(argv[0])

   filename = argv[0]
   with open(filename, 'rb') as f:
      content = f.read()
   newHex = str(binascii.hexlify(content))
   finalHex = newHex[2:]
   finalHex = finalHex[:-1]
   #print(finalHex)

   #Write File
   with open(PATH + '/ENC_input.txt', 'w') as txt:
       txt.write(finalHex)
       txt.close()
   

if __name__ == "__main__":
   main(sys.argv[1:])
