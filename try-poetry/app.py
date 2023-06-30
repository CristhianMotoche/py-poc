from flask import Flask, request, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 32*'a'

class Company:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Contact:
    def __init__(self, id, name, company_id):
        self.id = id
        self.name = name
        self.company_id = company_id

companies = [Company(1, 'Something'), Company(2, 'Else')]
contacts = [Contact(1, 'Something', 1), Contact(2, 'Else', 1),
            Contact(3, 'Something', 2), Contact(4, 'Else', 2)]

class MyForm(FlaskForm):

    contact = FieldList(StringField('Full Name'), min_entries=3)
    name = StringField('REAL NAME', validators=[Required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = MyForm()
    if form.validate_on_submit():
        print(form.data)
        return 'Success'
    return render_template("index.html", form=form)


@app.route('/api/contacts')
def api_contacts():
    company = request.args.get('company', type=int)
    resp_contacts = map(lambda contact: {'id': contact.id, 'name': contact.name},
            filter(lambda contact: contact.company_id == company, contacts))
    return jsonify(list(resp_contacts))


if __name__ == "__main__":
    app.run(debug=True)
