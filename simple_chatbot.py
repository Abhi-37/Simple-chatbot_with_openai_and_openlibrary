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
                    title = book.get("title", "Unknown Title")
                    author = ", ".join(book.get("author_name", ["Unknown Author"]))
                    print(f"Title: {title}")
                    print(f"Author(s): {author}")
                    print("------------------------")
            else:
                print("No books found.")

if __name__ == "__main__":
    main()
