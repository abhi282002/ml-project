from flask import Flask, request, jsonify
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

app = application


####Route for a home page

@app.route('/')
def index():
  return "Hello World"


