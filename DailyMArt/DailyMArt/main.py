from flask import Flask, render_template
from pymongo import MongoClient

main = Flask(__name__)

client = MongoClient("mongodb+srv://host:host@cluster0.pjpf7.mongodb.net/shop_db?retryWrites=true&w=majority")
db = client.shop_db
collection = db["Products"]



mock_data = [{"name": "High_fat", "price": "6.99", "expiry": "23/12", "category": "milk", "image_path": "/static/images/milk.jpg"}]

# Insert mock data only if the collection is empty
if collection.count_documents({}) == 0:
    collection.insert_many(mock_data)

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/product')
def products():
    temp = list(collection.find())
    return render_template("product.html", products=temp)

if __name__ == '__main__':
    main.run(debug=True)