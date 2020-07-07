# http://books.toscrape.com/

# libs for scrapping
# pip3 install requests lxml bs4
import requests, bs4

""" get all the books with rating 2 """
# <article class="product_pod">
# <div class="image_container">
# <a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
# </div>
# <p class="star-rating Two">
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# </p>
# <h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
# <div class="product_price">
# <p class="price_color">Â£51.77</p>
# <p class="instock availability">
# <i class="icon-ok"></i>
    
#         In stock
    
# </p>
# <form>
# <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
# </form>
# </div>
# </article>

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,"lxml") #lxml engine to parse
#print(len(soup.select('.product_pod'))) #20 books on the page
products = soup.select('.product_pod')
example = products[0]
print(example)
#print('star-rating Three' in str(example)) #true
z = example.select('.star-rating.Three') #must have . for space
print(z)

#or
print([] == example.select('.star-rating.Two')) #true

z = example.select('a')[1]['title']
print(z)


""" Looping thru """
two_star_titles = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)