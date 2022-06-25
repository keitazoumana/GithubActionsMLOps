import packages.data_management as dm

URL = "https://raw.githubusercontent.com/keitazoumana/Fastapi-tutorial/master/data/spam.csv"
folder = "./data/raw"
final_file_name = "spam.csv"
    
dm.acquire_data(URL, folder, final_file_name)