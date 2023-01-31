import pandas as pd
from flask import Flask, request
import joblib

app = Flask(__name__)
alphabet = "abcdefghijklmnopqrstuvwxyz-"


def encode_prenom(x):
    output = [letter in x.upper() for letter in alphabet.upper()]
    return pd.Series(output)


@app.route("/predict/")
def predict():
    prenom = request.args.get('prenom')

    if prenom:
        model = joblib.load("prenoms.v1.joblib")
        result = model.predict([encode_prenom(prenom)])
        prediction = result[0]

        if prediction > 0.5:
            return 'M'
        else:
            return 'F'

    return 'KO'
