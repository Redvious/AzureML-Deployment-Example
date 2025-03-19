from azureml.core import Workspace, Model, Environment
from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig

# Load the workspace from the config.json file
try:
    ws = Workspace.from_config()
    print(f"Workspace name: {ws.name}")
    print(f"Subscription ID: {ws.subscription_id}")
    print(f"Resource group: {ws.resource_group}")
except Exception as e:
    print("Failed to load workspace. Check your config.json file.")
    print(e)
    exit()

# Register the model
model = Model.register(workspace=ws, model_path="model.pkl", model_name="my_model")

# Configure the environment
env = Environment.from_conda_specification(name="my_env1", file_path="environment.yml")

# Register the environment (optional)
env.register(workspace=ws)

# Configure inference
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# Configure deployment (ACI)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Deploy the model
try:
    service = Model.deploy(
        workspace=ws,
        name="irismodel-service",
        models=[model],
        inference_config=inference_config,
        deployment_config=deployment_config,
        overwrite=True
    )
    service.wait_for_deployment(show_output=True)
except Exception as e:
    print(f"Deployment failed: {e}")
    if 'service' in locals():
        print(service.get_logs())
    else:
        print("Service object not created. Check the deployment configuration.")

# Print the endpoint URL
print(f"Endpoint URL: {service.scoring_uri}")