from db import build_db
from server import app

if __name__ == "__main__":
    build_db()
    app.run(port=5000, threaded=True, host=("0.0.0.0"))