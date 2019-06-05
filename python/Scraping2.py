# get the libraries we need.
import nltk
from bs4 import BeautifulSoup
from urllib import request
# store the url we're using
url = "https://github.com/humanitiesprogramming/scraping-corpus"
# pull all the html from the url to see how it's structured
html = request.urlopen(url).read()

#took the URL and turned into a soup object
soup = BeautifulSoup(html, "lxml")
#adding .text gets you the words from the page
# print(soup.text)
our_text = soup.text
links = soup.find_all("a")[0:10]
#slice to see everything between the first and 2,000th character
print(our_text[0:2000])

#take out the new line entry to get rid of some of the junk
print(soup.text.replace("\n", "  "))
