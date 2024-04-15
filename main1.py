# A really nice thing about the BeautifulSoup library is that it is built on the top of the HTML parsing libraries like html5lib, lxml, html.parser, etc. So  BeautifulSoup object and specify the parser library can be created at the same time. In the example above,

soup = BeautifulSoup(r.content, 'html5lib')

# We create a BeautifulSoup object by passing two arguments:

# r.content : It is the raw HTML content.
# html5lib : Specifying the HTML parser we want to use.
# Now soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content. Step 4: Searching and navigating through the parse tree Now, we would like to extract some useful data from the HTML content. The soup object contains all the data in the nested structure which could be programmatically extracted. In our example, we are scraping a webpage consisting of some quotes. So, we would like to create a program to save those quotes (and all relevant information about them). 

#Python program to scrape website and save quotes from website 

import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "http://www.values.com/inspirational-quotes" 
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib') 
   
quotes=[]  # a list to store quotes 
   
table = soup.find('div', attrs = {'id':'all_quotes'})  
   
for row in table.findAll('div', 
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt'].split(" #")[0] 
    quote['author'] = row.img['alt'].split(" #")[1] 
    quotes.append(quote) 
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)
