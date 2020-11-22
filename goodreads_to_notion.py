
# import sys
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/GoodReadsScraper')

from goodsreads_scraper.Books import Books
from notion.client import NotionClient
import argparse
import sys


def goodreads_book_to_notion(book_id, notion_token, notion_page_url):
    # description = "Run notion-py client smoke tests"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("--book", dest="book_id", help="Goodreads Book ID", required=True, type=int)
    # args = parser.parse_args()
    #
    # book_id = args.book_id
    # if not book_id:
    #     print(
    #         "Must pass book id"
    #     )
    #     sys.exit(1)

    client = NotionClient(token_v2=notion_token)

    cv = client.get_collection_view(notion_page_url)

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
        row.Cover = book["Cover"]
    except AttributeError:
        row = cv.collection.add_row()
        row.title = book["Title"]
        row.Author = book["Author"]
        row.Book_Id = book["Book Id"]
        row.Exclusive_Shelf = "to-read"
        row.Number_of_Pages = book["Number of Pages"]
        row.Cover = book["Cover"]

    print(row)
