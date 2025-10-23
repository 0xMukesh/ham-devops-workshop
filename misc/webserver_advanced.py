from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "password")
DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "testdb")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/add", methods=["POST"])
def add_item():
    data = request.json
    item = Item(name=data["name"])
    db.session.add(item)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name})


@app.route("/list", methods=["GET"])
def list_items():
    items = Item.query.all()
    return jsonify([{"id": i.id, "name": i.name} for i in items])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
