class HackerLanguage(object):
    def __init__(self):
        super(HackerLanguage, self).__init__()
        self.message = ""

    def write(self, text):
        self.message += text

    def delete(self, number):
        self.message = self.message[0:len(self.message) - number]

    def send(self):
        return self._encrypt(self.message)

    def read(self, text):
        return self._decrypt(text)

    def _encrypt(self, text):
        output = ""

        for i in text:
            if (i.isalpha()):
                output += f"{ord(i):b}"
            elif (i.isspace()):
                output += "1000000"
            else:
                output += i

        return output

    def _decrypt(self, text):
        text = text[::-1]
        output = ""
        i = 0

        while (i != len(text)):
            if (len(text) - i < 7):
                output += text[i:]
                break

            code = text[i:i + 7]

            if (code == "1000000"[::-1]):
                output += " "
                i += 7
            else:
                try:
                    code = chr(int(code[::-1], 2))

                    if (code.isalpha()):
                        output += code

                    i += 7
                except Exception as e:
                    output += code[0]
                    i += 1

        return output[::-1]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    message_3 = HackerLanguage()
    message_3.write('Remember: 21.07.2018 at 11:11AM')
    message_3.delete(2)
    message_3.write('PM')

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_3.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'
    assert message_2.read("11001011101101110000111010011101100") == "email"
    assert message_3.read("10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101") == "Remember: 21.07.2018 at 11:11PM"
    print("Coding complete? Let's try tests!")
