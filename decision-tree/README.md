# Decision Tree Classifier
This repository contains a Python scripts that demonstrates the use of a Decision Tree Classifier to analyze some datasets. The code utilizes scikit-learn's DecisionTreeClassifier to create the tree and also evaluates its performance. The resulting decision tree is visualized using matplotlib.

# Files
1. 'decision_tree_sonar.py'
This Python script uses a decision tree classifier to analyze the Sonar dataset. 

# Datasets Descriptions
The Sonar dataset contains data obtained from sonar signals, where each row represents a specific signal sample. The column 'Classe' indicates whether the object detected by the sonar is a mine (Mina) or a rock (Rocha).

# Notes
In the 'decision_tree_sonar.py' even after performing hyperparameter tuning using GridSearchCV, there still seems to be some overfitting in the decision tree model. 
The training accuracy is 1.0 (100%), while the prediction accuracy on the test set is 0.714 (71.43%).
- For the "Mine" class, the precision is 0.60, recall is 0.75, and f1-score is 0.67. This indicates that when the model predicts "Mine," it is correct 60% of the time, and it can identify 75% of the actual "Mine" instances.
- For the "Rock" class, the precision is 0.82, recall is 0.69, and f1-score is 0.75. The model performs better for the "Rock" class, with higher precision and f1-score.
The overall accuracy on the test set is not bad. However, analyzing the numbers in the classification report, it suggests that the model may not generalize well for both classes. The lower recall for the "Rock" class indicates that the model might be biased towards predicting "Mine" more often.
