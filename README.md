# String Scrambler
A gibberish converter.

## Usage for existing programs
Read the instructions in Decrypt.key, and encrypt or decrypt strings by importing Decrytor into your python program, and using
Decryptor.decrypt(string) or Decryptor.encrypt(string).
These functions return strings. This is useful for existing python programs.

## Usage for fun
This program can also be used only to encrypt strings. Basically, read the encrypt usage instructions. It's format is:
python3 EncryptString.py stringToEncrypt

However, read the usage about backslashes and quotation marks.

Now for decrypting, it's simliar using DecryptString, however the encryptor may spit out a string with backslashes and/or quotes. When using variables in a python program this is not a problem, but you'll have to add backslashes as described in Encrypt_Usage.

##Enrypting Files
(Make sure to rearrange the characters in decrypt.key to something random, but no duplicates of characters. Use the randomKeygen.py to get this)

1. Open a file with HxD.
2. Ctrl A and Ctrl C to copy all the hex code.
3. Paste this in ENC_input.txt.
4. Run RemoveInputSpaces.
5. Run EncryptFile.
6. The output hex code will be in ENC_output.txt
7. Rename the output file with whatever crazy encrypted extension you want.

##Decrypting Files
1. Make sure your Decrypt.Key matches the person's who encrypted it.
2. Copy the encrypted hex code to DEC_input.txt
3. Run DecryptFile.
4. Create a new file, with an appropriate extension that matches the original file's.
5. Open the new file with HxD, and paste in the characters from DEC_output.txt.
6. Your file should now work like the original.

## License
Do whatever you want with it, I don't care. Copy it, mod it, use it for whatever reason. If you are using it for a program, or a game, please give me some credit for making it, but for small projects this is optional or not needed.
