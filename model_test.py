from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

import pytest

clf = joblib.load('dockerfile/apps/model.pkl')

def test_no_args():
    with pytest.raises(ValueError):
        query_df = pd.DataFrame({})
        query = pd.get_dummies(query_df)
        prediction =  np.asscalar(clf.predict(query))

def test_query_return_zero():
    health = 1
    absences = 2
    freetime = 1
    studytime = 1
    failures = 1
    schoolsup = 0
    famsup = 0
    famrel = 1
    dalc = 0
    walc = 0
    query_df = pd.DataFrame({ 'health' : pd.Series(health) ,'absences' : pd.Series(absences),'freetime' : pd.Series(freetime),'studytime' : pd.Series(studytime),'failures' : pd.Series(failures),'schoolsup' : pd.Series(schoolsup),'famsup' : pd.Series(famsup),'famrel' : pd.Series(famrel),'Dalc' : pd.Series(dalc),'Walc' : pd.Series(walc)})
    query = pd.get_dummies(query_df)
    prediction = np.asscalar(clf.predict(query))
    assert prediction == 0

def test_query_return_one():
    health = 0 
    absences = 0
    freetime = 0
    studytime = 0
    failures = 1
    schoolsup = 0
    famsup = 0
    famrel = 0
    dalc = 1
    walc = 1
    query_df = pd.DataFrame({ 'health' : pd.Series(health) ,'absences' : pd.Series(absences),'freetime' : pd.Series(freetime),'studytime' : pd.Series(studytime),'failures' : pd.Series(failures),'schoolsup' : pd.Series(schoolsup),'famsup' : pd.Series(famsup),'famrel' : pd.Series(famrel),'Dalc' : pd.Series(dalc),'Walc' : pd.Series(walc)})
    query = pd.get_dummies(query_df)
    prediction = np.asscalar(clf.predict(query))
    assert prediction == 1

def test_too_few_args():
    with pytest.raises(ValueError):
        query_df = pd.DataFrame({'health' : pd.Series(1)})
        query = pd.get_dummies(query_df)
        prediction =  np.asscalar(clf.predict(query))

def test_too_many_args():
    with pytest.raises(ValueError):
        age = 100
        health = 0 
        absences = 0
        freetime = 0
        studytime = 0
        failures = 1
        schoolsup = 0
        famsup = 0
        famrel = 0
        dalc = 1
        walc = 1
        query_df = pd.DataFrame({ 'age': pd.Series(age), 'health' : pd.Series(health) ,'absences' : pd.Series(absences),'freetime' : pd.Series(freetime),'studytime' : pd.Series(studytime),'failures' : pd.Series(failures),'schoolsup' : pd.Series(schoolsup),'famsup' : pd.Series(famsup),'famrel' : pd.Series(famrel),'Dalc' : pd.Series(dalc),'Walc' : pd.Series(walc)})
        query = pd.get_dummies(query_df)
        prediction = np.asscalar(clf.predict(query))