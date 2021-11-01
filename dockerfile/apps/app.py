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
     famrel = request.args.get('famrel')
     studytime = request.args.get('studytime')
     failures = request.args.get('failures')
     data = [[health],[absences],[freetime],[famrel],[studytime],[failures]]
     query_df = pd.DataFrame({ 'health' : pd.Series(health) ,'absences' : pd.Series(absences),'freetime' : pd.Series(freetime),'famrel' : pd.Series(famrel),'studytime' : pd.Series(studytime),'failures' : pd.Series(failures)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)