# Add Goodreads Books to your Notion Dashboard

The function adds Goodreads books using the GoodReads ID to Notion.

The unofficial wrapper for Notion is being used to provide the collection.

## Example: Adding a new book to Notion

```

goodreads_book_to_notion(book_id, notion_token, notion_page_url)

```

Get the Notion Token from your browser cookies for notion.so

Copy the Notion view URL from your browser


### Make sure that Notion Table view has the following fields of the same name

- title
- Book Id
- Author
- Cover
- Number of Pages
- Exclusive Shelf

Exclusive Shelf is the shelf that records reading status. to-read, currently-reading and read.
Exclusive Shelf by default is to-read as there is no authentication with GoodReads yet.

Except Cover, all fields are from the GoodReads export file.

## Future TODO:

Use Goodreads API to get all real time status of books and add to Notion.