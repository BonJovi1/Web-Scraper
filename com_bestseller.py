from bs4 import BeautifulSoup
from requests import get
import csv

names = []
authors = []
prices = []
average = []
number = []
urls = []

na = "Not Available"


def Do_It(url):

    response = get(url)

    html = BeautifulSoup(response.text, 'html.parser')
    books = html.find_all('div', class_='zg_itemImmersion')

    for book in books:

        name = book.find('div', class_='p13n-sc-truncate p13n-sc-line-clamp-1')
        try:
            names.append(name.text)
        except BaseException:
            names.append(na)

        url = book.find('a', class_='a-link-normal')
        try:
            urls.append("https://www.amazon.com/" + url['href'])
        except BaseException:
            urls.append(na)

        author = book.find('div', class_='a-row a-size-small')
        try:
            authors.append(author.text)
        except BaseException:
            authors.append(na)

        price = book.find('span', class_='p13n-sc-price')
        try:
            prices.append(price.text)
        except BaseException:
            prices.append(na)

        numberofratings = book.find('a', class_='a-size-small a-link-normal')
        try:
            number.append(numberofratings.text)
        except BaseException:
            number.append(na)

        averagerating = book.find('div', class_='a-icon-row a-spacing-none')
        try:
            averagerating = averagerating.find('a', class_='a-link-normal')
            try:
                average.append(averagerating['title'])
            except BaseException:
                average.append(na)
        except BaseException:
            average.append(na)


Do_It("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/")
Do_It("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_2?_encoding=UTF8&pg=2")
Do_It("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_3?_encoding=UTF8&pg=3")
Do_It("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_4?_encoding=UTF8&pg=4")
Do_It("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_5?_encoding=UTF8&pg=5")

final = []
final.append(["Name", "URL", "Author", "Price",
              "Number of Ratings", "Average Rating"])

for i in range(100):
    final.append([names[i].strip(),
                  urls[i].strip(),
                  authors[i].strip(),
                  prices[i].strip(),
                  number[i].strip(),
                  average[i].strip()])

myfile = open("./output/com_book.csv", "w")

with myfile:
    writer = csv.writer(myfile, delimiter=";")
    writer.writerows(final)
