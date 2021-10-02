from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('test', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError:
    print('check path!')