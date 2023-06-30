# Titanic Survival Prediction Project

This repository contains code for predicting passenger survival on the Titanic using machine learning techniques. The dataset consists of passenger information such as age, sex, class, and other features that will be used to train the model.


# Dataset
The dataset is loaded from two CSV files: train.csv and test.csv. The data includes the following columns:

PassengerId: A unique identifier for each passenger (numeric, primary key).

Survived: Target variable indicating whether the passenger survived or not (0 = No, 1 = Yes).

Pclass: Passenger class (1 = 1st class, 2 = 2nd class, 3 = 3rd class).

Name: Name of the passenger (categorical).
Sex: Gender of the passenger (categorical).
Age: Age of the passenger (numeric, continuous).
SibSp: Number of siblings/spouses aboard (numeric, discrete).
Parch: Number of parents/children aboard (numeric, discrete).
Ticket: Ticket number (categorical).
Fare: Fare price (numeric, continuous).
Cabin: Cabin number (categorical).
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

# Exploratory Data Analysis
The Jupyter Notebook includes code for exploring the dataset and gaining insights into the data. It performs the following analyses:

Displays data types of each column.
Shows the first 5 entries of the training dataset.
Calculates and displays the percentage of missing values for each column.
Plots histograms for numerical variables.
Analyzes the probability of survival based on gender.
Plots bar charts for survival based on gender, passenger class, and embarkation port.
Analyzes the influence of age on survival probability using distribution plots.
Creates a scatter matrix for selected numerical variables.
