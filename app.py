from flask import Flask
from routes.user_routes import user_bp
from database.db import init_db

app = Flask(__name__)
app.register_blueprint(user_bp)

init_db()

if __name__ == "__main__":
    app.run(debug=True)