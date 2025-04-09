import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )''')
    # Resetting database for repeated testing
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET'])  # Only GET for easier injection via browser
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    # Print raw user input for debugging (dangerous!)
    print(f"[DEBUG] Raw input -> username: {username}, password: {password}")

    # ⚠️ Fully vulnerable query construction
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    print(f"[DEBUG] Executing query: {query}")

    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    try:
        c.execute(query)
        result = c.fetchone()
    except Exception as e:
        result = None
        print(f"[ERROR] {e}")
        
    conn.close()

    if result:
        user, pw = result[1], result[2]  # username and password
        return f"✅ Login successful!<br>Username: <b>{user}</b><br>Password: <b>{pw}</b>"
    else:
        return "❌ Login failed!"

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
