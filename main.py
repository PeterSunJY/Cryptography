"""
This program is used to encode and decode various kinds of cipher.
This program runs in terminal. The python3 interpreter is needed.

Version: 4/12/2020 from Pycharm
"""

import os


class ReadAndWrite:
    """
    This class is used to read texts from input file and write texts
    to output files. If the output file is not empty, the new output
    will overwrite the file.
    """

    def __init__(self):
        self.localPath = os.getcwd()

    @staticmethod
    def file_read():
        fp = open("input_text.txt", "r")
        read_list = fp.read()
        fp.close()
        return read_list

    @staticmethod
    def file_write(write_list):
        fp = open("output_text.txt", "w")
        fp.write(write_list)
        fp.close()
        return ()


class UniversalInput:
    """
    This class is used to process input data. Different cipher need
    different kinds of input.
    """

    def __init__(self, text_type=None):
        self.textType = text_type

    @staticmethod
    def check_mode_input(actual_input, valid_input):
        """
        This function is used to check if user input invalid data.
        """
        if actual_input not in valid_input:
            print("The input is not valid, please try again.\n")
            return False
        else:
            return True

    def generalized_caesar_codes_input(self, mode3):
        text = None
        while True:
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError:
                print("Invalid input, k must be an integer.")
        if mode3 == "1":
            text = input("Please input the " + self.textType + " :\n")
        elif mode3 == "2":
            text = ReadAndWrite().file_read()
        input_list = [k, text]
        return input_list

    def linear_codes_input(self, mode3):
        text = None
        while True:
            try:
                a = int(input("Please input the value of a: \n"))
                break
            except ValueError:
                print("Invalid input, a must be an integer.")
        while True:
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError:
                print("Invalid input, k must be an integer.")
        if mode3 == "1":
            text = input("Please input the " + self.textType + " :\n")
        elif mode3 == "2":
            text = ReadAndWrite().file_read()
        input_list = [a, k, text]
        return input_list


class GeneralizedCaesarCodes:
    """
    This class is used to encode and decode generalized caesar codes
    """

    def __init__(self, k, ciphertext, plaintext):
        self.ciphertext_input = ciphertext
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
            print(j, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        for i in self.ciphertext_input:
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
            print(j, end="")
        print("\n")
        return self.plaintext


class LinearCodes:
    """
    This class is used to encode and decode linear codes
    """

    def __init__(self, a, k, ciphertext, plaintext):
        self.ciphertext_input = ciphertext
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
                i1 = (self.a * (ord(i) - 65) + self.k) % 26
                i2 = chr(i1 + 65)
                self.ciphertext.append(i2)
            elif i.islower():
                i1 = (self.a * (ord(i) - 97) + self.k) % 26
                i2 = chr(i1 + 97)
                self.ciphertext.append(i2)
            else:
                self.ciphertext.append(i)

        for j in self.ciphertext:
            print(j, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        for i in self.ciphertext_input:
            if i == " ":
                self.plaintext.append(i)
            elif i.isupper():
                i1 = ord(i) - 65 - self.k
                while i1 % self.a != 0 or i1 < 0:
                    i1 += 26
                i2 = chr(int(i1 / self.a) + 65)
                self.plaintext.append(i2)
            elif i.islower():
                i1 = ord(i) - 97 - self.k
                while i1 % self.a != 0 or i1 < 0:
                    i1 += 26
                i2 = chr(int(i1 / self.a) + 97)
                self.plaintext.append(i2)
            else:
                self.plaintext.append(i)

        for j in self.plaintext:
            print(j, end="")
        print("\n")
        return self.plaintext


def mode():
    """
    This function is used to process different modes. Mode1 represent which
    kinds of code users want to choose. Mode2 represent the choice between
    encode and decode. Mode3 represent manually input data or read from input
    file.
    """
    while True:
        mode1 = input("Please input number to choose the type of cipher.\n\
            1. Generalized Caesar Codes\n\
            2. LinearCodes\n")
        if UniversalInput().check_mode_input(mode1, ["1", "2"]):
            break
        else:
            continue
    while True:
        mode2 = input("Please input number to choose encode or decode.\n\
            1. Encode\n\
            2. Decode\n")
        if UniversalInput().check_mode_input(mode2, ["1", "2"]):
            break
        else:
            continue
    while True:
        mode3 = input("Please input number to choose input method.\n\
            1. Manual input\n\
            2. Read file \"input_text.txt\" at local path\n")
        if UniversalInput().check_mode_input(mode3, ["1", "2"]):
            break
        else:
            continue

    if mode1 == "1":
        if mode2 == "1":
            input_list = UniversalInput("plain text").generalized_caesar_codes_input(mode3)
            gcc = GeneralizedCaesarCodes(input_list[0], 0, input_list[1])
            ReadAndWrite().file_write(''.join(gcc.encode()))

        elif mode2 == "2":
            input_list = UniversalInput("cipher text").generalized_caesar_codes_input(mode3)
            gcc = GeneralizedCaesarCodes(input_list[0], input_list[1], 0)
            ReadAndWrite().file_write(''.join(gcc.decode()))

    elif mode1 == "2":
        if mode2 == "1":
            input_list = UniversalInput("plain text").linear_codes_input(mode3)
            lc = LinearCodes(input_list[0], input_list[1], 0, input_list[2])
            ReadAndWrite().file_write(''.join(lc.encode()))

        elif mode2 == "2":
            input_list = UniversalInput("cipher text").linear_codes_input(mode3)
            lc = LinearCodes(input_list[0], input_list[1], input_list[2], 0)
            ReadAndWrite().file_write(''.join(lc.decode()))


def main():
    while True:
        mode()
    # ReadAndWrite().FileRead("plaintext")


if __name__ == '__main__':
    main()
