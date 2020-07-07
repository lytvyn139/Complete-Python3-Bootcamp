#pip3 install pillow
from PIL import Image
mac = Image.open('example.jpg')
#mac.show() #will open image
print(mac.size)
print(mac.filename)
print(mac.format_description)

""" CROPPING IMAGE """
pencils = Image.open('pencils.jpg')
pencils.size #1950/1300
#pencils.show()

x = 0
y = 0
w = 1950 / 3
h = 1300 /10
pencils.crop((x,y,w,h))
#pencils.show()

mac.size
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac.crop((x,y,w,h))
#mac.show()

""" Copying and Pasting Images """
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))
mac.paste(im=computer,box=(796,0))
#mac.show()

""" Resizing """
h,w = mac.size
new_h = int(h/3)
new_w = int(w/3)

# Note this is not permanent change
# for permanent change, do a reassignment
# e.g. mac = mac.resize((100,100))
mac.resize((new_h,new_w))
mac.resize((3000,500))
#mac.show()

""" Rotating Images """ #not working
pencils.rotate(120)
pencils.show()


""" Transparency """ #not working
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
red.putalpha(128)
blue.putalpha(128)
blue.paste(red,box=(0,0),mask=red)
blue.show()