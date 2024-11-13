import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data", "mydatabase.db"
)
app.config["SWAGGER"] = {"title": "Items API", "uiversion": 3}
Swagger(app, template_file="docs/items.yaml")

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Item('{self.name}')"


with app.app_context():
    db.create_all()
    if not Item.query.all():
        item1 = Item(name="Apple")
        item2 = Item(name="Banana")
        item3 = Item(name="Orange")
        db.session.add_all([item1, item2, item3])
        db.session.commit()


@app.route("/api/items", methods=["GET", "POST"])
def items():
    if request.method == "GET":
        items = Item.query.all()
        return jsonify([{"id": item.id, "name": item.name} for item in items])

    if request.method == "POST":
        data = request.get_json()
        item = Item(name=data["name"])
        db.session.add(item)
        db.session.commit()
        return jsonify({"id": item.id, "name": item.name}), 201


@app.route("/api/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
def item(item_id):
    item = Item.query.get_or_404(item_id)

    if request.method == "GET":
        return jsonify({"id": item.id, "name": item.name})

    if request.method == "PUT":
        data = request.get_json()
        item.name = data["name"]
        db.session.commit()
        return jsonify({"id": item.id, "name": item.name})

    if request.method == "DELETE":
        db.session.delete(item)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)
