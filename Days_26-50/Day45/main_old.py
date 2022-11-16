from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title) #<title>Angela's Personal Site</title>
# print(soup.title.string) #Angela's Personal Site
# print(soup.title.name) #title
# print(soup.prettify()) #the whole html content

all_li_tags = soup.find_all(name="a")

# for tag in all_li_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
