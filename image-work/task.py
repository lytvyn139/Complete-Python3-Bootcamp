from PIL import Image
words = Image.open('word_matrix.png')
mask = Image.open("mask.png")
mask.size #(505, 251)
words.size #(1015, 559)
mask = mask.resize((1015,559))
mask.size #(1015, 559)
mask.putalpha(200)
mask.show()

words.paste(mask,(0,0),mask)
words.show()