from flask import Blueprint, request, jsonify
from database.db import get_db

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    conn = get_db()
    conn.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )
    conn.commit()
    return {"message": "User created"}, 201

@user_bp.route("/users", methods=["GET"])
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(u) for u in users])

@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
    return dict(user) if user else {"error": "Not found"}

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    return {"message": "Deleted"}