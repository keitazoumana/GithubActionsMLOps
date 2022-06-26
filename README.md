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

## Results On DagsHub
DagsHub provides the capabilities to use MLFlow and DVC while giving the choice of working on Github. The following results are the experiments from DagsHub, using MLFlow to track the model `F1-Score`, `Precision` and `Recall`.

<p align="center">
  <img src="./images/experiments.png" alt="Experiment on DagsHub" height="200"/>
</p>

## Github Actions Experiment 
The following animation corresponds to the execution of the pipeline using Github Actions from Data Extraction to Model Training. 

<p align="center">
  <iframe width="420" height="315"
    src="https://gfycat.com/blackandwhitearctichyracotherium">
  </iframe>
</p>

## Test App Locally

## Deploy into Production with Github Actions

<p align="center">
  <iframe width="420" height="315"
    src="https://gfycat.com/kaleidoscopicjointblueandgoldmackaw">
  </iframe>
</p>
