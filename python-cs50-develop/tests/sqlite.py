import sys

sys.path.insert(0, "../src")

from cs50 import SQL

db = SQL("sqlite:///sqlite.db")
db.execute("SELECT 1")
