import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Loading the sonar dataset
sonar = pd.read_csv(r'C:\Users\Ana Luiza\Desktop\Git\Github\data-science-study\decision-tree\sonar.csv') 

# Print information about the dataset
print("Dimensions: {0}".format(sonar.shape))
print(sonar.describe(), sep='\n')

# Extracting features (X) and target (y) from the dataset
X = sonar.iloc[:, 0:(sonar.shape[1] - 1)]

# The target variable is converted to numerical values
le = LabelEncoder()
y = le.fit_transform(sonar.iloc[:, (sonar.shape[1] - 1)])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.1)

# Creating a Decision Tree Classifier
sonar_tree = DecisionTreeClassifier(random_state=0, criterion='entropy')

# Performing GridSearchCV for hyperparameter tuning
# Trying different values for maximum depth, minimum samples split and minimum samples leaf
param_grid = {
    'max_depth': [3, 5, 7, None],  
    'min_samples_split': [2, 5, 10], 
    'min_samples_leaf': [1, 2, 4]  
}

grid_search = GridSearchCV(estimator=sonar_tree, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Using the best estimator from GridSearchCV
sonar_tree = grid_search.best_estimator_

# Evaluating the model's accuracy on the training set
print("Training accuracy:", sonar_tree.score(X_train, y_train))

# Predicting the target values for the test set
y_pred = sonar_tree.predict(X_test)

# Evaluating the accuracy for the test set
print("Prediction accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["Mine", "Rock"]))

# Generate a confusion matrix and create a table for better visualization
cnf_matrix = confusion_matrix(y_test, y_pred)
cnf_table = pd.DataFrame(data=cnf_matrix, index=["Mine", "Rock"], columns=["Mine (prev)", "Rock (prev)"])
print(cnf_table)

# Plot the decision tree directly using scikit-learn's plot_tree method
plt.figure(figsize=(15, 10))
plot_tree(sonar_tree, filled=True, feature_names=sonar.columns[:-1], class_names=["mine", "rock"])
plt.savefig(r'C:\Users\Ana Luiza\Desktop\Git\Github\data-science-study\decision-tree\sonar-tree.png')
