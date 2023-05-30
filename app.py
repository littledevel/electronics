from flask import Flask, request, render_template, url_for, flash, redirect
from db_json import Store

app = Flask(__name__)
app.config['SECRET_KEY'] = "TA TRIA GOURONUAKA"
store = Store()


@app.route('/', methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html")


@app.route('/manage', methods=["GET"])
def manage():
    return "OK"


@app.route('/create', methods=["POST", "GET"])
def create():
    data = {}
    if request.method == 'POST':
        data["name"] = request.form['item_name']
        data["quantity"] = request.form['quantity']
        data["description"] = request.form['description']
        if len(data["name"]) < 1:
            return render_template("error.html",
                                   error="Store items should have at least a name, please press Back and reenter item data")
        store.put(data)
        return redirect(url_for('index'))
    return render_template("create.html")


@app.route('/items')
def items():
    return render_template('items.html', store_items=store.get())


if __name__ == '__main__':
    app.run()
