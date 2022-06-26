    from yaml import safe_load 
    from os.path import join
    import os

    #####  Source Code Access  
    ec2_prepare_params = safe_load(open("params.yaml"))["ec2_prepare"]
    DAGSHUB_REMOTE_URL = ec2_prepare_params["DAGSHUB_REMOTE_URL"]
    EC2_KEY_PAIR = ec2_prepare_params["EC2_KEY_PAIR"]

    # EC2 User Access 
    ec2_user_params = safe_load(open("params.yaml"))["host_information"]
    EC2_HOST = ec2_user_params["HOST"]
    EC2_USER = ec2_user_params["EC2_USER"]
    EC2_IP_ADDRESS = ec2_user_params["EC2_IP"]
    EC2_REMOTE_DIRECTORY = ec2_user_params["EC2_REMOTE_DIRECTORY"]

    # Dockerfile and app.py file
    meta_data = safe_load(open("params.yaml"))["meta_data"]
    DOCKERFILE = meta_data["DOCKERFILE"] 
    APP_FILE = meta_data["APP"] 

    # 1. Give the execution right to the KEY_PAIR FILE
    os.system("chmod 400 {EC2_KEY_PAIR}")

    # 2. Connect to the instance and get relevant files 
    os.system("ssh {EC2_HOST}")

    # Copy the metadata to EC2 
    os.system("scp {DOCKERFILE} {APP_FILE} {EC2_USER}@{EC2_IP_ADDRESS}:/{EC2_REMOTE_DIRECTORY}")

    #### Model and Data Parameters
    model_data_params = safe_load(open("params.yaml"))["model_data_config"]
    MODEL_PATH = model_data_params["MODEL_PATH"]
    DATA_PATH = model_data_params["METRICS_PATH"]

    # Configure DVC 


    # 2. Pull data and model
    os.system("dvc pull {MODEL_PATH} {DATA_PATH}")

    # 4. Run the docker container 
    os.system("docker build -t fastapiapp:latest -f {DOCKERFILE} .")
    os.system("docker run -p 80:80 fastapiapp:latest")