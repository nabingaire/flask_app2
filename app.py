from flask import Flask,render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGODB_URL,server_api=ServerApi('1'))
db = client.get_database('shop_db')
products_all = db.get_collection('products')

@app.route('/')
def home():  # put application's code
    return render_template('home.html')

@app.route('/products')
def products():
        products = list(products_all.find())  # put application's code here
        return render_template('products.html', products=products)


if __name__ == '__main__':

    app.run()
