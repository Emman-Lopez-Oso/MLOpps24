# Experiment tracking with MLFlow
This markdown is made to keep up with the notes from lesson 3.

### Notes on running ML FLow and setting up servers locally:

- When running your MLF command: `mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000` it's important to find the actual **tracking uri** which can be found right after the phrase "Listening at:" typically as `http://127.0.0.1:5001`.

### Add parameter tuning to the notebook
In the previous lesson, we were messing around with the `alpha` for tuning the hyperparameters of our model.

mlflow server \
    --backend-store-uri sqlite:////workspaces/MLOpps24/02-experiment-tracking/mlflow_db/mlflow.db \
    --default-artifact-root /workspaces/MLOpps24/02-experiment-tracking/mlflow_artifacts \
    --host 0.0.0.0 \
    --port 5000

### Hyperopt with ML Flow

- Hyperopt [fmin](https://github.com/hyperopt/hyperopt/wiki/FMin): method minimizes outputs of hyperparameters. So we are finding the best value of scalar-valued, possibly stachastic function over a set of arguments into that function.
- Hyperopt