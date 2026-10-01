from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)
# this response gave the complete html structure of the file

print("the response is loaded 👍")


soup = BeautifulSoup(response.text, 'html.parser')
#this html.parser says treat this text file as an html

# find tags
tags = soup.find("h1")
# this onyl finds the first tag
# to find all we will use this which results in list
tags_all = soup.find_all("li")

# soup.prettify we help us to see the html more beautifully

for titleall in soup.find_all("h3"):
    print("the title -----------------------")
    print(titleall.text)
    # this gives all the title names
print(" the next part 😒😒😒")
for title_in_class in soup.find_all("div",class_ = "col-sm-8 col-md-9"):
    #accesing the last element
    print(title_in_class.li.text.split()[-1])
# the title in specific div class and specific li tag
