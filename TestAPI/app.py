import email
from flask import Flask, render_template, request, redirect, url_for, jsonify,make_response,session,send_file
from flask.sessions import NullSession
import flask_login 
from flask_login.utils import logout_user
import pandas as pd
import pyodbc
import json
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import decimal
from openpyxl.styles import Alignment , Font , PatternFill
import openpyxl
import time 
import babel
import sys

app = Flask(__name__)


@app.route("/API_INF_OEE01", methods=['POST'])
def API_INF_OEE01():
    print(request.get_json())
    data = request.get_json()
    print("------------")
   
    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True ,port=5001)