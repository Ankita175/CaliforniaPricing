import pickle as pkl
from flask import Flask, request, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
@app.route('/')
def home():
    return render-template('home.html')

@app.route('/predict',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).shape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).shape(1, -1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])


