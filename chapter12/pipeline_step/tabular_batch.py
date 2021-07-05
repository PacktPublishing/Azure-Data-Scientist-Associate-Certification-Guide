from azureml.core import Model
import joblib


def init():
    global model
    model_path = Model.get_model_path("chapter12-loans")
    model = joblib.load(model_path)


def run(mini_batch):
    print(mini_batch.info())
    mini_batch["approved"] = model.predict(mini_batch)
    return mini_batch.values.tolist()
