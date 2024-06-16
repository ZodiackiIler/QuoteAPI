## QuoteAPI

QuoteAPI is a simple and efficient RESTful API for managing quotes, built using FastAPI. It allows users to fetch random quotes, add new quotes, update existing quotes, and delete quotes. The quotes are stored in an SQLite3 database, and the API ensures secure modifications through token-based authentication.

### Features

- **Fetch Random Quote**: Retrieve a random quote from the database.
- **Add New Quote**: Securely add a new quote to the database using a secret token.
- **Update Existing Quote**: Update the details of an existing quote with token authentication.
- **Delete Quote**: Delete a quote from the database with token authentication.
- **Documentation**: Auto-generated documentation available through Swagger UI and ReDoc.

### Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **SQLite3**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **python-dotenv**: Reads key-value pairs from a `.env` file and can set them as environment variables.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ZodiackiIler/QuoteAPI.git
   cd QuoteAPI
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python init_db.py
   ```

5. **Create a `.env` file and add your secret token**:
   ```plaintext
   SECRET_TOKEN=your_secret_token
   ```

### Usage

1. **Run the API server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
