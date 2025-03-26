import numpy as np
from azureml.core.model import Model
from joblib import load
import json


def init():
    global model
    model_path = Model.get_model_path("iris__model")
    model = load(model_path)
    print("Model loaded successfully")

def run(raw_data):
    try:
        data = np.array(json.loads(raw_data)["data"])
        predictions = model.predict(data)
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
    
