# libs for scrapping
# pip3 install requests lxml bs4
import requests, bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,"lxml") #lxml engine to parse

image_info = soup.select('.thumbimage')
print(image_info)
print(f'*********** there are: {len(image_info)} images')
computer = image_info[0]
#print(computer['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
kasparov_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/440px-Kasparov_Magath_1985_Hamburg-2.png')

#save file
f = open('deep_blue.jpg','wb')
f.write(image_link.content)
f.close()

f = open('kasparov.jpg','wb')
f.write(kasparov_link.content)
f.close()



