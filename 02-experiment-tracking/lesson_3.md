# Experiment tracking with MLFlow
This markdown is made to keep up with the notes from lesson 3. 

### Notes on running ML FLow and setting up servers locally: 

- When running your MLF command: `mlflow ui --backend-store-uri sqlite:///02-experiment-tracking/mlflow_db/mlflow.db --port 5001` it's important to find the actual **tracking uri** which can be found right after the phrase "Listening at:" typically as `http://127.0.0.1:5001`. 

### Add parameter tuning to the notebook
- In the previous lesson, we were messing around with the `alpha` for tuning the hyperparameters of our model.

mlflow server \
    --backend-store-uri sqlite:////workspaces/MLOpps24/02-experiment-tracking/mlflow_db/mlflow.db \
    --default-artifact-root /workspaces/MLOpps24/02-experiment-tracking/mlflow_artifacts \
    --host 0.0.0.0 \
    --port 5001

### Hyperopt with ML Flow

- Hyperopt [fmin](https://github.com/hyperopt/hyperopt/wiki/FMin): method minimizes outputs of hyperparameters. So we are finding the best value of scalar-valued, possibly stachastic function over a set of arguments into that function.
- Hyperopt hp():

# Model Management 

## Machine Learning Lifecycle
![ML Lifecycle](https://i0.wp.com/neptune.ai/wp-content/uploads/2023/10/Experiment-tracking.png?resize=1020%2C534&ssl=1)

Refers to the multiple steps in MLOPS that are required to monitor and maintain an ML model. 

While Experiment Tracking covers model training, evaluation and architecture (recursively), Model Management covers ET as well as model versioning, deployment and scaling hardware.

You can use MLFlow to track your models. Once you finish with those experiment tracking stages, you have to monitor and determine if the model requires any updating.

After we've done all the work of training and evaluating, we want to be able to save it and version it somehow. MLFlow can help with managing and deploying models. Problems with keeping versions in folder system is that there is no versioning (folder name can help but who knows), no model lineage (not easy to understand how the models were created, what were the hyperparameters, etc.), and is error prone (you end up overwriting an older model)

### Model management with mlflow 
Typically, we'd save with pickle using the following code: 
`with open('models/lin_reg.bin', 'wb') as f_out:
    pickle.dump(d(v,lr), f_out)`

Later we learned how to set tags and parameters in MLFlow using methods from the package.

#### Saving the model as an artifact 
The simplest way to do it is by using `mlflow.log_artifact()`

best to use `mlflow.xgboost.log_model(booster, artifact_path = "models_mlflow")`

So the options are: 
1. Log model as an artifact - `mlflow.log_artifact("my_model", artifact_path="models/")
2. Log model using the method log_model() - mlflow.<framework>.log_model(model, artifact_path = "models/")


# Model Registry 

Theory is that you get an email from a Data Scientist that wants you to deploy a model. A few questions you might ask as a data engineer are: 

1. What has changed? 
2. Should I update any of the hyperparameters of the model im production? 
3. Is there any pre-processing that needs to be added?
4. What is the environment that this model should run? 


## Usin MlFlow Tracking Server
The platform has a series of model runs that have a few that are ready for production, and those get registered into ML Flow's Model Registry. 

You essentially have it pbroken down into:
- Staging
- Production
- Archives

The deployment engineer looks through the various versions and determines what gets put through the various stages of the lifecycle.

The Model Registry does not deploy any model, it just lists them out and the labels are simply tags. There needs to be some CI/CD code if there is going to be any real deployment.

After you find the models that you'd like to submit to the Registry, look for the button "Register Model". The button disappears and it leads to a link for the registered model. If you register multiple, you can have them sent to the same list of models which is at the top tab labeled "Models".

Good idea to add descriptions to the model regressors. You can also link every version of the model to a specific run, add tags to the model to ensure that you can keep tabs on the most important information.

There's a button past "Stage" that lets you put whatever model you want to in a specific portion of the staging process. 


## Model Management in MLflow

The Model Registry component is a centralized model store, set of APIs, and a UI, to collaboratively manage the full lifecycle of an MLflow Model. 

It provides: 
- Model lineage, 
- Model versioning, 
- Stage transitions, and
- Annotations 

# MLflow in Practice 

Consider different scenarios for running MLflow 

1. A single data scientist participating in an ML competition -> Kind of irrelevant because there's no reason to create a tracking server remotely. 
2. A cross-functional team with one data scientist working on an ML model. -> Model registry would be good but it's not totally clear whether it's necessary to run this remotely. 
3. Multiple data scientists working on multiple ML models -> Absolutely important to run this remotely because there are many hands on the same project. 


## Configuring MLflow 
- Backend Store: This is where all the metadata of your experiement (Metrics, parameters, tags, etc.). If you don't specify a location for this, MLflow will assume that you want to save this all locally and will configure a local filesystem to do so. 
    - Alternatively, you can use a SQLAlchemy compatible DB. This enables your use of the Model Registry

- Artifacts Store
    - Unless otherwise specified, this will be stored locally. 
    - Remote (E.g. s3 Bucket)
- Tracking Server

## Satisfying various requirements 




