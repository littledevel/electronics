from flask import Flask, request, render_template, url_for, flash, redirect
from inventory import StoreItem, Store
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "TA TRIA GOURONUAKA"

store = Store()

@app.route('/', methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    store.add(StoreItem().marshal(request.json))
    return "OK"


@app.route('/create', methods=["POST", "GET"])
def create():
    data = {}
    if request.method == 'POST':
        data["name"] = request.form['item_name']
        data["quantity"] = request.form['quantity']
        data["description"] = request.form['description']
        store.add(StoreItem().set_data(data))
        return redirect(url_for('index'))
    return render_template("create.html")

@app.route('/items')
def items():
    return render_template('items.html', store_items=store.get())



if __name__ == '__main__':
   app.run()
