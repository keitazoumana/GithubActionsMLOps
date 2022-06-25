from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd 
import os
import ssl
import json

def acquire_data(URL, saving_folder, final_file_name, data_encoding = 'latin-1'):

    # Create SSL
    ssl._create_default_https_context = ssl._create_unverified_context 
    
    # Read data 
    data = pd.read_csv(URL, encoding=data_encoding)

    # Save data into the folder
    data.to_csv(os.path.join(saving_folder, final_file_name), index=False)


def save_metrics(metrics_dict, saving_folder, final_file_name):

    metrics_saving_path = os.path.join(saving_folder, final_file_name)

    with open(metrics_saving_path, 'w') as fp:
        json.dump(metrics_dict, fp)


def prepare_data(path_to_data, saving_folder, final_file_name, encoding="latin-1"):
    """
        @params:
            - path_to_data: the path to the data
            - encoding: the encoding format to be used

        @return:
            - dictionary with following keys: 
                - text: the actual text message
                - label: the label associated to that text message
    """

    # Read data from path
    data = pd.read_csv(path_to_data, encoding=encoding)

    # Encode labels
    data['label'] = data['v1'].map({'ham': 0, 'spam': 1})

    # Create new text column
    data['text'] = data['v2']

    # Drop the "v2" column
    data.drop('v2', axis=1, inplace=True)

    # Save in a final destination
    data.to_csv(os.path.join(saving_folder, final_file_name), index=False)


def create_train_test_data(X, y, test_size, random_state):
    cv = CountVectorizer()
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        random_state=random_state)

    return {'x_train': X_train, 'x_test': X_test,
            'y_train': y_train, 'y_test': y_test}, cv

