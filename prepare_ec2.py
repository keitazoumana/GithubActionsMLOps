    from yaml import safe_load 
    from os.path import join
    import os

    #####  Source Code Access  
    ec2_prepare_params = safe_load(open("params.yaml"))["ec2_prepare"]
    DAGSHUB_REMOTE_URL = ec2_prepare_params["DAGSHUB_REMOTE_URL"]
    DEPENDENCIES = ec2_prepare_params["REQUIREMENTS"]

    # 1. Clone the source code
    os.system("git clone {DAGSHUB_REMOTE_URL}")

    #### Model and Data Parameters
    model_data_params = safe_load(open("params.yaml"))["model_data_config"]
    MODEL_PATH = model_data_params["MODEL_PATH"]
    DATA_PATH = model_data_params["METRICS_PATH"]

    # 2. Pull data and model
    os.system("dvc pull {MODEL_PATH} {DATA_PATH}")

    # 3. Install the requirements
    os.system("pip install -r {DEPENDENCIES}")
