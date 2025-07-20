from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON error: {e}")
        return []

def load_csv_data():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"CSV error: {e}")
        return []

def load_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": str(row[0]), "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    except Exception as e:
        print(f"SQLite error: {e}")
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    elif source == 'sql':
        data = load_sql_data()
    else:
        error = "Wrong source"

    if not error and product_id:
        product_id = str(product_id)
        filtered = [item for item in data if str(item.get("id")) == product_id]
        if filtered:
            data = filtered
        else:
            error = "Product not found"
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
