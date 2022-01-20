# GCP AutoML Demonstration

### Create a service account {#service-account}
Create an account with **AutoML Admin role** and download the key as json file. After the credentials are downloaded set the environment variable **GOOGLE_APPLICATION_CREDENTIALS** as the absolute path to the credentials file.

```bash
$ GOOGLE_APPLICATION_CREDENTIALS="absolute/path/to/credentials"
```
[Use this link to know how to set up one](https://developers.google.com/android/management/service-account)

### Install dependencies
Run the following code in the terminal or virtual environment to install the required dependencies.
```bash
$ pip install -r requirements.txt --upgrade
```
### Run the code

Replace the project_id variable with your project_id on line 3 of [index.py](./index.py).
```python
project_id = "your_project_id"
```

Replace gs bucket path to the dataset with your own path in the file [index.py](./index.py), line number 4.

```python
path = "gs://path/to/your/dataset"
```
On line number 5 of [index.py](./index.py) change the display_name variable to anything that you want it to be reflected on the dataset and model.

```python
display_name="<any_display_name>"
```
***
> **NOTE**
Do not use any special character other than **underscore** ( _ )
***
And then run the script using the following command.

```bash
$ python index.py
```
OR
``` bash
$ python3 index.py
```

### Check the console for messeges

Go to [Tables datasets](https://console.cloud.google.com/automl-tables/datasets) to view your dataset.

Go to [Tables models](https://console.cloud.google.com/automl-tables/models) to view your model.