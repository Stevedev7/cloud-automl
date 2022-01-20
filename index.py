from google.cloud import automl_v1beta1 as automl

project_id = 'niveustraining'
path = 'gs://test-dataset-automl-bucket/predictive-maintenance/data.csv'
display_name = 'machine_failure'

client = automl.TablesClient(project=project_id, region='us-central1')

def create_dataset(client, dataset_display_name):
    dataset = client.create_dataset(project=project_id, dataset_display_name=dataset_display_name)
    return dataset

def generate_display_name(name):
    import time
    return f'{name}_{(str(int(time.time())))}'

def import_data(client, dataset_display_name, path):
    input_uris = path.split(",")
    response = client.import_data(
        dataset_display_name=dataset_display_name,
        gcs_input_uris=input_uris
    )
    print("Processing import...")
    print("Data imported. {}".format(response.result()))

def set_target_column(client, dataset_display_name, column_name):
    client.set_target_column(dataset_display_name=dataset_display_name, column_spec_display_name=column_name)

def delete_dataset(client, dataset_display_name):
    response = client.delete_dataset(dataset_display_name=dataset_display_name)
    print("Dataset deleted. {}".format(response.result()))

def create_model(client, dataset_display_name, model_display_name):
    response = client.create_model(
        model_display_name,
        train_budget_milli_node_hours=1000,
        dataset_display_name=dataset_display_name
    )

    print("Training model...")
    print("Training operation name: {}".format(response.operation.name))
    print("Training completed: {}".format(response.result()))

def list_models(client):
    response = client.list_models()
    for model in response:
        print(model.display_name)

def deploy_model(client, model_diplay_name):
    response = client.deploy_model(model_display_name=model_display_name)

    # synchronous check of operation status.
    print("Model deployed. {}".format(response.result()))

def undeploy_model(client, model_display_name):
    response = client.undeploy_model(model_display_name=model_display_name)
    print("Model undeployed. {}".format(response.result()))


dataset_display_name=generate_display_name(display_name)
# dataset_display_name = ''
print(f"Creating Dataset {dataset_display_name}")
dataset = create_dataset(client, dataset_display_name)

print(dataset.display_name)

print(f"Importing data")
import_data(client, dataset_display_name, path)


print('setting target column')
set_target_column(client, dataset_display_name, 'Failure_Type')

model_display_name = generate_display_name(display_name)

print(f"Creating model {model_display_name}")
create_model(client, dataset_display_name, model_display_name)



# list_models(client)


deploy_model(client, model_display_name)

# undeploy_model(client, model_display_name)

