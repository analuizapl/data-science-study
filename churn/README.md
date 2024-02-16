# Churn 
This repository contains a Python script (createdata.py) to generate synthetic data for insurance claims and a Jupyter Notebook (churn.ipynb) for churn analysis using machine learning techniques.

# Data Generation 
The createdata.py script generates synthetic data for insurance claims. It follows these steps:

Loads car model data from Car_Models.csv.

Generates fake insurance data using the Faker library, including customer information, insurance situations, outcomes, and car models.

Merges the generated data with the car model data based on random car models.

Adds additional columns such as the count of claims, situation dates, and customer IDs.

Saves the generated dataset to a CSV file named insurance_df.csv.


# Notebook Description
The churn.ipynb notebook contains the following sections:

Data Loading and Preprocessing: Loading the insurance dataset, handling missing values, and converting data types.

Exploratory Data Analysis (EDA): Exploring the dataset through visualization and correlation analysis.

Feature Engineering: Dropping unnecessary columns, encoding categorical variables, and selecting relevant features for modeling.

Model Training and Evaluation: Splitting the dataset into train and test sets, training a Random Forest Classifier, and evaluating the model's performance.


# Insurance Claims Data
The insurance claims data includes the following columns:

Costumer_name: Name of the customer.

Costumer_age: Age of the customer.

Type_situation: Type of insurance situation (e.g., Collision, Fire, Robbery).

Outcome_insurance: Outcome of the insurance claim (e.g., APPROVED, DENIED, NOT USED).

Days_to_fix: Number of days taken to fix the issue.

Active_user: Indicates whether the customer is an active user (0 or 1).

Car_model: Model of the car involved in the insurance claim.

Year: Year of the car model.

Count_claims: Number of claims made by the customer.

Situation_Date: Date of the insurance situation.

Costumer_id: Unique ID assigned to each customer.
