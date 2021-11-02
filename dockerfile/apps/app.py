from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     health = request.args.get('health')     
     absences = request.args.get('absences')
     freetime = request.args.get('freetime')
     studytime = request.args.get('studytime')
     failures = request.args.get('failures')
     schoolsup = request.args.get('schoolsup')
     famsup = request.args.get('famsup')
     famrel = request.args.get('famrel')
     dalc = request.args.get('Dalc')
     walc = request.args.get('Walc')
     query_df = pd.DataFrame({ 'health' : pd.Series(health) ,'absences' : pd.Series(absences),'freetime' : pd.Series(freetime),'studytime' : pd.Series(studytime),'failures' : pd.Series(failures),'schoolsup' : pd.Series(schoolsup),'famsup' : pd.Series(famsup),'famrel' : pd.Series(famrel),'Dalc' : pd.Series(dalc),'Walc' : pd.Series(walc)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)