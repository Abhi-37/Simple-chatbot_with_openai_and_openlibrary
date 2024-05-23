import openai
import requests

def search_books(query):
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print("Failed to fetch data from Open Library API")
        return []

def get_book_info(book):
    title = book.get("title", "Unknown Title")
    authors = ", ".join(book.get("author_name", ["Unknown Author"]))
    publish_year = book.get("first_publish_year", "Unknown")
    publishers = ", ".join(book.get("publisher", ["Unknown Publisher"]))
    return {
        "title": title,
        "authors": authors,
        "publish_year": publish_year,
        "publishers": publishers
    }

def main():
    print("Welcome to the Book Search Chatbot!")
    while True:
        query = input("Enter a book title to search (or 'quit' to exit): ")
        if query.lower() == "quit":
            print("Goodbye!")
            break
        else:
            books = search_books(query)
            if books:
                print(f"Found {len(books)} books:")
                for book in books:
                    book_info = get_book_info(book)
                    print("Title:", book_info["title"])
                    print("Authors:", book_info["authors"])
                    print("Publish Year:", book_info["publish_year"])
                    print("Publishers:", book_info["publishers"])
                    print("------------------------")
            else:
                print("No books found.")

if __name__ == "__main__":
    main()

