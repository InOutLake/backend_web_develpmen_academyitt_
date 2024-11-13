import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data", "mydatabase.db"
)
app.config["SWAGGER"] = {"title": "Users API", "uiversion": 3}
Swagger(app, template_file="docs/users.yaml")

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Item('{self.title}', '{self.price}', '{self.info}', '{self.photo}')"


with app.app_context():
    db.create_all()
    if not User.query.all():
        user1 = User(name="Alice")
        user2 = User(name="Bob")
        user3 = User(name="Carol")
        db.session.add_all([user1, user2, user3])
        db.session.commit()


@app.route("/api/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        users = User.query.all()
        return jsonify([{"id": user.id, "name": user.name} for user in users])

    if request.method == "POST":
        data = request.get_json()
        user = User(name=data["name"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"id": user.id, "name": user.name}), 201


@app.route("/api/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == "GET":
        return jsonify({"id": user.id, "name": user.name})

    if request.method == "PUT":
        data = request.get_json()
        user.name = data["name"]
        db.session.commit()
        return jsonify({"id": user.id, "name": user.name})

    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)
