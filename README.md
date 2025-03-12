# book_rental_api

## Overview
This is a RESTful API for a book rental system built with Flask, MongoDB, and PyMongo. The API allows users to:
- Add new books with rental details
- Retrieve a list of all books (including rental details and user info)
- Update rental details for a book
- Delete a book from the system

## Technologies Used
- Python (Flask)
- MongoDB (NoSQL Database)
- PyMongo (MongoDB Client for Python)
- RESTful API principles

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- MongoDB (running locally or on MongoDB Atlas)
- Flask and required dependencies

### Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/book_rental_api.git
cd book_rental_api
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Set Up MongoDB
Ensure MongoDB is running locally or use a MongoDB Atlas cluster.
- If running locally, start MongoDB with:
  ```sh
  mongod --dbpath /path/to/data/db
  ```
- If using Atlas, update the connection URI in `app.py`:
  ```python
  client = pymongo.MongoClient("mongodb+srv://your_username:your_password@cluster.mongodb.net/?retryWrites=true&w=majority")
  ```

### Step 5: Run the Application
```sh
python app.py
```

## API Endpoints
| Method | Endpoint           | Description |
|--------|------------------|-------------|
| GET    | `/books`        | Get all books with rental details |
| POST   | `/books`        | Add a new book |
| PUT    | `/books/<book_id>` | Update rental details of a book |
| DELETE | `/books/<book_id>` | Delete a book |

## Example API Usage
### Add a New Book (POST `/books`)
```json
{
  "title": "MongoDB for Beginners",
  "author": "John Doe",
  "year": 2023,
  "rental_details": {
    "date_rented": "2025-03-10",
    "due_date": "2025-03-20",
    "user_id": "M12345"
  }
}
```

### Retrieve All Books (GET `/books`)
```json
[
  {
    "title": "MongoDB for Beginners",
    "author": "John Doe",
    "publication_year": 2023,
    "rentalDetails": {
      "date_rented": "2025-03-10",
      "due_date": "2025-03-20"
    },
    "user_id": "M12345"
  }
]
```

### Update Rental Details (PUT `/books/<book_id>`)
```json
{
  "rental_details": {
    "date_rented": "2025-03-12",
    "due_date": "2025-03-25"
  }
}
```

### Delete a Book (DELETE `/books/<book_id>`)
```sh
curl -X DELETE http://127.0.0.1:5000/books/67d1478b960204a26db71236
```

## Deployment
To deploy this project:
- Use **Gunicorn** for production servers
- Deploy to **Heroku, AWS, or any cloud provider**

Example with Gunicorn:
```sh
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Contributions
Feel free to submit issues or fork the repository to add new features.

## License
MIT License
