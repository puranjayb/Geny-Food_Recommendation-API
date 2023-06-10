import pickle
import json

from fastapi import FastAPI
from pydantic import BaseModel

from sklearn.pipeline import Pipeline
import function1, function2, function3

app = FastAPI()

class input(BaseModel):
    # To be filled with the input parameters required by model
    parameter1 : str
    parameter2 : int
    parameter3 : float
    parameter4 : bool

model_pipeline = Pipeline([ ('ABC', function1()), ('PQR', function2()), ('XYZ', function3()) ])

food_recommendation_model = pickle.load(open('directory/filename', 'rb'))

@app.post('/prediction')
def food_recommendation_prediction(input_paramenters : input):
    input_data = input_paramenters.json()
    input_data_to_dictionary = json.loads(input_data)

    # Extracting the values stored under each parameter name
    parameter1 = input_data_to_dictionary['Parameter1']
    parameter2 = input_data_to_dictionary['Parameter2']
    parameter3 = input_data_to_dictionary['Parameter3']
    parameter4 = input_data_to_dictionary['Parameter4']

    input_data_to_list = [parameter1, parameter2, parameter3, parameter4]
    pipelined_data = model_pipeline.transform([input_data_to_list])
    prediction = food_recommendation_model.predict(pipelined_data)


    # Depends on the nature of prediction variable
    if ("Some Conditon"):
        result = "Condition 1"
    else:
        result = "Condition B"

    return {"Prediction" : result}



