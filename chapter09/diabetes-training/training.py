from sklearn.linear_model import LassoLars
from sklearn.metrics import mean_squared_error
from azureml.core import Workspace
from azureml.core.run import Run, _OfflineRun
import argparse
import os
import joblib

parser = argparse.ArgumentParser()
parser.add_argument('--alpha', type=float, 
                    dest='alpha', help='The alpha parameter')
args = parser.parse_args()

run = Run.get_context()
ws = None
if type(run) == _OfflineRun:
    ws = Workspace.from_config()
else:
    ws = run.experiment.workspace

diabetes_ds = ws.datasets['diabetes']
training_data, validation_data = \
               diabetes_ds.random_split(
                 percentage = 0.8,
                 seed=1337)
X_train = training_data.drop_columns('target') \
                       .to_pandas_dataframe()
y_train = training_data.keep_columns('target') \
                       .to_pandas_dataframe()
X_validate = validation_data.drop_columns('target') \
                            .to_pandas_dataframe()
y_validate = validation_data.keep_columns('target') \
                            .to_pandas_dataframe()

def train_and_evaluate(run, alpha, X_t, y_t, X_v, y_v):
  model = LassoLars(alpha=alpha)
  model.fit(X_t, y_t)
  predictions = model.predict(X_v)
  rmse = mean_squared_error(predictions, y_v, squared = False)
  range_y_validate = y_v.to_numpy().ptp()
  nrmse = rmse/range_y_validate
  run.log("nrmse", nrmse)
  run.log_row("nrmse over α", α=alpha, nrmse=nrmse)
  return model, nrmse

model, nrmse = train_and_evaluate(run, args.alpha,
                X_train, y_train, X_validate, y_validate)

os.makedirs('./outputs', exist_ok=True)
model_file_name = 'model.pkl'
joblib.dump(value=model,
            filename=
                  os.path.join('./outputs/',model_file_name))