from flask import Flask
from flask import render_template, request

app = Flask(__name__)

books = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", books=books)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    new_book = { 'title': data['title'], 'author': data['author'] }
    books.append(new_book)
    return f"""
    <tr>
        <td>{new_book['title']}</td>
        <td>{new_book['author']}</td>
    </tr>
    """
