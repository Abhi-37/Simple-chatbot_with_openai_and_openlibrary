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
    info = {
        "title": book.get("title", "Unknown Title"),
        "authors": ", ".join(book.get("author_name", ["Unknown Author"])),
        "publish_year": book.get("first_publish_year", "Unknown Year"),
        "publishers": ", ".join(book.get("publisher", ["Unknown Publisher"])),
        "isbn": ", ".join(book.get("isbn", ["Unknown ISBN"])),
        "edition_count": book.get("edition_count", "Unknown Edition Count"),
        "language": ", ".join(book.get("language", ["Unknown Language"])),
        "cover_url": f"http://covers.openlibrary.org/b/id/{book.get('cover_i', 'unknown')}-L.jpg",
        "first_sentence": book.get("first_sentence", ["Unknown First Sentence"])[0] if book.get("first_sentence") else "Unknown First Sentence"
    }
    return info

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
                    info = get_book_info(book)
                    print(f"Title: {info['title']}")
                    print(f"Author(s): {info['authors']}")
                    print(f"First Publish Year: {info['publish_year']}")
                    print(f"Publisher(s): {info['publishers']}")
                    print(f"ISBN: {info['isbn']}")
                    print(f"Edition Count: {info['edition_count']}")
                    print(f"Language: {info['language']}")
                    print(f"Cover URL: {info['cover_url']}")
                    print(f"First Sentence: {info['first_sentence']}")
                    print("------------------------")
            else:
                print("No books found.")

if __name__ == "__main__":
    main()
