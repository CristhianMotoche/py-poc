from dataclasses import dataclass

from flask import Flask
from flask import abort, render_template, request

app = Flask(__name__)

@dataclass
class City:
    id: int
    name: str
    description: str


cities = [
    # Initial city
    City(id=1, name='Quito', description='Carita de Dios!')
]

def next_id() -> int:
    try:
        return max([x.id for x in cities]) + 1
    except ValueError:
        return 1

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", cities=cities)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    new_city = City(id=next_id(), name=data['name'], description=data['description'])
    cities.append(new_city)
    return render_template("city_row.html", city=new_city)

@app.route("/delete/<int:city_id>", methods=["DELETE"])
def delete(city_id: int):
    try:
        [x] = [city for city in cities if city.id == city_id]
        cities.remove(x)
        return ""
    except ValueError:
        return abort(404)
