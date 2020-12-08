from werkzeug.utils import secure_filename
import joblib
from flask import Flask, request, render_template,jsonify
import numpy as np
import requests
import json
import threading
# Define a flask app
app = Flask(__name__, template_folder='Templates')

def process_eval():
    response = requests.request("GET", "https://31ps5t3oc2.execute-api.us-west-1.amazonaws.com/default/datafroms3")
    x = eval(response.text)
    return x['data']
#
# @app.route('/', methods=['GET'])
# def index():
#    return render_template('fileUpload.html')
@app.route('/', methods=['GET', 'POST'])
def handle_form():
        y=process_eval()
        Trump_Neutral = y['Trump_Neutral']
        Trump_Positive = y['Trump_Positive']
        Trump_Negative = y['Trump_Negative']
        Biden_Negative = y['Biden_Negative']
        Biden_Neutral = y['Biden_Neutral']
        Biden_Positive = y['Biden_Positive']
        Total = y['No_One'] + Trump_Neutral+ Trump_Positive+ Trump_Negative+ Biden_Negative + Biden_Neutral+ Biden_Positive
        return render_template('fileUpload.html',Total = Total, Trump_Negative= Trump_Negative, Trump_Neutral = Trump_Neutral, Trump_Positive = Trump_Positive, Biden_Negative = Biden_Negative, Biden_Neutral= Biden_Neutral,
                               Biden_Positive = Biden_Positive)
# @app.route('/', methods=['GET', 'POST'])
# def handle_form1():
#         return render_template('FirstPage.html')
if __name__ == "__main__":
    app.run()

