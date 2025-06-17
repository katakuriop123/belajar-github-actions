import sqlite3
from flask import request

def unsafe_query():
    conn = sqlite3.connect("users.db")
    username = request.args.get("username")
    query = "SELECT * FROM users WHERE name = '%s'" % username
    conn.execute(query)
