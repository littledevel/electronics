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

@app.route('/items')
def items():
    return render_template('items.html', store_items=store.get())



if __name__ == '__main__':
   app.run()
