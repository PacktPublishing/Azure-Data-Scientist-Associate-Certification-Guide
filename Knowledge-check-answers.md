# Knowledge check answers

In most of the book's chapters, you will find a couple of questions that will allow you to perform a knowledge check on the topics discussed in the corresponding chapter.
This page provides the answers to those questions.

> Note that when possible, it is recommended to [transition to the v2 platform](https://learn.microsoft.com/azure/machine-learning/how-to-migrate-from-v1), since v1 is scheduled to reach it's end of life. In the answers we provides links to both versions, when applicable.

## Chapter 2

- *Which of the following are applicable ways of deploying the Azure ML workspace?*

  All of the options are correct:

  - You can deploy through Azure CLI with either [v1](https://learn.microsoft.com/azure/machine-learning/v1/how-to-manage-workspace-cli?tabs=createnewresources) or [v2](https://learn.microsoft.com/azure/machine-learning/how-to-configure-cli?tabs=public#set-up) AzureML CLI extensions.
  - You can [create a workspace from the Azure portal](https://learn.microsoft.com/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal).
  - You can use [ARM templates](https://learn.microsoft.com/azure/machine-learning/how-to-create-workspace-template?tabs=azcli) or even [Terraform](https://learn.microsoft.com/azure/machine-learning/how-to-manage-workspace-terraform?tabs=publicworkspace) to deploy a workspace.
  - You can deploy a workspace with either [v1](https://learn.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py#workspace) or [v2](https://learn.microsoft.com/azure/machine-learning/how-to-manage-workspace?tabs=python) python SDKs.

- *You are creating a custom role and you want to deny the ability to delete a workspace. Where do you need to add the `Microsoft.MachineLearningServices/workspaces/delete` action?*

  According to the [Manage users and roles](https://learn.microsoft.com/azure/machine-learning/how-to-assign-roles) page, in order to deny that action, you need to add it in the `NotActions` section of the custom role definition.

- *What do you have to install in the Azure CLI before you can deploy an Azure ML workspace?*
  
  You will need to install either the [v1](https://learn.microsoft.com/azure/machine-learning/v1/reference-azure-machine-learning-cli) or the [v2](https://learn.microsoft.com/azure/machine-learning/how-to-configure-cli) AzureML CLI extension.

## Chapter 4

- *How many data scientists can work on a single compute instance that has 8 cores and 56 GB of RAM?*

  According to [the official documentation](https://learn.microsoft.com/azure/machine-learning/concept-compute-instance), "each compute instance has only one owner, although you can share files between multiple compute instances". This means that no matter how many cores it has, it can only be used by a single person.

- *What type of credentials do you need to provide to access a data lake store that's either Gen 1 or Gen 2?*

  For the purposes of the DP-100 exam, the answer is that you need to specify the *service principal credentials* which will be used to access the data, as seen in the [yaml syntax](https://learn.microsoft.com/azure/machine-learning/how-to-datastore?tabs=cli-identity-based-access%2Ccli-adls-sp%2Ccli-azfiles-account-key%2Ccli-adlsgen1-identity-based-access#create-an-azure-data-lake-gen2-datastore). The platform has evolved though and you can use the more secure approach of [identity-based data access](https://learn.microsoft.com/azure/machine-learning/how-to-identity-based-service-authentication?tabs=cli#accessing-storage-services) which is supported in Azure Blob storage and both Azure Data Lake Store (ADLS) Gen 1 and Gen 2.

- *Which of the following Azure tools can help you orchestrate data moving from an on-premises environment?*

  [Azure Data Factory](https://learn.microsoft.com/azure/data-factory/introduction) is the defacto tool to orchestrate data movements within Azure. You can potentially [code some small data movement within an AzureML job](https://learn.microsoft.com/azure/machine-learning/how-to-read-write-data-v2?tabs=cli) but you will probably miss features like auto-scale, auto-resume of failed movements and the rest of the enterprise grade features, like traceability, that Azure Data Factory offers.

## Chapter 5

- *You need to train a classification model but only consider linear models during the AutoML process. Which of the following allows you to do that in the Azure Machine Learning Studio experience?*

  You will need to add all algorithms besides the linear ones in the `Blocked algorithms` option of the [Automated ML wizard](https://learn.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml).

## Chapter 6

Note that the designer has been updated recently to incorporate more features. The core concepts remain the same even if [the deployment of the real time endpoint process has changed a bit](https://learn.microsoft.com/azure/machine-learning/tutorial-designer-automobile-price-deploy).

- *What are the options for deploying real-time pipelines?*

  For the purposes of the DP-100 exam, the answer is that you can deploy in either Azure Container Instances (ACI) and Azure Kubernetes Services (AKS), which is the 2nd option in the list of answers. Note that ACI should only be used for development purposes or for very small scale projects where you don't care about high availability or other enterprise grade features.

## Chapter 7

- *What is the default minimum number of nodes for an AzureML compute cluster?*

  The default minimum number of nodes is 0.

- *You upload a CSV file to the default datastore that contains credit card transaction details. Which of the following methods should you use to create a dataset reference?*

  You can use either the [`Dataset.File.from_files()`](https://learn.microsoft.com/python/api/azureml-core/azureml.data.dataset_factory.filedatasetfactory?view=azure-ml-py#azureml-data-dataset-factory-filedatasetfactory-from-files) or the [`Dataset.Tabular.from_delimited_files()`](https://learn.microsoft.com/python/api/azureml-core/azureml.data.dataset_factory.tabulardatasetfactory?view=azure-ml-py#azureml-data-dataset-factory-tabulardatasetfactory-from-delimited-files) methods depending on whether you want to load the csv as a file or a tabular dataset. These are options a and b in the book. In v2, you can [use URIs to access the file](https://learn.microsoft.com/azure/machine-learning/how-to-access-data-interactive?tabs=adls#examples) or use [the MLTable construct](https://learn.microsoft.com/azure/machine-learning/concept-data?tabs=uri-file-example%2Ccli-data-create-example#mltable) to read the CSV file as tabular data.

- *How can you force the creation of a blob container during the registration process of an Azure blob-based datastore?*

  For the purposes of the DP-100 exam, you should pass the `create_if_not_exists=True` parameter to the [`Datastore.register_azure_blob_container()` method](https://learn.microsoft.com/python/api/azureml-core/azureml.core.datastore(class)?view=azure-ml-py#azureml-core-datastore-register-azure-blob-container). This is option b in the book. In v2, the container needs to exists before registering it using [the code shown in the docs](https://learn.microsoft.com/azure/machine-learning/how-to-datastore#create-an-azure-blob-datastore).

## Chapter 8

- *You want to log the number of validation rows you will use within a script. Which method of the Run class will you use?*

  The number of validation rows is a scalar value, so you would use the `log` method. This is option c in the book. See the [Remarks section or the Run Class]((https://learn.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#remarks)) for more logging examples.

- *You want to run a Python script that utilizes `scikit-learn`. How would you configure the AzureML environment?*

  You will need to add the `scikit-learn` [Conda dependency in the environment](https://learn.microsoft.com/azure/machine-learning/how-to-train-scikit-learn#create-a-custom-environment). This is option a in the book. The `sklearn` is the package name that you will need to include in your script.

- *You need to use MLflow to track the metrics generated in an Experiment and store them in your AzureML workspace. Which two pip packages do you need to have in your Conda environment?*

  You will need to install both `mlflow` and `azureml-mlflow` packages. These are options a and b in the book. The first one brings the MLflow SKD and the second one provides the AzureML integration. See an example in [this Microsoft learn page](https://learn.microsoft.com/azure/machine-learning/how-to-use-mlflow-cli-runs?tabs=aml%2Ccli%2Cmlflow).

- *You need to use MLflow to track the value 0.1 for the training_rate metric. Which of the following code achieves this requirement? Assume all classes are correctly imported at the top of the script:*

  You will need to use `mlflow.log_metric('training_rate', 0.1)` which is option a in the book.

## Chapter 9

- *You want to get the best model trained by an AutoML run. Which code is correct?*

  The [`run.get_output()` method](https://learn.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#azureml-train-automl-run-automlrun-get-output) returns the run and the corresponding fitted model, so you need the `model = run.get_output()[1]` which is option b in the book.

- *You want to run a forecasting AutoML experiment on top of data you receive from a sensor. You receive one record every day from the sensor. You want to be able to predict the values for 5 days. Which of the following parameters should you pass to the ForecastingParameters class?*

  The [`forecast_horizon` parameter](https://learn.microsoft.com/python/api/azureml-automl-core/azureml.automl.core.forecasting_parameters.forecastingparameters?view=azure-ml-py#azureml-automl-core-forecasting-parameters-forecastingparameters-forecast-horizon) uses the same unit as the time interval of the training data. In this case you have 1 day as the training data time interval, thus option a, `forecast_horizon = 5`, is the correct answer (the `* 1` part was used as a distraction to match the rest of the answers which refer to either hour time scale or half day time scale correspondingly).

## Chapter 10

- *You are using `TabularExplainer` to interpret a sklearn
`DecisionTreeClassifier`. Which underlying SHAP explainer will be used?*

  The `TreeExplainer` will be used, which is option b.

- *You want to interpret a sklearn `DecisionTreeClassifier` using `MimicExplainer`. Which of the following models can you use for the explainable_model parameter?*

  Although a `DecisionTreeExplainableModel` may be the closest option to the original model, regarding its structure, you can use any surrogate model, which is option e in the book.

- *Can you use PFIExplainer to produce local feature importance values?*

  PFI explainer cannot be used to create local or instance-level feature importance.

## Chapter 11

- *What affects the execution order of the pipeline steps?*

  The correct answer is option b because only the data dependencies between the steps affect their execution order.

- *True or false: All steps within a pipeline need to execute within the same compute target and `Environment`.*

  False. Each step can leverage different compute and/or `Environment`.

- *True or false: `PythonScriptStep`, by default, reuses the previous execution results if nothing has changed in the parameters or the code files.*

  True, reuse is enabled by default ([`allow_reuse=True`](https://learn.microsoft.com/python/api/azureml-pipeline-steps/azureml.pipeline.steps.pythonscriptstep?source=recommendations&view=azure-ml-py#parameters)).

- *You are trying to debug a child run execution issue. Which of the following methods should you call in the `StepRun` object?*

  Use option b, the [`get_details_with_logs()` method](https://learn.microsoft.com/python/api/azureml-pipeline-core/azureml.pipeline.core.steprun?view=azure-ml-py#azureml-pipeline-core-steprun-get-details-with-logs).

- *You have just defined a pipeline in Python code. What steps do you need to make to schedule a daily execution of that pipeline?*

  You will need to publish the pipeline and create a `ScheduleRecurrence` that is referencing the published pipeline's id and has `Day` as the frequency parameter. You will then need to create a `Schedule` using the `Schedule.create()` method. See the [Remarks section for a full example](https://learn.microsoft.com/python/api/azureml-pipeline-core/azureml.pipeline.core.schedulerecurrence?view=azure-ml-py#remarks).

## Chapter 12

- *You want to deploy a real-time endpoint that will handle transactions from a live betting website. The traffic from this website will have spikes during games and will be very low during the night. Which of the following compute targets should you use?*

  Azure Kubernetes Service (AKS) is the defacto for deploying production ready workloads. This is option d in the book. In the v2 platform you can leverage [the online endpoints that support autoscaling](https://learn.microsoft.com/azure/machine-learning/how-to-autoscale-endpoints?tabs=azure-cli).

- *You want to monitor a real-time endpoint deployed in AKS and determine the average response time of the service. Which monitoring solution should you use?*

  You can use [Application Insights to monitor and collect data from the web endpoints](https://learn.microsoft.com/azure/machine-learning/v1/how-to-enable-app-insights). This is option c in the book. In the v2 platform you can also get [similar metrics using the process described in the Microsoft learn page](https://learn.microsoft.com/azure/machine-learning/how-to-monitor-online-endpoints).

- *You have a computer vision model, and you want to process 100 images in parallel. You author a pipeline with a parallel step. You want to process 10 images at a time. Which of the following ParallelRunConfig parameters should you set?*

  Images will be part of a FileDataset input. The [`mini_batch_size`](https://learn.microsoft.com/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunconfig?view=azure-ml-py#parameters) will indicate the number of files the user script can process in one run() call. This means that `mini_batch_size=10`, which is option a in the book, is the correct answer.
