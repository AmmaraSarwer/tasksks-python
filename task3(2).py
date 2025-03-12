def search_by_author(inventory, author_name):
    """
    Search for books written by a specific author in the inventory.
    
    :param inventory: Dictionary with ISBN as keys and book details as values
    :param author_name: The author's name to search for
    :return: List of tuples containing (ISBN, title) of matching books
    """
    return [(isbn, details["title"]) for isbn, details in inventory.items() if details.get("author") == author_name]

# Example inventory dictionary
inventory = {
    "978-0-141-03659-3": {"title": "Book One", "author": "William L. Shirer"},
    "978-1-4767-8566-5": {"title": "Book Two", "author": "Ron Chernow"},
    "978-1-250-13559-2": {"title": "Another Book", "author": "Erik Larson"}
}

# Example usage
author_to_search = "John Doe"
matching_books = search_by_author(inventory, author_to_search)
print(matching_books)
