# init_db.py
import sqlite3
import random

def create_table():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            author TEXT,
            theme TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_random_quote():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM quotes')
    count = cursor.fetchone()[0]

    if count == 0:
        conn.close()
        return None

    random_id = random.randint(1, count)
    cursor.execute('SELECT * FROM quotes WHERE id = ?', (random_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "text": row[1],
            "author": row[2] if row[2] else None,
            "theme": row[3] if row[3] else None
        }
    else:
        return None


def add_quote_to_db(text, author, theme):
    try:
        conn = sqlite3.connect('quotes.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO quotes (text, author, theme) VALUES (?, ?, ?)
        ''', (text, author, theme))
        conn.commit()
        conn.close()
        return {"message": "Quote added successfully"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"Internal server error: {e}"}

def update_quote_in_db(quote_id, text, author, theme):
    try:
        conn = sqlite3.connect('quotes.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE quotes SET text = ?, author = ?, theme = ? WHERE id = ?
        ''', (text, author, theme, quote_id))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            return {"error": "Quote not found"}
        return {"message": "Quote updated successfully"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"Internal server error: {e}"}

def delete_quote_from_db(quote_id):
    try:
        conn = sqlite3.connect('quotes.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM quotes WHERE id = ?
        ''', (quote_id,))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            return {"error": "Quote not found"}
        return {"message": "Quote deleted successfully"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"Internal server error: {e}"}


create_table()
