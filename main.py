'''
This program is used to decipher the ciphertext of linear code 
with value of a and k. Input the ciphertext, a and k, than the 
program will print the plaintext.
'''

# This version is from Pycharm

import os


class ReadAndWrite:

    def __init__(self):
        self.localPath = os.getcwd()

    def FileRead(self):
        fp = open("input_text.txt", "r")
        readList = fp.read()
        fp.close()
        return(readList)

    def FileWrite(self, writeList):
        fp = open("output_text.txt", "w")
        fp.write(writeList)
        fp.close()
        return()


class UniversalInput:

    def __init__(self, textType = None):
        self.textType = textType

    def checkModeInput(self, actualInput, validInput):
        if actualInput not in validInput:
            print("The input is not valid, please try again.\n")
            return(False)
        else:
            return(True)

    def GeneralizedCaesarCodesInput(self, mode3):
        while(True):
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError: 
                print("Invalid input, k must be an integer.")
        if mode3 == "1":
            text = input("Please input the " + self.textType +" :\n")
        elif mode3 == "2" :
            text = ReadAndWrite().FileRead()
        inputList = [k, text]
        return(inputList)

    def linearCodesInput(self, mode3):
        while(True):
            try:           
                a = int(input("Please input the value of a: \n"))
                break
            except ValueError:
                print("Invalid input, a must be an integer.")
        while(True):
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError:
                print("Invalid input, k must be an integer.")
        if mode3 == "1":
            text = input("Please input the " + self.textType +" :\n")
        elif mode3 == "2":
            text = ReadAndWrite().FileRead()
        inputList = [a, k, text]
        return(inputList)



class GeneralizedCaesarCodes:

    def __init__(self, k, ciphertext, plaintext):
        self.ciphertextInput = ciphertext
        self.plaintextInput = plaintext
        self.k = k
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        for i in self.plaintextInput:
            if i == " ":
                self.ciphertext.append(i)
            elif i.isupper():
                i1 = (ord(i) - 65 + self.k) % 26
                i2 = chr(i1 + 65)
                self.ciphertext.append(i2)
            elif i.islower():
                i1 = (ord(i) - 97 + self.k) % 26
                i2 = chr(i1 + 97)
                self.ciphertext.append(i2)
            else:
                self.ciphertext.append(i)
        for j in self.ciphertext:
            print(j, end = "")
        print("\n")
        return(self.ciphertext)


    def decode(self):
        for i in self.ciphertextInput:
            if i == " ":
                self.plaintext.append(i)
            elif i.isupper():
                i1 = ord(i) - 65 - self.k
                if i1 < 0:
                    i1 += 26
                i2 = chr(i1 + 65)
                self.plaintext.append(i2)
            elif i.islower():
                i1 = ord(i) - 97 - self.k
                if i1 < 0:
                    i1 += 26
                i2 = chr(i1 + 97)
                self.plaintext.append(i2)
            else:
                self.plaintext.append(i)

        for j in self.plaintext:
            print(j, end = "")
        print("\n")
        return(self.plaintext)


class LinearCodes:

    def __init__(self, a, k, ciphertext, plaintext):
        self.ciphertextInput = ciphertext
        self.plaintextInput = plaintext
        self.a = a
        self.k = k
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        for i in self.plaintextInput:
            if i == " ":
                self.ciphertext.append(i)
            elif i.isupper():
                i1 = (self.a*(ord(i) - 65) + self.k) % 26
                i2 = chr(i1 + 65)
                self.ciphertext.append(i2)
            elif i.islower():
                i1 = (self.a*(ord(i) - 97) + self.k) % 26
                i2 = chr(i1+97)
                self.ciphertext.append(i2)
            else:
                self.ciphertext.append(i)

        for j in self.ciphertext:
            print(j, end = "")
        print("\n")
        return(self.ciphertext)


    def decode(self):
        for i in self.ciphertextInput:
            if i == " ":
                self.plaintext.append(i)
            elif i.isupper():
                i1 = ord(i) - 65 - self.k
                while i1 % self.a != 0 or i1 < 0:
                    i1 += 26
                i2 = chr(int(i1/self.a) + 65)
                self.plaintext.append(i2)
            elif i.islower():
                i1 = ord(i) - 97 - self.k
                while i1 % self.a != 0 or i1 < 0:
                    i1 += 26
                i2 = chr(int(i1/self.a) + 97)
                self.plaintext.append(i2)
            else:
                self.plaintext.append(i)

        for j in self.plaintext:
            print(j, end = "")
        print("\n")
        return(self.plaintext)

def mode():
    while(True):
        mode1 = input("Please input number to choose the type of cipher.\n\
            1. Generalized Caesar Codes\n\
            2. LinearCodes\n")
        if UniversalInput().checkModeInput(mode1, ["1","2"]):
            break
        else:
            continue
    while(True):
        mode2 = input("Please input number to choose encode or decode.\n\
            1. Encode\n\
            2. Decode\n")
        if UniversalInput().checkModeInput(mode2, ["1","2"]):
            break
        else:
            continue
    while(True):
        mode3 = input("Please input number to choose input method.\n\
            1. Manual input\n\
            2. Read file \"input_text.txt\" at local path\n")
        if UniversalInput().checkModeInput(mode3, ["1","2"]):
            break
        else:
            continue

    if mode1 == "1":
        if mode2 == "1":
            inputlist = UniversalInput("plaintext").GeneralizedCaesarCodesInput(mode3)
            GCC = GeneralizedCaesarCodes(inputlist[0], 0, inputlist[1])
            ReadAndWrite().FileWrite(''.join(GCC.encode()))

        elif mode2 == "2":
            inputlist = UniversalInput("ciphertext").GeneralizedCaesarCodesInput(mode3)
            GCC = GeneralizedCaesarCodes(inputlist[0], inputlist[1], 0)
            ReadAndWrite().FileWrite(''.join(GCC.decode()))

    elif mode1 == "2":
        if mode2 == "1":
            inputlist = UniversalInput("plaintext").linearCodesInput(mode3)
            LC = LinearCodes(inputlist[0], inputlist[1], 0, inputlist[2])
            ReadAndWrite().FileWrite(''.join(LC.encode()))
            
        elif mode2 == "2":
            inputlist = UniversalInput("ciphertext").linearCodesInput(mode3)
            LC = LinearCodes(inputlist[0], inputlist[1], inputlist[2], 0)
            ReadAndWrite().FileWrite(''.join(LC.decode()))
    


def main():
    while(True):
        mode()
    #ReadAndWrite().FileRead("plaintext")

if __name__ == '__main__':
    main()


