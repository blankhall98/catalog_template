from flask import Flask, render_template, redirect, url_for, flash, request
from forms import addItem
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blankhalldev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/items.db'

db = SQLAlchemy(app)

#database class -----
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50))
    details = db.Column(db.String(100))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Item %r>' % self.name

#Routes -----
@app.route("/", methods=['GET','POST'])
def index():
    items = Item.query.all()
    return render_template('index.html',items=items)

@app.route("/add_item", methods=["GET","POST"])
def add_item():
    form = addItem()

    #If addItem form is valid
    if form.validate_on_submit():
        
        name = form.name.data
        category = form.category.data
        details = form.details.data
        price = form.price.data

        new_item = Item(name=name,category=category,details=details,price=price)

        db.session.add(new_item)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('add_item.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)