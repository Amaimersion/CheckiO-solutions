import copy

class Text(object):
    def __init__(self, data=None):
        self._data = data or {
            "text": "",
            "font": ""
        }

    def write(self, text):
        self._data["text"] += text

    def set_font(self, font):
        self._data["font"] = font

    def show(self):
        font = self._data["font"]
        font = "[{0}]".format(font) if font else ""

        return "{font}{text}{font}".format(font=font, text=self._data["text"])

    def get_data(self):
        return self._data

    def restore(self, data):
        self.__init__(data.get_data())

class SavedText(object):
    def __init__(self):
        self._data = []

    def save_text(self, data):
        self._data.append(copy.deepcopy(data))

    def get_version(self, version):
        return self._data[version]

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    print(text.show())
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")