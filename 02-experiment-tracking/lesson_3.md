# Experiment tracking with MLFlow 

Add parameter tuning to the notebook


In the previous lesson, we were messing around with the `alpha` for tuning the hyperparameters of our model. 

mlflow server \
    --backend-store-uri sqlite:////workspaces/MLOpps24/02-experiment-tracking/mlflow_db/mlflow.db \
    --default-artifact-root /workspaces/MLOpps24/02-experiment-tracking/mlflow_artifacts \
    --host 0.0.0.0 \
    --port 5001



