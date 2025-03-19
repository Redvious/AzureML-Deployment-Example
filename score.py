import numpy as np
from azureml.core.model import Model
import pickle
import json

def init():
    global model
    # Get the path where the model file is stored
    model_path = Model.get_model_path("my_model", version=12)

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")

def run(raw_data):

    try:
        data = np.array(json.loads(raw_data)["data"])
        predictions = model.predict(data)
        # Return the predictions as JSON
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})