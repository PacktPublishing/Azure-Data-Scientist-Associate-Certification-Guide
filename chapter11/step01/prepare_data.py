import argparse
from azureml.core.run import Run
from sklearn.model_selection import train_test_split
import lightgbm as lgb
import os

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=str, dest="dataset")
parser.add_argument(
    "--output-path", type=str, dest="output_path", help="Directory to store datasets"
)
args = parser.parse_args()

run = Run.get_context()
loans_dataset = run.input_datasets["loans"]

print(f"Dataset id: {loans_dataset.id}")
loans_df = loans_dataset.to_pandas_dataframe()

x = loans_df[["income", "credit_cards", "age"]]
y = loans_df["approved_loan"].values
feature_names = x.columns.to_list()
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

train_data = lgb.Dataset(x_train, label=y_train, feature_name=feature_names)
test_data = lgb.Dataset(x_test, label=y_test, reference=train_data)

output_path = args.output_path
if not os.path.exists(output_path):
    os.makedirs(output_path)

train_data.save_binary(os.path.join(output_path, "train_dataset.bin"))
test_data.save_binary(os.path.join(output_path, "validation_dataset.bin"))
