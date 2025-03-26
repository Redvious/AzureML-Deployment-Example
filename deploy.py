from azureml.core import Workspace
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig, Model
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies

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

model_path='model.pkl'
model_name='iris__model'

# Register the model
model = Model.register(workspace=ws, model_path=model_path, model_name=model_name)

# Configure the environment
conda_env = Environment.from_conda_specification(
    name="myconda-env",
    file_path="environment.yml"
)
conda_env.register(workspace=ws)

# Configure inference
inference_config = InferenceConfig(entry_script='score.py', environment=conda_env)

# Configure deployment (ACI)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Deploy the model
try:
    service = Model.deploy(workspace=ws,
                           name="iris-prediction-service",
                           models=[model],
                           inference_config=inference_config,
                           deployment_config=deployment_config,
                           overwrite=True)
    service.wait_for_deployment(show_output=True)
except Exception as e:
    print(f"Deployment failed: {e}")
    if 'service' in locals():
        print(service.get_logs())
    else:
        print("Service object not created. Check the deployment configuration.")


print(f"Endpoint URL: {service.scoring_uri}")