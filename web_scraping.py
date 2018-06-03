'''
CLASS: Web Scraping with Beautiful Soup

What is web scraping?
- Extracting information from websites (simulates a human copying and pasting)
- Based on finding patterns in website code (usually HTML)

What are best practices for web scraping?
- Scraping too many pages too fast can get your IP address blocked
- Pay attention to the robots exclusion standard (robots.txt)
- Let's look at http://www.imdb.com/robots.txt

What is HTML?
- Code interpreted by a web browser to produce ("render") a web page
- Let's look at example.html
- Tags are opened and closed
- Tags have optional attributes

How to view HTML code:
- To view the entire page: "View Source" or "View Page Source" or "Show Page Source"
- To view a specific part: "Inspect Element"
- Safari users: Safari menu, Preferences, Advanced, Show Develop menu in menu bar
- Let's inspect example.html
'''

# read the HTML code for a web page and save as a string
import requests

with open('example.html', 'r') as f:
    html = f.read()

# convert HTML into a structured Soup object
from bs4 import BeautifulSoup
b = BeautifulSoup(html)

# print out the object
print(b)

# 'find' method returns the first matching Tag (and everything inside of it)
b.find('title')

# Tags allow you to access the 'inside text'
b.find('title').text

# Tags also allow you to access their attributes
d = {'key':'value'}
d['key']
b.find('h1')['id']

# 'find_all' method is useful for finding all matching Tags
paragraphs = b.find_all('p')
type(paragraphs)

# ResultSets can be sliced like lists
b.find_all('p')[1].text
b.find_all('p')[1:3]
b.find_all('p')[-1]

# iterate over a ResultSet
for item in b.find_all('p'):
    print(item)

for item in b.find_all('p'):
    print(item.text)
    print()

for item in b.find_all('p'):
    try:
        print(item['id'])
        print()
    except KeyError:
        pass


# limit search by Tag attribute
b.find('p', attrs={'id':'scraping'})

# limit search to specific sections

#traverse the hierarchy
b.find('body').find('h1')

'''
EXERCISE ONE
'''

# find the 'h2' tag and then print its text
b.find('h2')
b.find('h2').text

# find the 'p' tag with an 'id' value of 'feedback' and then print its text
b.find('p', attrs={'id':'feedback'}).text

# find the first 'p' tag and then print the value of the 'id' attribute
b.find_all('p')[1]['id']
b.find_all('p')[1]['class']

# print the text of all four li tags

for item in b.find_all('li'):
    print(item)

# print the text of only the API resources

results = b.find(name='ul', attrs={'id':'api'}).find_all(name='li')
for tag in results:
    print(tag.text)


'''
Scraping the IMDb website
'''

import requests

# get the HTML from the Shawshank Redemption page
r = requests.get('http://www.imdb.com/title/tt0111161/')

# convert HTML into Soup
b = BeautifulSoup(r.text)
print(b)

# run this code if you have encoding errors
import sys
sys.setdefaultencoding('utf8')

# get the title
b.find('title')
<h1 itemprop="name" class="">The Shawshank Redemption&nbsp;<span id="titleYear">(<a href="/year/1994/?ref_=tt_ov_inf">1994</a>)</span>            </h1>
b.find(name='h1', attrs={'itemprop':'name'}).text

# get the star rating (as a float)
b.find('span', attrs={'itemprop':'ratingValue'}).text

'''
EXERCISE TWO
'''

# get the description

b.find(name='div', attrs={'class':'summary_text'}).text.strip()


# get the content rating

<div class="subtext">
                    <meta itemprop="contentRating" content="R">R
    <span class="ghost">|</span>                    <time itemprop="duration" datetime="PT142M">
                        2h 22min
                    </time>
    <span class="ghost">|</span>
<a href="/genre/Crime?ref_=tt_ov_inf"><span class="itemprop" itemprop="genre">Crime</span></a>, 
<a href="/genre/Drama?ref_=tt_ov_inf"><span class="itemprop" itemprop="genre">Drama</span></a>

    <span class="ghost">|</span>
<a href="/title/tt0111161/releaseinfo?ref_=tt_ov_inf" title="See more release dates">14 October 1994 (USA)
<meta itemprop="datePublished" content="1994-10-14">
</a>            </div>

b.find(name='meta', attrs={'class':'subtext'}).text
b.find(name='meta', attrs={'itemprop':'contentRating'})['content']

# get the duration in minutes (as an integer)



'''
BeautifulSoup Extra Material
'''

# read the example web page again
url = r'https://raw.githubusercontent.com/justmarkham/DAT7/master/data/example.html'
r = requests.get(url)

# convert to Soup
b = BeautifulSoup(r.text)

# these are equivalent
b.find(name='p')    # normal way
b.find('p')         # 'name' is the first argument
b.p                 # can also be accessed as an attribute of the object

# these are equivalent
b.find(name='p', attrs={'id':'scraping'})   # normal way
b.find('p', {'id':'scraping'})              # 'name' and 'attrs' are the first two arguments
b.find('p', id='scraping')                  # can write the attributes as arguments

# these are equivalent
b.find(name='p', attrs={'class':'topic'})   # normal way
b.find('p', class_='topic')                 # 'class' is special, so it needs a trailing underscore
b.find('p', 'topic')                        # if you don't name it, it's assumed to be the class

# these are equivalent
b.find_all(name='p')    # normal way
b.findAll(name='p')     # old function name from Beautiful Soup 3
b('p')                  # if you don't name the method, it's assumed to be find_all