import os
import joblib
import json


def init():
    global model
    # model_path = Model.get_model_path(model_name, version=version)
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model/model.joblib")
    print(f"Loading model from {model_path}")
    model = joblib.load(model_path)


def run(raw_data):
    try:
        print(raw_data)
        data = json.loads(raw_data)["data"]
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
