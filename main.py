"""
This program is used to encode and decode various kinds of cipher.
This program runs in terminal. The python3 interpreter is needed.

Version: 13:40 4/28/2020 from Pycharm
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
        return

    def rsa_file_read(self, mode2):
        if mode2 == "1":
            return self.file_read()
        elif mode2 == "2":
            fp = open("input_text.txt", "r")
            read_list1 = fp.readlines()
            read_list2 = []
            for line in read_list1:
                line = line.strip()
                read_list2.append(line)
            fp.close()
            return read_list2

    def rsa_file_write(self, mode2, write_list):
        if mode2 == "1":
            fp = open("output_text.txt", "w")
            for i in write_list:
                fp.write(i)
                fp.write("\n")
            fp.close()
        elif mode2 == "2":
            self.file_write(write_list)


class UniversalInput:
    """
    This class is used to process input data. Different cipher need
    different kinds of input.
    """

    def __init__(self, text_type=None):
        self.text_type = text_type

    @staticmethod
    def prime(x):
        check = True
        for i in range(2, x):
            if x % i == 0:
                check = False
        return check

    @staticmethod
    def relatively_prime(a, b):
        check = True
        if a > b:
            for i in range(2, b + 1):
                if b % i == 0 and a % i == 0:
                    check = False
        else:
            for i in range(2, a + 1):
                if a % i == 0 and b % i == 0:
                    check = False
        return check

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

    def check_mode3(self, mode3):
        text = None
        if mode3 == "1":
            text = input("Please input the " + self.text_type + " :\n")
        elif mode3 == "2":
            text = ReadAndWrite().file_read()
        return text

    def rsa_check_mode3(self, mode2, mode3):
        text = None
        if mode3 == "1":
            text = input("Please input the " + self.text_type + " :\n")
        elif mode3 == "2":
            text = ReadAndWrite().rsa_file_read(mode2)
        return text

    def generalized_caesar_codes_input(self, mode3):
        while True:
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError:
                print("Invalid input, k must be an integer.")
        text = self.check_mode3(mode3)
        input_list = [k, text]
        return input_list

    def linear_codes_input(self, mode3):
        while True:
            try:
                a = int(input("Please input the value of a: \n"))
                if self.relatively_prime(a, 26):
                    break
                else:
                    print("The value of a is not valid, a must be relatively prime with 26.\n")
                    continue
            except ValueError:
                print("Invalid input, a must be an integer.")
        while True:
            try:
                k = int(input("Please input the value of k: \n"))
                break
            except ValueError:
                print("Invalid input, k must be an integer.")
        text = self.check_mode3(mode3)
        input_list = [a, k, text]
        return input_list

    def vigenere_cipher_input(self, mode3):
        while True:
            key_phrase = input("Please input the key phrase: \n")
            if key_phrase.islower():
                break
            else:
                print("key phrase must be lowercase letter")
                continue
        text = self.check_mode3(mode3)
        input_list = [key_phrase, text]
        return input_list

    def hill_cipher_input(self, mode3):
        while True:
            input_list = ["a", "b", "c", "d"]
            for i in range(len(input_list)):
                while True:
                    try:
                        input_list[i] = int(input("Please input the value of " + input_list[i] + " :\n"))
                        break
                    except ValueError:
                        print("Invalid input, " + input_list[i] + " must be an integer")
            f = 1
            p = (input_list[0] * input_list[3] - input_list[1] * input_list[2]) % 26
            while (p * f) % 26 != 1:
                f += 1
                if f == 10000:
                    break
            if f == 10000:
                print("The value of a, b, c, d are not valid.\nad-bc must have an inverse number in mod 26\n")
                continue
            else:
                break
        text = self.check_mode3(mode3)
        input_list.append(text)
        return input_list

    def autokey_cipher_input(self, mode3):
        while True:
            seed = input("Please input the seed: \n")
            if seed.islower():
                seed = ord(seed) - 97
                break
            else:
                print("Invalid seed, the seed must be a lower case letter.\n")
                continue
        text = self.check_mode3(mode3)
        input_list = [seed, text]
        return input_list

    def vernam_cipher_input(self, mode3, input_type):
        i = None
        text = None
        input_list = []
        if input_type == "plain text":
            while True:
                text = self.check_mode3(mode3)
                if text.islower():
                    break
                else:
                    print("The input plain text must be lower case letters with no space.\n")
                    mode3 = "1"
                    continue
        elif input_type == "cipher text":
            check = False
            while True:
                text = self.check_mode3(mode3)
                for i in text:
                    if self.check_mode_input(i, ["0", "1"]):
                        check = True
                        continue
                    else:
                        check = False
                        break
                if check:
                    break
                else:
                    print("The cipher text must be binary.\n")
                    mode3 = "1"
                    continue

        while True:
            key_stream = input("Please input key stream, it must be exact 5 times the length of the plaintext.\n")
            if input_type == "plain text":
                if len(key_stream) != 5 * len(text):
                    print("The key stream is not valid.\n")
                    continue
            for i in range(len(key_stream)):
                if self.check_mode_input(key_stream[i], ["0", "1"]):
                    continue
                else:
                    break
            if i != len(key_stream) - 1:
                continue
            else:
                input_list = [key_stream, text]
                break
        return input_list

    def rsa_input(self, mode2, mode3):
        pq = []
        input_pq = ["p", "q"]
        for i in range(len(input_pq)):
            while True:
                try:
                    pq.append(int(input("Please input the value of " + input_pq[i] + ".\n")))
                    if self.prime(pq[i]):
                        break
                    else:
                        del pq[-1]
                        print("Invalid input, p must be a prime number.")
                except ValueError:
                    print("Invalid input. The value of p and q must be integers.")
        m = pq[0] * pq[1]
        n = (pq[0]-1) * (pq[1] - 1)
        print("The value of m is " + str(m))
        print("The value of n is " + str(n))
        e = None
        while True:
            try:
                e = int(input("Please input the value of e. The value of e must be relatively prime with n.\n"))
                if self.relatively_prime(e, n):
                    if 0 <= e < n:
                        break
                    else:
                        print("Invalid input. The value of e must satisfy 0 <= e < n.\n")
                        continue
                else:
                    print("Invalid input. The value of e and n must be relatively prime.")
                    continue
            except ValueError:
                print("Invalid input, the value of e must be an integer.\n")
                continue
        text = self.rsa_check_mode3(mode2, mode3)
        input_list = [m, n, e, text]
        return input_list


class GeneralizedCaesarCodes:
    """
    This class is used to encode and decode Generalized Caesar Codes
    """

    def __init__(self, k, ciphertext, plaintext):
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.k = k
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        for i in self.plaintext_input:
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
                while i1 < 0:
                    i1 += 26
                i2 = chr(i1 + 65)
                self.plaintext.append(i2)
            elif i.islower():
                i1 = ord(i) - 97 - self.k
                while i1 < 0:
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
    This class is used to encode and decode Linear Codes
    """

    def __init__(self, a, k, ciphertext, plaintext):
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.a = a
        self.k = k
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        for i in self.plaintext_input:
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


class VigenereCipher:
    """
    This class is used to encode and decode Vigenere Cipher
    """

    def __init__(self, key_phrase, ciphertext, plaintext):
        self.key_phrase = key_phrase
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        key_index = 0
        for i in self.plaintext_input:
            if i == " ":
                self.ciphertext.append(i)
            elif i.isupper():
                i1 = ord(i) - 65
                j = self.key_phrase[key_index]
                j1 = ord(j) - 97
                cipher = chr((j1 + i1) % 26 + 65)
                self.ciphertext.append(cipher)
            elif i.islower():
                i1 = ord(i) - 97
                j = self.key_phrase[key_index]
                j1 = ord(j) - 97
                cipher = chr((j1 + i1) % 26 + 97)
                self.ciphertext.append(cipher)
            else:
                self.ciphertext.append(i)
            key_index += 1
            if key_index == len(self.key_phrase):
                key_index = 0

        for k in self.ciphertext:
            print(k, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        key_index = 0
        for i in self.ciphertext_input:
            if i == " ":
                self.plaintext.append(i)
            elif i.isupper():
                i1 = ord(i) - 65
                j = self.key_phrase[key_index]
                j1 = ord(j) - 97
                if i1 - j1 < 0:
                    i1 = i1 - j1 + 26
                else:
                    i1 = i1 - j1
                i1 = chr(i1 + 65)
                self.plaintext.append(i1)
            elif i.islower():
                i1 = ord(i) - 97
                j = self.key_phrase[key_index]
                j1 = ord(j) - 97
                if i1 - j1 < 0:
                    i1 = i1 - j1 + 26
                else:
                    i1 = i1 - j1
                i1 = chr(i1 + 97)
                self.plaintext.append(i1)
            else:
                self.plaintext.append(i)
            key_index += 1
            if key_index == len(self.key_phrase):
                key_index = 0

        for k in self.plaintext:
            print(k, end="")
        print("\n")
        return self.plaintext


class HillCipher:
    """
    This class is used to encode and decode Hill Cipher
    """

    def __init__(self, a, b, c, d, ciphertext, plaintext):
        self.a = a % 26
        self.b = b % 26
        self.c = c % 26
        self.d = d % 26
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.plaintext = []
        self.ciphertext = []

    def add_x(self):
        num = 0
        for i in self.plaintext_input:
            if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
                num += 1
        if num % 2 != 0:
            self.plaintext_input = self.plaintext_input + "x"
            return
        else:
            return

    def encode(self):
        self.add_x()
        i = 0
        j = 0
        while i < len(self.plaintext_input):
            other = []
            if i == len(self.plaintext_input) - 1:
                self.ciphertext.append(self.plaintext_input[i])
                break
            for j in range(i + 1, len(self.plaintext_input)):
                if self.plaintext_input[i].isupper():
                    i1 = ord(self.plaintext_input[i]) - 65

                    if self.plaintext_input[j].isupper():
                        j1 = ord(self.plaintext_input[j]) - 65
                        ex = (self.a * i1 + self.b * j1) % 26
                        ex1 = chr(ex + 65)
                        self.ciphertext.append(ex1)
                        for k in other:
                            self.ciphertext.append(k)
                        ey = (self.c * i1 + self.d * j1) % 26
                        ey1 = chr(ey + 65)
                        self.ciphertext.append(ey1)
                        break
                    elif self.plaintext_input[j].islower():
                        j1 = ord(self.plaintext_input[j]) - 97
                        ex = (self.a * i1 + self.b * j1) % 26
                        ex1 = chr(ex + 65)
                        self.ciphertext.append(ex1)
                        for k in other:
                            self.ciphertext.append(k)
                        ey = (self.c * i1 + self.d * j1) % 26
                        ey1 = chr(ey + 97)
                        self.ciphertext.append(ey1)
                        break
                    else:
                        other.append(self.plaintext_input[j])
                        continue

                elif self.plaintext_input[i].islower():
                    i1 = ord(self.plaintext_input[i]) - 97

                    if self.plaintext_input[j].isupper():
                        j1 = ord(self.plaintext_input[j]) - 65
                        ex = (self.a * i1 + self.b * j1) % 26
                        ex1 = chr(ex + 97)
                        self.ciphertext.append(ex1)
                        for k in other:
                            self.ciphertext.append(k)
                        ey = (self.c * i1 + self.d * j1) % 26
                        ey1 = chr(ey + 65)
                        self.ciphertext.append(ey1)
                        break
                    elif self.plaintext_input[j].islower():
                        j1 = ord(self.plaintext_input[j]) - 97
                        ex = (self.a * i1 + self.b * j1) % 26
                        ex1 = chr(ex + 97)
                        self.ciphertext.append(ex1)
                        for k in other:
                            self.ciphertext.append(k)
                        ey = (self.c * i1 + self.d * j1) % 26
                        ey1 = chr(ey + 97)
                        self.ciphertext.append(ey1)
                        break
                    else:
                        other.append(self.plaintext_input[j])
                        continue

                else:
                    self.ciphertext.append(self.plaintext_input[i])
                    j -= 1
                    break
            i = j + 1

        for k in self.ciphertext:
            print(k, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        i = 0
        j = 0
        f = 1
        p = (self.a * self.d - self.b * self.c) % 26
        while (p * f) % 26 != 1:
            f += 1

        while i < len(self.ciphertext_input):
            other = []
            if i == len(self.ciphertext_input) - 1:
                self.plaintext.append(self.ciphertext_input[i])
                break
            for j in range(i + 1, len(self.ciphertext_input)):
                if self.ciphertext_input[i].isupper():
                    i1 = ord(self.ciphertext_input[i]) - 65

                    if self.ciphertext_input[j].isupper():
                        j1 = ord(self.ciphertext_input[j]) - 65
                        dx = (f * self.d * i1) - (f * self.b * j1)
                        while dx < 0:
                            dx += 26
                        dx = dx % 26
                        dx1 = chr(dx + 65)
                        self.plaintext.append(dx1)
                        for k in other:
                            self.plaintext.append(k)
                        dy = (-1 * f * self.c * i1) + (f * self.a * j1)
                        while dy < 0:
                            dy += 26
                        dy = dy % 26
                        dy1 = chr(dy + 65)
                        self.plaintext.append(dy1)
                        break

                    elif self.ciphertext_input[j].islower():
                        j1 = ord(self.ciphertext_input[j]) - 97
                        dx = (f * self.d * i1) - (f * self.b * j1)
                        while dx < 0:
                            dx += 26
                        dx = dx % 26
                        dx1 = chr(dx + 65)
                        self.plaintext.append(dx1)
                        for k in other:
                            self.plaintext.append(k)
                        dy = (-1 * f * self.c * i1) + (f * self.a * j1)
                        while dy < 0:
                            dy += 26
                        dy = dy % 26
                        dy1 = chr(dy + 97)
                        self.plaintext.append(dy1)
                        break
                    else:
                        other.append(self.ciphertext_input[j])
                        continue

                elif self.ciphertext_input[i].islower():
                    i1 = ord(self.ciphertext_input[i]) - 97

                    if self.ciphertext_input[j].isupper():
                        j1 = ord(self.ciphertext_input[j]) - 65
                        dx = (f * self.d * i1) - (f * self.b * j1)
                        while dx < 0:
                            dx += 26
                        dx = dx % 26
                        dx1 = chr(dx + 97)
                        self.plaintext.append(dx1)
                        for k in other:
                            self.plaintext.append(k)
                        dy = (-1 * f * self.c * i1) + (f * self.a * j1)
                        while dy < 0:
                            dy += 26
                        dy = dy % 26
                        dy1 = chr(dy + 65)
                        self.plaintext.append(dy1)
                        break

                    elif self.ciphertext_input[j].islower():
                        j1 = ord(self.ciphertext_input[j]) - 97
                        dx = (f * self.d * i1) - (f * self.b * j1)
                        while dx < 0:
                            dx += 26
                        dx = dx % 26
                        dx1 = chr(dx + 97)
                        self.plaintext.append(dx1)
                        for k in other:
                            self.plaintext.append(k)
                        dy = (-1 * f * self.c * i1) + (f * self.a * j1)
                        while dy < 0:
                            dy += 26
                        dy = dy % 26
                        dy1 = chr(dy + 97)
                        self.plaintext.append(dy1)
                        break
                    else:
                        other.append(self.ciphertext_input[j])
                        continue

                else:
                    self.plaintext.append(self.ciphertext_input[i])
                    j -= 1
                    break
            i = j + 1

        for k in self.plaintext:
            print(k, end="")
        print("\n")
        return self.plaintext


class AutokeyCipher:
    def __init__(self, seed, ciphertext, plaintext):
        self.seed = seed
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        for i in self.plaintext_input:
            if i.isupper():
                i1 = ord(i) - 65
                j = (i1 + self.seed) % 26
                self.seed = i1
                j = chr(j + 65)
                self.ciphertext.append(j)
            elif i.islower():
                i1 = ord(i) - 97
                j = (i1 + self.seed) % 26
                self.seed = i1
                j = chr(j + 97)
                self.ciphertext.append(j)
            else:
                self.ciphertext.append(i)

        for k in self.ciphertext:
            print(k, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        for i in self.ciphertext_input:
            if i.isupper():
                i1 = ord(i) - 65
                j = (i1 - self.seed) % 26
                self.seed = j
                j = chr(j + 65)
                self.plaintext.append(j)
            elif i.islower():
                i1 = ord(i) - 97
                j = (i1 - self.seed) % 26
                self.seed = j
                j = chr(j + 97)
                self.plaintext.append(j)
            else:
                self.plaintext.append(i)

        for k in self.plaintext:
            print(k, end="")
        print("\n")
        return self.plaintext


class VernamCipher:
    """
    This class is used to encode and decode Vernam cipher. This cipher can only encode lower
    case letter without space. Upper case letters, numbers, space, and symbol won't be accepted
    as input plaintext. The key stream must be binary number which has exact 5 times length of
    the input plaintext. The input cipher text must be binary.
    """
    def __init__(self, key_stream, ciphertext, plaintext):
        self.key_stream = key_stream
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.plaintext = []
        self.ciphertext = []

    def encode(self):
        input_combine = ""
        for i in self.plaintext_input:
            i1 = ord(i) - 97
            i2 = bin(i1)[2:]
            i3 = ""
            if len(i2) < 5:
                for j in range(5 - len(i2)):
                    i3 += "0"
                i3 += i2
                input_combine += i3
            else:
                input_combine += i2
        for x in range(len(input_combine)):
            if input_combine[x] == self.key_stream[x]:
                self.ciphertext.append("0")
            else:
                self.ciphertext.append("1")
        for k in self.ciphertext:
            print(k, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        after_xor = ""
        for x in range(len(self.ciphertext_input)):
            if self.key_stream[x] == self.ciphertext_input[x]:
                after_xor += "0"
            else:
                after_xor += "1"
        for i in range(0, len(after_xor), 5):
            result1 = after_xor[i:i+5]
            num1 = 0
            for j in range(len(result1)):
                num1 += int(result1[j]) * (2 ** (4-j))
            result2 = chr(num1 + 97)
            self.plaintext.append(result2)

        for k in self.plaintext:
            print(k, end="")
        print("\n")
        return self.plaintext


class RSA:
    """
    This class is used to encode and decode the RSA Cryptosystem. This cipher can encode
    all 128 elements in ASCII table. The value of p, q and e must be manually chosen. The
    decode of this cipher only support reading from input_text.txt file.
    """
    def __init__(self, m, n, e, ciphertext, plaintext):
        self.m = m
        self.n = n
        self.e = e
        self.ciphertext_input = ciphertext
        self.plaintext_input = plaintext
        self.ciphertext = []
        self.plaintext = []

    def encode(self):
        for i in self.plaintext_input:
            i1 = ord(i)
            i1 = (i1 ** self.e) % self.m
            self.ciphertext.append(str(i1))
        for k in self.ciphertext:
            print(k, end="")
        print("\n")
        return self.ciphertext

    def decode(self):
        d = None
        num1 = 1
        while True:
            if (num1 * self.e) % self.n == 1:
                d = num1
                break
            else:
                num1 += 1
                continue
        for i in self.ciphertext_input:
            i1 = int(i)
            i1 = (i1 ** d) % self.m
            i1 = chr(i1)
            self.plaintext.append(str(i1))

        for k in self.plaintext:
            print(k, end="")
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
            2. LinearCodes\n\
            3. Vigenere Cipher\n\
            4. Hill Cipher\n\
            5. Autokey Cipher\n\
            6. Vernam Cipher\n\
            7. RSA Cryptosystem\n")
        if UniversalInput().check_mode_input(mode1, ["1", "2", "3", "4", "5", "6", "7"]):
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
            2. Read file \"input_text.txt\" at local path\n\
The RSA Cryptosystem decode doesn't support manual input.\n")
        print()
        if UniversalInput().check_mode_input(mode3, ["1", "2"]):
            break
        else:
            continue

    if mode1 == "1":
        if mode2 == "1":
            input_list = UniversalInput("plain text").generalized_caesar_codes_input(mode3)
            gcc = GeneralizedCaesarCodes(input_list[0], 0, input_list[1])
            ReadAndWrite().file_write(''.join(gcc.encode()))
            return

        elif mode2 == "2":
            input_list = UniversalInput("cipher text").generalized_caesar_codes_input(mode3)
            gcc = GeneralizedCaesarCodes(input_list[0], input_list[1], 0)
            ReadAndWrite().file_write(''.join(gcc.decode()))
            return

    elif mode1 == "2":
        if mode2 == "1":
            input_list = UniversalInput("plain text").linear_codes_input(mode3)
            lc = LinearCodes(input_list[0], input_list[1], 0, input_list[2])
            ReadAndWrite().file_write(''.join(lc.encode()))
            return

        elif mode2 == "2":
            input_list = UniversalInput("cipher text").linear_codes_input(mode3)
            lc = LinearCodes(input_list[0], input_list[1], input_list[2], 0)
            ReadAndWrite().file_write(''.join(lc.decode()))
            return

    elif mode1 == "3":
        if mode2 == "1":
            input_list = UniversalInput("plain text").vigenere_cipher_input(mode3)
            vc = VigenereCipher(input_list[0], 0, input_list[1])
            ReadAndWrite().file_write(''.join(vc.encode()))
            return
        elif mode2 == "2":
            input_list = UniversalInput("cipher text").vigenere_cipher_input(mode3)
            vc = VigenereCipher(input_list[0], input_list[1], 1)
            ReadAndWrite().file_write(''.join(vc.decode()))
            return

    elif mode1 == "4":
        if mode2 == "1":
            input_list = UniversalInput("plain text").hill_cipher_input(mode3)
            hc = HillCipher(input_list[0], input_list[1], input_list[2], input_list[3], 0, input_list[4])
            ReadAndWrite().file_write(''.join(hc.encode()))
            return
        elif mode2 == "2":
            input_list = UniversalInput("cipher text").hill_cipher_input(mode3)
            hc = HillCipher(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4], 0)
            ReadAndWrite().file_write(''.join(hc.decode()))
            return

    elif mode1 == "5":
        if mode2 == "1":
            input_list = UniversalInput("plain text").autokey_cipher_input(mode3)
            ac = AutokeyCipher(input_list[0], 0, input_list[1])
            ReadAndWrite().file_write(''.join(ac.encode()))
            return
        elif mode2 == "2":
            input_list = UniversalInput("cipher text").autokey_cipher_input(mode3)
            ac = AutokeyCipher(input_list[0], input_list[1], 0)
            ReadAndWrite().file_write(''.join(ac.decode()))
            return

    elif mode1 == "6":
        if mode2 == "1":
            input_list = UniversalInput("plain text").vernam_cipher_input(mode3, "plain text")
            vmc = VernamCipher(input_list[0], 0, input_list[1])
            ReadAndWrite().file_write(''.join(vmc.encode()))
            return
        elif mode2 == "2":
            input_list = UniversalInput("cipher text").vernam_cipher_input(mode3, "cipher text")
            vmc = VernamCipher(input_list[0], input_list[1], 0)
            ReadAndWrite().file_write(''.join(vmc.decode()))
            return

    elif mode1 == "7":
        if mode2 == "1":
            input_list = UniversalInput("plain text").rsa_input(mode2, mode3)
            rsa = RSA(input_list[0], input_list[1], input_list[2], 0, input_list[3])
            ReadAndWrite().rsa_file_write(mode2, rsa.encode())
            return
        elif mode2 == "2":
            input_list = UniversalInput("cipher text").rsa_input(mode2, "2")
            rsa = RSA(input_list[0], input_list[1], input_list[2], input_list[3], 0)
            ReadAndWrite().rsa_file_write(mode2, ''.join(rsa.decode()))
            return


def main():
    while True:
        mode()


if __name__ == '__main__':
    main()
