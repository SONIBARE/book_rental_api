from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

# Initialize Flask application
app = Flask(__name__)

# MongoDB configuration (Local Database)
app.config["MONGO_URI"] = "mongodb://localhost:27017/book_rental"
mongo = PyMongo(app)

# Reference to collections
books_collection = mongo.db.books
users_collection = mongo.db.users

# ------------------------
# 📌 API Endpoints
# ------------------------

# 📍 Add a new book (POST)
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book_id = books_collection.insert_one({
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "rental_details": {
            "date_rented": data["rental_details"]["date_rented"],
            "due_date": data["rental_details"]["due_date"]
        },
        "user_id": ObjectId(data["user_id"])
    }).inserted_id
    return jsonify({"message": "Book added", "book_id": str(book_id)}), 201

# 📍 Retrieve all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    books = []
    for book in books_collection.find({}, {"_id": 0}):  # Exclude MongoDB ObjectId
        books.append({
            "title": book.get("title", "Unknown Title"),
            "author": book.get("author", "Unknown Author"),
            "publication_year": book.get("year", "Unknown Year"),
            "rentalDetails": book.get("rental_details", {}),  # Get the full rental details
            "user_id": str(book.get("rental_details", {}).get("user_id", "N/A"))  # ✅ Extract user_id correctly
        })
    return jsonify(books)


# 📍 Update rental details (PUT)
@app.route('/books/<book_id>', methods=['PUT'])
def update_rental(book_id):
    data = request.json
    result = books_collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {"rental_details": data["rental_details"]}}
    )
    if result.matched_count:
        return jsonify({"message": "Rental details updated"}), 200
    return jsonify({"error": "Book not found"}), 404

# 📍 Delete a book (DELETE)
@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = books_collection.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count:
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))  # Exclude ObjectId for simplicity
    return jsonify(users)

# ------------------------
# 📌 Run the application
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
