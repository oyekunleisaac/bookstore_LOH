from flask import Blueprint, jsonify, request

api_bp = Blueprint('api_bp', __name__)

# This is a sample data for the books since I am not connecting a db, subsequent data from users saves in a cache when they add a book.
books = [
    {"id": 1, "title": "Book One", "author": "Isaac Dev"},
    {"id": 2, "title": "Book Two", "author": "Backend Developer"}
]

# API route to get all books including the new one I cathc from users
@api_bp.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API route to get a specific book by ID || For the search bar, it accepts only int
@api_bp.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# API route to add a new book
@api_bp.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201


# API route to update a book
@api_bp.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book.update(updated_book)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# API route to delete a book
@api_bp.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})
