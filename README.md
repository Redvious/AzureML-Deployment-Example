# Azure ML Deployment Example

This repository demonstrates how to deploy a simple Iris classification model using Azure Machine Learning.

## Steps

1. **Register the Model**:
   - The trained model is saved in `model.pkl`.

2. **Deploy the Model**:
   - Run `deploy.py` to deploy the model to Azure ML.

3. **Test the Endpoint**:
   - Run `test_endpoint.py` to send requests to the deployed endpoint.

## Prerequisites

- An active Azure subscription.
- Python dependencies installed (see `environment.yml`).