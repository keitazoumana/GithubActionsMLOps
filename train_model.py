# Packages
import joblib
import pandas as pd

# Get customized functions from library
import packages.data_management as dm
import packages.model_trainer as mt


# 0.Path to prepared data
path_to_data = './data/preprocessed/spam_preprocessed.csv'

# 1.Read the prepared data
prepared_data = pd.read_csv(path_to_data)

# 2.Create train - test split
train_test_data, vectorizer = dm.create_train_test_data(prepared_data['text'], 
                                         prepared_data['label'], 
                                         0.25, 2021)

# 3.Run training
model, report = mt.run_model_training(train_test_data['x_train'], train_test_data['x_test'], 
                           train_test_data['y_train'], train_test_data['y_test'])

# 4.Save the trained model the vectorizer and metrics
joblib.dump(model, './models/spam_detector_model.pkl')
joblib.dump(vectorizer, open("./vectors/vectorizer.pickle", "wb")) 

# Save the metrics
saving_folder = "./data/metrics"
final_file_name = "metrics.json"
dm.save_metrics(report, saving_folder, final_file_name)
