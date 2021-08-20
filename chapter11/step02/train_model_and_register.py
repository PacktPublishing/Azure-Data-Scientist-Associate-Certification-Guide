# This code is a modified version of the train_model.py
# to demonstrate the registration process you will learn
# in Chapter 12, Operationalizing models with code
import argparse
import os
import lightgbm as lgb
import joblib


parser = argparse.ArgumentParser()
parser.add_argument(
    "--learning-rate",
    type=float,
    dest="learning_rate",
    help="Learning date for LightGBM",
    default=0.01,
)
parser.add_argument(
    "--input-path",
    type=str,
    dest="input_path",
    help="Directory containing the datasets",
    default="../data",
)
parser.add_argument(
    "--output-path",
    type=str,
    dest="output_path",
    help="directory to store model",
    default="./model",
)
args = parser.parse_args()

print(f"Loading data from {args.input_path}")
train_data = lgb.Dataset(os.path.join(args.input_path, "train_dataset.bin"))
validation_data = lgb.Dataset(os.path.join(args.input_path, "validation_dataset.bin"))

param = {
    "task": "train",
    "objective": "binary",
    "metric": "auc",
    "num_leaves": 5,
    "learning_rate": args.learning_rate,
}

model = lgb.train(
    param,
    train_set=train_data,
    valid_sets=validation_data,
    early_stopping_rounds=5,
)

output_path = args.output_path
if not os.path.exists(output_path):
    os.makedirs(output_path)

joblib.dump(value=model, filename=os.path.join(output_path, "model.joblib"))

# The following code is explained in Chapter 12, Operationalizing models with code
from azureml.core.run import Run, _OfflineRun
run = Run.get_context()
registered_model = None
if type(run) == _OfflineRun:
    # If we are offline we don't have the run context to
    # associate with the model registration.
    from azureml.core import Workspace, Model
    ws = Workspace.from_config()
    registered_model = Model.register(
        ws,
        model_name="chapter11-loan-model-offline",
        model_path=output_path,
        model_framework="LightGBM",
        model_framework_version=lgb.__version__
    )
else:
    # We need to upload artifact to the run
    run.upload_folder("model", output_path)
    registered_model = run.register_model(
        model_name="chapter11-loan-model-online",
        model_path="model",
        model_framework="LightGBM",
        model_framework_version=lgb.__version__,
    )

print(f"Registered version {registered_model.version} for model {registered_model.name}")
