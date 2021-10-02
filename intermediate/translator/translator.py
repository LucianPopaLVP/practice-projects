from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./En-text', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(my_file)
        print(translation)
except FileNotFoundError as e:
    print('check your file path silly!!')