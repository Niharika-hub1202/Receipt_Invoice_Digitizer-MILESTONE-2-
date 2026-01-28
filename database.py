import sqlite3

def get_connection():
    return sqlite3.connect("receipts.db", check_same_thread=False)

def create_tables():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS receipts (
        invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor TEXT,
        purchase_date TEXT,
        purchase_time TEXT,
        total_amount INTEGER,
        payment_method TEXT,
        deleted INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
