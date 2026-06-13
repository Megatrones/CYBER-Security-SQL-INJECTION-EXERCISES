from flask import Flask, request
import sqlite3

app = Flask(__name__)

# إنشاء قاعدة بيانات وهمية
def init_db():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    conn.commit()
    conn.close()

init_db()

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # الثغرة هنا: دمج مباشر للنصوص
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    return "Login Successful!" if user else "Login Failed!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
