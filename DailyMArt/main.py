from itertools import product

from flask import Flask, render_template
from pymongo import MongoClient

main = Flask(__name__)

client = MongoClient(f"mongodb+srv://host:host@cluster0.pjpf7.mongodb.net/shop_db?retryWrites=true&w=majority")
db= client.shop_db
collection = db["Products"]

mock_data=[{"name":"High_fat","price":"6.99","expiry":"23/12","category":"milk","image_path":"/static/images/milk.jpg"}]
collection.insert_many(mock_data)


@main.route('/')
def home():
    return render_template("home.html")

@main.route('/product')
def products():
    products =list(collection.find())
    return render_template("/product.html",product_obj=products)

if __name__ == '__main__':
    main.run(debug=True)
