
# libs for scrapping
# pip3 install requests lxml bs4
import requests, bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,"lxml") 

    # <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
    #     <span class="text" itemprop="text">“I have not failed. I&#39;ve just found 10,000 ways that won&#39;t work.”</span>
    #     <span>by <small class="author" itemprop="author">Thomas A. Edison</small>
    #     <a href="/author/Thomas-A-Edison">(about)</a>
    #     </span>
    #     <div class="tags">
    #         Tags:
    #         <meta class="keywords" itemprop="keywords" content="edison,failure,inspirational,paraphrased" /    > 
    #         <a class="tag" href="/tag/edison/page/1/">edison</a>
    #         <a class="tag" href="/tag/failure/page/1/">failure</a>
    #         <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
    #         <a class="tag" href="/tag/paraphrased/page/1/">paraphrased</a>
    #     </div>
    # </div>
z = soup.select('.author')[0].getText()
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print('\n',authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)


#print top 10 tags
len(soup.select('.tag-item')) #10

for item in soup.select('.tag-item'):
    print(item.text)



#TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

#Possible Solution #1 ( Assuming You Know Number of Pages
url = 'http://quotes.toscrape.com/page/'
authors = set()

for page in range(1,10):
    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
#print(authors)

#Possible Solution #2 ( Unknown Number of Pages, but knowledge of last page)
page_url = url+str(9999999)
# Obtain Request
res = requests.get(page_url)
# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')

page_still_valid = True
authors = set()
page = 1

while page_still_valid:
    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
    # Go to Next Page
    page += 1
print(authors)