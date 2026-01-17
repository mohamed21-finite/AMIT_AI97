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
def add_customer():
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Insert the document into the collection
        result = customers_col.insert_one({
            "Name": user_data["name"],
            "Age": user_data["age"],
            "Gender": user_data["gender"],
            "Region": user_data["region"]
        })
        
        # Return success message and the ID of the new document
        return jsonify({
            "message": "User added successfully",
            "id": str(result.inserted_id)
        }), 201 # 201 Created status code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


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

response1 = requests.post("http://127.0.0.1:5000/add_customers",json=new_customer1)

response2 = requests.get("http://127.0.0.1:5000/customers")
print(response1.json())
print(response2.json())