import requests
from bs4 import BeautifulSoup
import math


def get_read_book_list(book_list_id):
    url = f"https://www.goodreads.com/review/list/{book_list_id}?page=1&shelf=read&utf8=✓&sort=date_read&order=d"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    books = soup.find("table", attrs={"id": "books"})
    books = books.tbody.find_all("tr")

    number_of_books_read = int(soup.find('span', attrs={"class": "h1Shelf"}).span.text.lstrip('(').rstrip(')'))
    number_of_pages = math.ceil(number_of_books_read/30)

    all_books = {
        "books_read_count": number_of_books_read,
        "books": []
    }

    for page in range(1, number_of_pages):
        url = f"https://www.goodreads.com/review/list/{book_list_id}?page={page}&shelf=read&utf8=✓&sort=date_read&order=d"

        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")

        books = soup.find("table", attrs={"id": "books"})
        books = books.tbody.find_all("tr")

        for book in books:
            rows = {}
            for td in book.find_all("td"):
                # remove any newlines and extra spaces from left and right
                row_name = td.label.text.replace('\n', ' ').strip()
                if row_name == 'cover':
                    rows['cover'] = td.img['src'].replace('._SY75_', '')
                    rows['book_id'] = td.div.div['data-resource-id']
                elif row_name == 'shelves':
                    print(td.div.a)
                elif row_name == 'author':
                    rows[row_name] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'title':
                    rows[row_name] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'isbn':
                    rows[row_name] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'isbn13':
                    rows[row_name] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'num pages':
                    rows['pages'] = td.div.text.replace('\n        pp', '').strip()
                elif row_name == 'avg rating':
                    rows['avg_rating'] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'num ratings':
                    rows['num_of_ratings'] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'my rating':
                    rows['my_rating'] = td.div.div['data-rating']
                elif row_name == 'date read':
                    rows['date_read'] = td.div.text.replace('\n', ' ').strip()
                elif row_name == 'date added':
                    rows['date_added'] = td.div.text.replace('\n', ' ').strip()

            all_books['books'].append(rows.copy())

    return all_books


def get_goodreads_book(book_id):
    url = f"https://www.goodreads.com/book/show/{book_id}"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    #
    # row.title = book["Title"]
    # row.Author = book["Author"]
    # row.Book_Id = book["Book Id"]
    # row.Exclusive_Shelf = "to-read"
    # row.Number_of_Pages = book["Number of Pages"]
    # row.Cover = book["Cover"]
    book = {}

    book['title'] = soup.find("h1", attrs={"id": "bookTitle"}).text.replace('\n', ' ').strip()
    book['author'] = soup.find("a", attrs={"class": "authorName"}).span.text.replace('\n', ' ').strip()
    book['shelf'] = 'to-read'
    book['num_pages'] = int(soup.find("div", attrs={"id": "details"})
                            .div.find("span", attrs={"itemprop": "numberOfPages"}).text.replace(' pages', ''))
    book['cover'] = soup.find("div", attrs={"class": "bookCoverPrimary"}).a.img['src']

    return book
