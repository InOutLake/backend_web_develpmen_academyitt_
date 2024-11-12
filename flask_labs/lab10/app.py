import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data", "mydatabase.db"
)

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    info = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Item('{self.title}', '{self.price}', '{self.info}', '{self.photo}')"


with app.app_context():
    db.create_all()
    if not Item.query.all():
        item1 = Item(
            title="Яблоко",
            price=49.99,
            info="Сладкое красное сочное наливное яблочко",
            photo="apple.png",
        )
        item2 = Item(
            title="Банан",
            price=29.99,
            info="Сладкая желтая деликатесная бананка",
            photo="banana.png",
        )
        item3 = Item(
            title="Апельсин",
            price=39.99,
            info="Сладкая солнечная апельсинка",
            photo="orange.png",
        )
        item4 = Item(
            title="Виноград",
            price=69.99,
            info="Сладкие пурпурные виноградинки",
            photo="grape.png",
        )

        db.session.add(item1)
        db.session.add(item2)
        db.session.add(item3)
        db.session.add(item4)

        db.session.commit()


@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
