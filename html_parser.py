import requests, bs4

# For websites
# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(type(no_starch_soup))

# Finding an Element with the select() Method
exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))  # The tag object as a string
print(elems[0].getText())
print(elems[0].attrs)

# paragraphs
pElems = exampleSoup.select("p")
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

# Getting Data from an Element’s Attributes
spanElem = exampleSoup.select("span")[0]
print(str(spanElem))
print(spanElem.get("id"))
print(spanElem.attrs)
