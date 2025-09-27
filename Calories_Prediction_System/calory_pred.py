# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 04:42:08 2025

@author: ADMIN
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    
    Gender : int
    Age : int
    Height : float
    Weight : float
    Duration: float
    Heart_Rate : float
    Body_Temp : float
    
# loading the saved model

model=pickle.load(open('calories_prediction.sav','rb'))

@app.post('/calories_prediction')

def calory_pred(input_parameters : model_input):
    input_data=input_parameters.json()
    input_dictionary =json.loads(input_data)
    
    gen=input_dictionary['Gender']
    age=input_dictionary['Age']
    height=input_dictionary['Height']
    weight=input_dictionary['Weight']
    duration=input_dictionary['Duration']
    rate=input_dictionary['Heart_Rate']
    temp=input_dictionary['Body_Temp']
    
    input_list = [gen,age,height,weight,duration,rate,temp]
    
    prediction=model.predict([input_list])
    
    return {"calories_prediction": float(prediction[0])}