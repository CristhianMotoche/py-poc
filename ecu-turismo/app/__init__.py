from flask import Flask
from flask import abort, render_template, request

app = Flask(__name__)

global_id = 1
books = [
    { 'id': 1,
      'title': 'Cumanda',
      'author': 'Juan Leon Mera'
    },
]

def next_id() -> int:
    try:
        return max([x['id'] for x in books]) + 1
    except ValueError:
        return 1

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", books=books)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    new_book = { 'id': next_id(), 'title': data['title'], 'author': data['author'] }
    books.append(new_book)
    print('CL - books', books);
    return f"""
    <tr>
        <td>{new_book['title']}</td>
        <td>{new_book['author']}</td>
        <td>EDIT</td>
        <td>
          <button hx-delete="/delete/{new_book['id']}" />Delete?</button>
        </td>
    </tr>
    """

@app.route("/delete/<int:book_id>", methods=["DELETE"])
def delete(book_id: int):
    try:
        [x] = [book for book in books if book['id'] == book_id]
        books.remove(x)
        return ""
    except:
        return abort(404)
