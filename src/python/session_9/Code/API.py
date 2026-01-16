from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, request, jsonify

import threading
import time
import requests

app = Flask(__name__) # build a dumy API

client = MongoClient("mongodb://localhost:27017/")
db = client["CustomersDB"]
customers_col = db["Customers"]


@app.route('/customers', methods = ['GET'])
def get_customer():
    customers = []
    for doc in customers_col.find():
        doc['_id'] = str(doc['_id'])
        customers.append(doc)
    # serialize convert returned customers object to JSON format using jsonify
    return jsonify(customers)


@app.route('/add_customers', methods = ['POST'])
def add_customer(customer_data):
    customer_data = request.get_json()
    result = customers_col.insert_one(customer_data)
    return jsonify({"message": "Customer added", "customer_id": str(result.inserted_id)})

def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)


threading.Thread(target = run_flask).start()
time.sleep(1)

new_customer1 = {
    "name": "Cristiano Ronaldo",  
    "age": 40,              
    "gender": "Male",       
    "region": "Riadh"   
}

response = requests.post("http://127.0.0.1:5000/add_customers",new_customer1)

response = requests.get("http://127.0.0.1:5000/customers")
print(response.json())