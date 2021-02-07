
# import sys
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/GoodReadsScraper')

# from goodsreads_scraper.Books import Books
from notion.client import NotionClient
from bs4_goodreads import get_goodreads_book


def goodreads_book_to_notion(book_ids, notion_token, notion_page_url):
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

    books = []

    for book_id in book_ids:
        book = get_goodreads_book(book_id)
        books.append(book)
        # Add a new record
        try:
            row = cv.collection.add_row()
            row.title = book["title"]
            row.Author = book["author"]
            row.Book_Id = book_id
            row.Exclusive_Shelf = "to-read"
            row.Number_of_Pages = book["num_pages"]
            row.Cover = book["cover"]
        except AttributeError:
            row = cv.collection.add_row()
            row.title = book["title"]
            row.Author = book["author"]
            row.Book_Id = book_id
            row.Exclusive_Shelf = "to-read"
            row.Number_of_Pages = book["num_pages"]
            row.Cover = book["cover"]

    return books
