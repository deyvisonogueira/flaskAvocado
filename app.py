import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open("model.pkl", "rb"))
class_data = pd.read_csv('avocado.csv')
type = dict(class_data['type'])


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    pred = model.predict(final_features)
    output = type[pred[0]]
    return render_template("index.html", prediction_text="Tipo " + output)

@app.route("/api", methods=["POST"])
def results():
    data = request.get_json(force=True)
    pred = model.predict([np.array(list(data.values()))])
    output = type[pred[0]]
    return jsonify(output)

@app.route("/api", methods=["GET"])
def gettype():
    typelist = type.tolist()
    return jsonify(typelist)
