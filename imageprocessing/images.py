from PIL import Image, ImageFilter

img = Image.open('./4.5 pikachu.jpg.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
crooked = filtered_img.rotate(90)
crooked.save('crooked.png', 'png')


img = Image.open('./4.5 pikachu.jpg.jpg')
filtered_img = img.convert('L')
filtered_img.save('greypika.png', 'png')
filtered_img.show()

img = Image.open('./4.2 bulbasaur.jpg.jpg')
filtered_img = img.convert('L')
resize = filtered_img.resize((100, 100))
resize.save('tiny.png', 'png')
