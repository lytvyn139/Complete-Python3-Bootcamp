# libs for scrapping
# pip3 install requests lxml bs4
import requests, bs4

#res = requests.get("https://medium.com/better-programming/javascript-unraveling-the-matrix-7327257652a9#1d02-e88f53842a59")
res = requests.get("http://www.example.com/")
soup = bs4.BeautifulSoup(res.text,"lxml") #lxml engine to parse

#All elements with the <div> tag
soup.select('div')
#The HTML element containing the id attribute of some_id
soup.select('#some_id')
#All the HTML elements with the CSS class named notice
soup.select('.notice')
#Any elements named <span> that are within an element named <div>
soup.select('div span')
#Any elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('div > span')

title_tag = soup.select('h1')[0].getText()
print(title_tag)

site_paragraphs = soup.select('p')[1].getText()
print(site_paragraphs)

print('*** Grace_Hopper ***')
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,"lxml") #lxml engine to parse
soup.select(".toctext")
for item in soup.select(".toctext"):
    z = item.text
    print(z)