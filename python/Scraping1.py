domain = "http://walshbr.com/"
pages = ["about", "blog", "pedagogy", "projects", "cv"]
urls = []
for page in pages:
    # print(domain + page)
    url = domain + page
    urls.append(url)

print(urls)
