import packages.data_management as dm

path_to_data = "./git_actions_data/raw/spam.csv"
saving_folder = "./git_actions_data/preprocessed"
final_file_name = "spam_preprocessed.csv"

dm.prepare_data(path_to_data, saving_folder, final_file_name, encoding="latin-1")