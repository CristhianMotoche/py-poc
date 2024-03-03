from dataclasses import dataclass

from flask import Flask
from flask import abort, render_template, request

app = Flask(__name__)

@dataclass
class City:
    id: int
    name: str
    recomendation: str


cities = [
    # Initial city
    City(
        id=1,
        name='Quito',
        recomendation=(
            'Visit The Teleferico and see city over 4000'
            ' meters over sea level after riding a 4km cable car'
        )
    )
]

def next_id() -> int:
    try:
        return max([x.id for x in cities]) + 1
    except ValueError:
        return 1

def lookup_city(city_id: int) -> City:
    [x] = [city for city in cities if city.id == city_id]
    return x

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", cities=cities)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    new_city = City(id=next_id(), name=data['name'], recomendation=data['recomendation'])
    cities.append(new_city)
    return render_template("city_row.html", city=new_city)

@app.route("/get/<int:city_id>", methods=["GET"])
def get(city_id: int):
    try:
        city = lookup_city(city_id)
        return render_template("city_row.html", city=city)
    except ValueError:
        return abort(404)

@app.route("/delete/<int:city_id>", methods=["DELETE"])
def delete(city_id: int):
    try:
        cities.remove(lookup_city(city_id))
        return ""
    except ValueError:
        return abort(404)

@app.route("/edit/<int:city_id>", methods=["GET", "POST"])
def edit(city_id: int):
    try:
        city = lookup_city(city_id)
        if request.method == "POST":
            data = request.form
            city.name = data['name']
            city.recomendation = data['recomendation']
            return render_template("city_row.html", city=city)
        return render_template("edit_city.html", city=city)
    except ValueError:
        return abort(404)
