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
# print(our_text[0:2000])
#
# #take out the new line entry to get rid of some of the junk
# print(soup.text.replace("\n", "  "))

#html pointer in the parentheses, which helps you say exactly what you want BS to pull
links_html = soup.select("td.content a")
this_link = links_html[0]
# print(links_html[0])
# print(this_link["href"])
urls = []
for link in links_html:
    #we're looping over links_html and this makes a URL list when we print
    # print(link["href"])
    # urls.append(link["href"])
    to_append = link["href"].replace("blob/", "")
    urls.append("https://raw.githubusercontent.com" + to_append)
    # ^adds the missing first part to each of the URLs

# print(urls)
# ^ this puts brackets around the list of URLs

test_url = urls[3]
corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace("\n", "")
    corpus_texts.append(text)
    # print("Scraping " + url)

print(len(corpus_texts))
print(len(corpus_texts[0]))

# assign the first text in the corpus to "this_text"
this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
# ^break this massive string up into individual words
print(process_this_text[0:20])
print(nltk.FreqDist(process_this_text).most_common(50))
# ^find the 50 most common words in the text
