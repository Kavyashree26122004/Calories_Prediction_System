# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 04:48:23 2025

@author: ADMIN
"""

import json
import requests

url='http://127.0.0.1:8000/calories_prediction'

input_data_for_model ={
    'Gender' :0,
    'Age' : 68,
    'Height' : 190.0,
    'Weight' : 94.0,
    'Duration': 29.0,
    'Heart_Rate' : 105.0,
    'Body_Temp' : 40.8
        
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, json=input_data_for_model)


print(response.status_code)   # should be 200
print(response.json())

