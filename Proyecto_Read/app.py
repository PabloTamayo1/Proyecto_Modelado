from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://10.40.45.49:27025/')
db = client['ProyectV1Read']
collection = db['health1']

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener los datos
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find())
        for item in data:
            item['_id'] = str(item['_id'])
        return jsonify({'status': 'success', 'data': data})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '_main_':
    app.run()