from db import build_db
from server import app

if __name__ == "__main__":
    build_db()
    app.run("127.0.0.1", 5000)