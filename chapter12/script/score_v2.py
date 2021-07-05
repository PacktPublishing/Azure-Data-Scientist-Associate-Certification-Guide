import os
import joblib
from inference_schema.schema_decorators import input_schema, output_schema
import pandas as pd
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType
import numpy as np
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType

def init():
    global model
    # model_path = Model.get_model_path(model_name, version=version)
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model/model.joblib")
    print(f"Loading model from {model_path}")
    model = joblib.load(model_path)


data_sample = pd.DataFrame(
    {
        "income": pd.Series([2000.0], dtype="float64"),
        "credit_cards": pd.Series([1], dtype="int"),
        "age": pd.Series([25], dtype="int")
    }
)
output_sample = np.array([0])
@input_schema("data", PandasParameterType(data_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
