# Simple-chatbot_with_openai_and_openlibrary

**Overview**
This Python program is a simple chatbot that allows users to search for books using the Open Library API. Users can enter the title of a book they're interested in, and the chatbot will retrieve information about the book, including its title, authors, publish year, and publishers.

**How It Works**
_**Search Functionality:**_ The chatbot prompts the user to enter a book title they want to search for. It then makes a request to the Open Library API using the provided title as the search query.

_**API Integration:**_ The program sends an HTTP request to the Open Library API endpoint https://openlibrary.org/search.json, passing the user's query as a parameter.

_**Processing Response:**_ The program receives a JSON response from the API, which contains information about the books matching the search query. It extracts relevant data such as the title, authors, publish year, and publishers from the response.

_**Display Results:**_ If books matching the query are found, the chatbot displays the information for each book, including its title, authors, publish year, and publishers. If no books are found, it notifies the user accordingly.

_**Repeat or Quit:**_ After displaying the search results, the chatbot prompts the user to enter another book title to search for. The user can continue searching for books or type 'quit' to exit the program.

**Running the Program**
**_To run the Book Search Chatbot:_**
Make sure you have Python installed on your system.
Download the provided Python script (book_search_chatbot.py) and save it in your desired directory.
Open a terminal or command prompt and navigate to the directory where the script is saved.
Run the script by executing the command: python book_search_chatbot.py
Follow the prompts to search for books by entering their titles. Type 'quit' to exit the program.

**Dependencies**
This program requires the requests library to make HTTP requests to the Open Library API. You can install it using pip:
Copy code
pip install requests

**Notes**
This chatbot uses the Open Library API to search for books. Since it doesn't require an API key, there's no need to sign up or obtain any credentials to use it.

The search functionality may not always return accurate results, depending on the quality and completeness of the data available in the Open Library database.
