from flask import Flask, request
import json
from inventory import Item,Inventory

app = Flask(__name__)

inv = Inventory()



@app.route('/')
def welcome():  # put application's code here
    return 'Welcome to Electronics Inventory'


@app.route('/items')
def get_items():
    return inv.get_all()


@app.route('/add',methods=["POST"])
def add_item():
    item = Item()
    item.marshal(request.json)
    inv.put(item)
    return "OK"


if __name__ == '__main__':
   app.run()
