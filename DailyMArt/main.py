from itertools import product

from flask import Flask, render_template
from pymongo import MongoClient

main = Flask(__name__)

client = MongoClient(f"mongodb+srv://host:host@cluster0.pjpf7.mongodb.net/shop_db?retryWrites=true&w=majority")
db= client.shop_db
collection = db["Products"]



@main.route('/')
def home():
    return render_template("home.html")

@main.route('/product')
def products():
    temp =list(collection.find())
    return render_template("/product.html",products=temp)

if __name__ == '__main__':
    main.run(debug=True)
