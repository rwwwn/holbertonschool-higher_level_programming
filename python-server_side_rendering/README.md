# Python - Server-Side Rendering

This project is part of the Holberton School curriculum and focuses on implementing server-side rendering (SSR) using Python and Flask. Unlike client-side rendering, SSR delivers fully rendered HTML pages from the server, improving performance, SEO, and user experience.

---

## 🧠 Learning Objectives

- Understand the difference between server-side and client-side rendering
- Build SSR-based web apps using Flask and Jinja2
- Create dynamic templates with loops and conditionals
- Read and process data from JSON, CSV, and SQLite files
- Handle query parameters and user input in Flask routes
- Build reusable components (e.g., headers/footers) with template includes

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `task_00_intro.py` | Generates invitation text files using a template and list of attendee dictionaries |
| `task_01_jinja.py` | Serves basic Flask app with reusable header/footer templates |
| `task_02_logic.py` | Displays dynamic content using Jinja2 loops and conditionals from a JSON file |
| `task_03_files.py` | Renders data from JSON or CSV files using query parameters |
| `task_04_db.py` | Adds support for SQLite as a dynamic data source with filtering by ID |

---

## 🗂️ Data Files

- `template.txt` – Template used for generating invitations
- `items.json` – Contains items for dynamic list rendering
- `products.json` – JSON product list for data display
- `products.csv` – CSV version of the product list
- `products.db` – SQLite database with a `Products` table (id, name, category, price)

---

## 🛠 Technologies

- Python 3.x
- Flask
- Jinja2 Templating
- JSON, CSV, SQLite
- HTML5

---

## ▶️ How to Run

Install Flask if you haven't:
```bash
pip install Flask
