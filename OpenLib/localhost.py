from urllib import request
from flask import Flask, jsonify, render_template
from database import *

app = Flask(__name__, template_folder='html', static_folder='html')

#####FRONTEND
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    articles = prepareNews()
    return render_template('news.html',articles=articles)

@app.route('/contact')
def contact():
    return render_template('contact.html')
#####FRONTEND

##### BACKEND #####

@app.route('/show_all/<table>')
def show_all(table):
    items = showAll(table)
    return jsonify(items)

@app.route('/show_tables')
def show_tables():
    tables = showTables()
    return jsonify(tables)

@app.route('/show_first/<table>/<int:count>')
def show_first(table, count):
    items = showFirst(table, count)
    return jsonify(items)

@app.route('/show_last/<table>/<int:count>')
def show_last(table, count):
    items = showLast(table, count)
    return jsonify(items)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    databasename = data['databasename']
    del data['databasename']
    addOne(data, databasename)
    return jsonify({"message": "Record added successfully"})

@app.route('/delete/<int:rowid>/<databasename>', methods=['DELETE'])
def delete(rowid, databasename):
    deleteOne(rowid, databasename)
    return jsonify({"message": f"Record with rowid {rowid} deleted successfully"})

@app.route('/update/<int:rowid>/<databasename>', methods=['PUT'])
def update(rowid, databasename):
    data = request.json
    updateOne(rowid, data, databasename)
    return jsonify({"message": f"Record with rowid {rowid} updated successfully"})

@app.route('/create_table', methods=['POST'])
def create_table():
    data = request.json
    table_name = data['table_name']
    columns = data['columns']
    createTable(table_name, columns)
    return jsonify({"message": f"Table {table_name} created successfully"})

@app.route('/delete_table/<table_name>', methods=['DELETE'])
def delete_table(table_name):
    deleteTable(table_name)
    return jsonify({"message": f"Table {table_name} deleted successfully"})

@app.route('/find/<value>/<column>/<table>')
def find_value(value, column, table):
    result = find(value, column, table)
    return jsonify({"result": result})

@app.route('/contains/<pattern>/<column>/<table>')
def contains_pattern(pattern, column, table):
    result = contains(pattern, column, table)
    return jsonify({"result": result})

##### BACKEND #####

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
