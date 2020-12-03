# Weather data to demonstrate data drift detection

Let's assume you trained a machine learning model using various features, including the temperature and the wind speed ones. The `weather-data-drift-base.parquet` dataset is the training dataset that contains the weather data from 28th of December 2009 to 28th of February 2010. The `weather-data-drift-target.parquet` dataset contains the latest inputs used by the trained model to make inferences. This dataset contains the weather data from 29th of December 2019 to 1st of March 2020.

The goal of data drift detection is understand how different these datasets are, something that would inevitably affect the model's performance since it would be making inferences on data that follow distributions not seen before by the model.

Features in the dataset:

- `datetime`: The timestamp of the measurement. You will find one record every 30 seconds.
- `temperature`: The temperature captured by the meteor station in &deg;C.
- `wind`: The speed of the wind in m/sec.
