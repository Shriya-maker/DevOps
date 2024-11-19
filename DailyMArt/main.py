from flask import Flask, render_template
from pymongo import MongoClient
import os

main = Flask(__name__)

db_password = os.getenv('MONGO_DB_PASSWORD')

if not os.getenv('TESTING'):
    client = MongoClient(
        f"mongodb+srv://host:{db_password}@cluster0.pjpf7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client.shop_db
    collection = db["Products"]
else:
    client = None
    db = None
    collection = None


@main.route('/')
def home():
    return render_template("home.html")


@main.route('/product')
def products():
    if os.getenv('TESTING'):
        temp = []
    else:
        temp = list(collection.find())
    return render_template("/product.html", products=temp)


if __name__ == '__main__':
    main.run(debug=True)