# ML Ops with GitHub Actions, DagsHub and AWS EC2 Instance 

<p align="center">
  <img src="./images/mlops_dagshub.png" alt="DagsHub + Actions + EC2" height="200"/>
</p>

This repository can be used for easily setting up a data science or machine learning project with automated training and deployment using [GitHub Actions](https://github.com/features/actions), [DagsHub](https://dagshub.com/) and [AWS EC2](https://aws.amazon.com/fr/ec2/). 
## Main Concepts Covered 
The following concepts are automatically performed using Github Actions and DagsHub.
- Automatically pull and process data from Github. 
- Train your model and track experiment with MLFlow
- Save your data, model and metadata to DVC 
- Deploy your model to AWS EC2 instance.

[TODO] 

# Getting started 
### 1. Prerequisites
#### Platforms
The following prerequisites are required to make this repository work:
- AWS subscription
- Access to [DagsHub](https://dagshub.com/)
- Access to [GitHub Actions](https://github.com/features/actions)

#### Other ressources
- Python 3.9.1 
- DVC 2.11  
- You can find all the additional information in the `requirements.txt` file

#### Main Components of Github Actions
GitHub Actions contains five main components as shown below. 

<p align="center">
  <img src="./images/github_actions_steps.png" alt="GitHub Actions Components" height="300"/>
</p>


## Results On DagsHub
DagsHub provides the capabilities to use MLFlow and DVC while giving the choice of working on Github. The following results are the experiments from DagsHub, using MLFlow to track the model `F1-Score`, `Precision` and `Recall`.

<p align="center">
  <img src="./images/experiments.png" alt="Experiment on DagsHub" height="300"/>
</p>

## Github Actions Experiment 
The following animation corresponds to the execution of the pipeline using Github Actions from Data Extraction to Model Training. 

<p align="center">
  <img src="./images/github_actions_pipeline.png" alt="Github Actions Experiment" height="300"/>
</p>


## Test App Locally
This is the test performed lically, to make sure everything is working before deploying into production. 


## Deploy into Production with Github Actions
Final result after deploying into production environment

