# Updates and additional topics

This file contains various updates to the book and additional help requested over github issues.

## Clone this repository within your Azure Machine Learning workspace

To clone the code in your workspace, open a terminal and use the following command:

``` bash
git clone https://github.com/PacktPublishing/Microsoft-Certified-Azure-Data-Scientist-Associate-Certification-Guide.git book
```

This command will clone this repository into the `book` folder. If you refresh the **Files** tree, you should be able to see the new folder.
![Cloning repository in AzureML](./auxiliary/images/Clone_Code_In_Terminal.png)

To pull the latest version of the codebase, you will first need to revert any changes made to your working copy and then pull the new version. You can do that using the following code:

``` bash
git checkout .
git pull
```

The following image shows what will happen if you have changes in your working copy that conflict with the changes on the remote GitHub server. This image also shows how to revert all local changes and then pull the latest version from the remote GitHub server.

![Pulling newer code version in AzureML](./auxiliary/images/Pull_Newer_Version.png)

## February 2022 updates on the book

- On page 213 the text mentions the `upload() method` when it is actually `upload_files() method`. Moreover, both `upload()` and `upload_files()` methods [are deprecated from the SDK](https://docs.microsoft.com/python/api/azureml-core/azureml.data.azure_storage_datastore.azureblobdatastore?view=azure-ml-py#azureml-data-azure-storage-datastore-azureblobdatastore-upload-files) and may be removed in the future. If the code snippet doesn’t work for you, you can upload the files through the Azure portal or use the [`Dataset.File.upload_directory()`](https://docs.microsoft.com/python/api/azureml-core/azureml.data.dataset_factory.filedatasetfactory?view=azure-ml-py#azureml-data-dataset-factory-filedatasetfactory-upload-directory) method instead.
- On page 284, the quotes did not print correctly. The proper code snippet is the following:

  ```python
  from azureml.core import Workspace, Environment
  from azureml.core.conda_dependencies import CondaDependencies 
  import sklearn
  
  ws = Workspace.from_config()
  diabetes_env = Environment(name="diabetes-training-env")
  diabetes_env.python.conda_dependencies = CondaDependencies.create(
   conda_packages=[f"scikit-learn=={sklearn.__version__}"],
   pip_packages=["azureml-defaults", "azureml-dataprep[pandas]"])
  target = ws.compute_targets['cpu-sm-cluster']
  ```

- On page 293, the quotes did not print correctly. Moreover, the `AzureML-Minimal` environment is only accessible through the `Environment.get(ws, "AzureML-Minimal")` reference and not the `ws.environments["AzureML-Minimal"]` notation that was used earlier in the book. The proper code snippet is the following:

  ```python
  from azureml.core import Workspace, ScriptRunConfig, Environment

  ws = Workspace.from_config()
  target = ws.compute_targets["cpu-sm-cluster"]

  script = ScriptRunConfig(
      source_directory="termination-policy-training",
      script="training.py",
      environment=Environment.get(ws, "AzureML-Minimal"),
      compute_target=target,
  )
  ```

- On page 347, the `AzureML-Tutorial` environment is only accessible through the `Environment.get(ws, "AzureML-Tutorial")` reference and not the `ws.environments["AzureML-Tutorial"]` notation that was used earlier in the book. The proper code snippet is the following:

  ```python
  from azureml.core import RunConfiguration, Environment

  runconfig = RunConfiguration()
  runconfig.environment = Environment.get(ws, 'AzureML-Tutorial')
  ```