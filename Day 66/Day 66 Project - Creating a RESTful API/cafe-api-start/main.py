from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import random

app = Flask(__name__)

# # Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Boolean: Callable


db = MySQLAlchemy(app)


# # Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=["GET"])
def rand_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(
        cafe=random_cafe.to_dict()
    )


@app.route('/all', methods=["GET"])
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# # HTTP GET - Read Record
@app.route('/search', methods=["GET"])
def search():
    loc = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=loc).first()
    if cafe:
        return jsonify(
            cafe=cafe.to_dict()
        )
    else:
        return jsonify(
             error={
                "Not Found": "Sorry, we do not have a cafe at that location"
             }
        )


# # HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={
            "success": "New cafe added!"
        }
    )


# # HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def update(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    price = request.args.get('new_price')
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(
            success="Price Updated!"
        )
    else:
        return jsonify(
            error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        )


# # HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == "TopSecretAPIKey":
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(
                success="Cafe Deleted!"
            )
        else:
            return jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            )
    else:
        return jsonify(
            error="Sorry, that's not allowed. Make sure you have the correct API Key."
        )


if __name__ == '__main__':
    app.run(debug=True)