
# import sys
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/GoodReadsScraper')

from goodsreads_scraper.Books import Books
from notion.client import NotionClient
import argparse
import sys

if __name__ == "__main__":
    description = "Run notion-py client smoke tests"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--book", dest="book_id", help="Goodreads Book ID", required=True, type=int)
    args = parser.parse_args()


    book_id = args.book_id
    if not book_id:
        print(
            "Must pass book id"
        )
        sys.exit(1)

    client = NotionClient(token_v2="a46f9b8ce309ada8e9b67137354230dffcdeee3d19ec3ef417c299d31def7e8b5419991ef894b77bd47618d615fc2d1aebf1da4e262370b85407887b4ca8a396ce9b321745a4500c6245879993b1")

    cv = client.get_collection_view("https://www.notion.so/gauravshetty4/52d7820f75574d40b41b63cba842679c?v=551574aa4359418eb63a77d5223a3aff")

    goodreads = Books()
    book = goodreads.get_book_details(book_id)


    # Add a new record
    try:
        row = cv.collection.add_row()
        row.title = book["Title"]
        row.Author = book["Author"]
        row.Book_Id = book["Book Id"]
        row.Exclusive_Shelf = "to-read"
        row.Number_of_Pages = book["Number of Pages"]
    except AttributeError:
        row = cv.collection.add_row()
        row.title = book["Title"]
        row.Author = book["Author"]
        row.Book_Id = book["Book Id"]
        row.Exclusive_Shelf = "to-read"
        row.Number_of_Pages = book["Number of Pages"]

    print(row)
