from googletrans import Translator, constants

def google_translate(word):
    translator = Translator()
    translation = translator.translate(word, dest="uz")
    return f"{translation.word}"

# print(google_translate("Привет"))

