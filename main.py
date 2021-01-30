from goodreads_to_notion import goodreads_book_to_notion
from typing import Optional
from bs4_goodreads import get_read_book_list
from fastapi import FastAPI

app = FastAPI()

#
# @app.get("/add-to-notion/{book_id}")
# def add_to_notion(book_id):
#     book = goodreads_book_to_notion(int(book_id), notion_token, notion_page_url)
#     return book


@app.get("/get-books/{book_list_id}")
def add_to_notion(book_list_id):
    books = get_read_book_list(book_list_id)
    return books


