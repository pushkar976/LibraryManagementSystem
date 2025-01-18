from flask import Blueprint, request, jsonify
from . import db
from .models import Book

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'}), 201


@api_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year
        } for book in books
    ]
    return jsonify(result), 200


@api_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        result = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year
        }
        return jsonify(result), 200
    else:
        return jsonify({"error": "Book not found"}), 404
