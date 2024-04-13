# Step 1: Installing the required third-party libraries

# Easiest way to install external libraries in python is to use pip. pip is a package management system used to install and manage software packages written in Python. All you need to do is:
# pip install requests
# pip install html5lib
# pip install bs4

# Step 2: Accessing the HTML content from webpage 

import requests 
URL = "https://www.geeksforgeeks.org/data-structures/" 
r = requests.get(URL) 
print(r.content) 

# Let us try to understand this piece of code.

# First of all import the requests library.
# Then, specify the URL of the webpage you want to scrape.
# Send a HTTP request to the specified URL and save the response from server in a response object called r.
# Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.
# Note: Sometimes you may get error “Not accepted” so try adding a browser user agent like below. Find your user agent based on device and browser from here https://deviceatlas.com/blog/list-of-user-agent-strings


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link. 
r = requests.get(url=URL, headers=headers) 
print(r.content)

# Step 3: Parsing the HTML content 

#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.values.com/inspirational-quotes" 
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify()) 
