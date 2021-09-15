import argparse
import os
import lightgbm as lgb
import joblib


parser = argparse.ArgumentParser()
parser.add_argument(
    "--learning-rate",
    type=float,
    dest="learning_rate",
    help="Learning rate for LightGBM",
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
    help="Directory to store model",
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
