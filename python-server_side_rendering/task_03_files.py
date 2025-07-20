from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def load_csv_data():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"Error reading CSV: {e}")
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
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if not error and product_id:
        try:
            product_id = str(int(product_id))  # ensure match in both JSON and CSV formats
            filtered = [item for item in data if str(item.get("id", item.get("id"))) == product_id]
            if filtered:
                data = filtered
            else:
                error = "Product not found"
                data = []
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
