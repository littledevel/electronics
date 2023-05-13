from flask import Flask, request, render_template
from inventory import StoreItem, Store
import json

app = Flask(__name__)

store = Store()

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    store.add(StoreItem().marshal(request.json))
    return "OK"


@app.route('/create', methods=["POST", "GET"])
def create():
    if request.method == 'POST':
        name = request.form['item_name']
        quantity = request.form['quantity']
        description = request.form['description']

    return render_template("create.html")

@app.route('/items')
def items():
    return render_template('items.html', store_items=store.get())



if __name__ == '__main__':
   app.run()
