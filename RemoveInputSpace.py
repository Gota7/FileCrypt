import sys
import os

PATH = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

#CleanSpaces

# first get all lines from file
with open(PATH+"/ENC_input.txt", 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]
lines = [line.replace('\n', '') for line in lines]

# finally, write lines in the file
with open(PATH+"/ENC_input.txt", 'w') as f:
    f.writelines(lines)
