# Packages
import os
import yaml
import joblib
import pandas as pd

# Get customized functions from library
import packages.data_management as dm
import packages.model_trainer as mt

# MLFlow 
import mlflow

# MLFlow VARIABLES
# Getting Mlflow credentials
mlflow_config = yaml.safe_load(open("params.yaml"))["mlflow_credentials"]

MLFLOW_TRACKING_URI= mlflow_config['MLFLOW_TRACKING_URI']
MLFLOW_TRACKING_USERNAME = mlflow_config['MLFLOW_TRACKING_USERNAME']
MLFLOW_TRACKING_PASSWORD = mlflow_config['MLFLOW_TRACKING_PASSWORD'] 

os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

if __name__ == "__main__":


    # 0.Path to prepared data
    path_to_data = './git_actions_data/preprocessed/spam_preprocessed.csv'

    # 1.Read the prepared data
    prepared_data = pd.read_csv(path_to_data)

    # 2.Create train - test split
    train_test_data, vectorizer = dm.create_train_test_data(prepared_data['text'], 
                                            prepared_data['label'], 
                                            0.30, 2024)

    # 3.Run training
    model, report = mt.run_model_training(train_test_data['x_train'], train_test_data['x_test'], 
                            train_test_data['y_train'], train_test_data['y_test'])

    # 4.Save the trained model the vectorizer and metrics
    joblib.dump(model, './git_actions_models/spam_detector_model.pkl')
    joblib.dump(vectorizer, open("./git_actions_vectors/vectorizer.pickle", "wb")) 

    # Save the metrics
    saving_folder = "./git_actions_data/metrics"
    final_file_name = "metrics.json"
    dm.save_metrics(report, saving_folder, final_file_name)

    # MLFlow Tracking Experiment
    mlflow.set_experiment("MLOps With Github Actions Experiment")

    with mlflow.start_run():

        # Log different metrics
        mlflow.log_metric("Precision", report['precision'])
        mlflow.log_metric("Recall", report['recall'])
        mlflow.log_metric("F1-Score", report['f1-score'])

