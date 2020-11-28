# Churn dataset

Fabricated dataset for churn prediction. The `churn-dataset.parquet` file is used for training models and the `churn-test-cases.csv` is used for unit testing the produced models.

Features in the dataset:

- `id`: Customer Id
- `customer_tenure`: How many years the customer has subscribed
- `product_tenure`: How long is the customer in the specific product
- `activity_last_6_months`: Minutes talked on phone last 6 months in total
- `activity_last_12_months`: Minutes talked on phone last 12 months in total
- `churned`: Bool indicating if the customer churned