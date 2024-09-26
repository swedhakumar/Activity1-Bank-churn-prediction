# Activity1-Bank-churn-prediction
 Bank Churn Prediction
This project predicts customer churn in a bank based on various customer attributes. It uses machine learning algorithms to classify customers who are likely to churn (exit the bank) and those who are likely to stay.

Table of Contents
Project Overview
Dataset
Installation
Exploratory Data Analysis (EDA)
Modeling
Decision Tree Classifier
Random Forest Classifier
Model Persistence
Results
Conclusion
License
Project Overview
Customer churn is a significant issue for businesses, and predicting which customers are likely to churn can help businesses take necessary actions to retain them. This project uses a dataset of bank customers and builds a machine learning model to predict whether a customer will churn based on their characteristics such as age, balance, number of products, etc.

Dataset
The dataset used in this project is the Churn_Modelling.csv file, which contains information about 10,000 customers. It includes the following columns:

RowNumber: Row index.
CustomerId: Unique customer identifier.
Surname: Customer surname.
CreditScore: Customer's credit score.
Geography: Customer's location.
Gender: Customer's gender.
Age: Customer's age.
Tenure: Number of years the customer has been with the bank.
Balance: Customer's bank balance.
NumOfProducts: Number of products the customer has with the bank.
HasCrCard: Whether the customer has a credit card (1=Yes, 0=No).
IsActiveMember: Whether the customer is an active member (1=Yes, 0=No).
EstimatedSalary: Customer's estimated salary.
Exited: Whether the customer churned (1=Yes, 0=No).
Preprocessing:
Dropped irrelevant columns such as RowNumber, CustomerId, and Surname.
Converted categorical variables (Geography and Gender) into numerical variables using one-hot encoding.
Installation
Requirements
Python 3.x
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Pickle
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/bank-churn-prediction.git
Install the required libraries:

bash
Copy code
pip install numpy pandas matplotlib seaborn scikit-learn
Open the Jupyter notebook or Python script to run the project.

Exploratory Data Analysis (EDA)
We performed exploratory data analysis using Seaborn and Matplotlib to understand relationships between features and customer churn.

Pair Plot: Visualized the relationships between different numerical features.
Count Plots: Checked distributions of categorical features like Gender, Geography, HasCrCard, IsActiveMember, etc., and their relationships with the target Exited.
Box Plots: Analyzed how numerical features like Age, Balance, CreditScore, and EstimatedSalary vary between customers who exited and those who didn't.
Correlation Matrix: We computed a correlation matrix to identify relationships between features and used a heatmap to visualize this.

Modeling
We built and evaluated two machine learning models:

1. Decision Tree Classifier
Train-Test Split: The dataset was split into training and testing sets using an 80-20 ratio.
Model: A decision tree classifier was used to predict churn.
Evaluation:
Confusion matrix.
Classification report (precision, recall, f1-score).
Accuracy score.
2. Random Forest Classifier
Model: A random forest classifier was trained and evaluated.
Evaluation: Similar evaluation metrics were used as for the decision tree classifier.
Model Performance
Both models were compared based on their accuracy and classification reports.

Model Persistence
The Random Forest model was saved using the pickle library for future use. This allows us to reload the model without having to retrain it.

python
Copy code
import pickle

# Save the model
Pkl_Filename = "bcp.pkl"
pickle.dump(random_obj, open(Pkl_Filename, 'wb'))

# Load the model
with open(Pkl_Filename, 'rb') as file:
    Pickled_Model = pickle.load(file)

# Score the model
score = Pickled_Model.score(X_test, y_test)
print(f"Test score: {score * 100:.2f} %")
Results
Decision Tree Classifier achieved an accuracy of X%.
Random Forest Classifier achieved an accuracy of Y% and performed better overall.
The confusion matrix and classification report for both models are provided, showing how well they predict churn vs. non-churn.

Conclusion
The Random Forest Classifier performed better than the Decision Tree Classifier, and with further tuning, it could be even more effective at predicting customer churn.

Predicting churn can help banks understand customer behavior and take proactive steps to retain customers.

License
This project is licensed under the MIT License - see the LICENSE file for details.
