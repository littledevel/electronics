from flask import Flask, request, render_template, url_for, flash, redirect
from db_json import JSON_Store
from db_interface import DatabaseModel

app = Flask(__name__)
app.config['SECRET_KEY'] = "TA TRIA GOURONUAKA"
store = JSON_Store()


@app.route('/', methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html")


@app.route('/create', methods=["POST", "GET"])
def create():
    data = {}
    if request.method == 'POST':
        data["quantity"] = request.form['quantity']
        data["category"] = request.form['category']
        data["description"] = request.form['description']
        data["link"] = request.form['link']
        store.put(data)
        return redirect(url_for('items'))
    return render_template("create.html", option_list=sorted(DatabaseModel().store_categories))

@app.route('/update', methods=["GET","POST"])
def update():
    data = {}
    if request.method == 'POST':
        data["quantity"] = request.form['quantity']
        data["category"] = request.form['category']
        data["description"] = request.form['description']
        data["link"] = request.form['link']
        store.put(data)
        return redirect(url_for('items'))
    store_item = store.get()[request.args["id"]]
    return render_template("update.html", store_item=store.get()[request.args["id"]],
                           option_list=sorted(DatabaseModel().store_categories))

@app.route('/delete', methods=["GET","POST"])
def delete():
    store.delete(request.args["id"])
    return render_template('items.html', store_items=store.get())


@app.route('/items')
def items():
    return render_template('items.html', store_items=store.get())


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
