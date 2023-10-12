# **<center>Heart Disease Prediction</center>** 
##### **<center>Category: Machine Learning Algorithms</center>**
##### **<center>ML Tool: Scikit-learn</center>**

## 
This is a django app that can be added in the INSTALLED_APPS list in your django project settings.py.
Made it an app so that I could add it in my website portfolio

## Summary
A Django web app onto which a machine learning model for detecting heart disease has been deployed so as to provide clinicians with a tool to aid in the early diagnosis of cardiac issues. As a result, it will be simpler to successfully treat patients and prevent negative consequences.

The system uses vast amounts of data that the healthcare sector gathers to forecast the likelihood that patients will develop heart disease. Predictions are made based on these data using variables like age, sex, blood pressure, cholesterol, and obesity. Some advanced machine learning algorithms are utilized to deliver acceptable findings and make wise decisions based on data.

The system's classification algorithms include Support vector machines, Logistic regression, , K-nearest neighbors, Naive bays, and Decision trees. Standard feature selection algorithms like Relief, Minimal redundancy maximal relevance, Least absolute shrinkage selection operator, and Local learning have been used to eliminate redundant and irrelevant features from the system.

## Introduction
A heart attack (Cardiovascular diseases) occurs when the flow of blood to the heart muscle suddenly becomes blocked. From WHO statistics every year 17.9 million dying from heart attack. The medical study says that human life style is the main reason behind this heart problem. Apart from this there are many key factors which warns that the person may/maynot getting chance of heart attack.

<center><img style="float: centre;" src="https://www.insidehook.com/wp-content/uploads/2017/07/heartattack_071217-1.jpg?resize=1200" width="600px"/></center>

## Packages Required

    #loading dataset
    import pandas as pd

    #visualisation
    import matplotlib.pyplot as plt
    %matplotlib inline
    import seaborn as sns

    #EDA
    from collections import Counter
    import pandas_profiling as pp
    import numpy as np

    # data preprocessing
    from sklearn.preprocessing import StandardScaler as ss

    # data splitting
    from sklearn.model_selection import train_test_split

    # Machine Learning Modeling
    from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC

    #saving highest accuracy model for deployment
    import pickle

## Know about Data

This is one of the most used dataset — [Cleveland Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) from the [UCI Repository](https://archive.ics.uci.edu/ml/index.php) - and it contains some medical information of patients which tells whether that person getting a heart attack chance is less or more. Using the information we explored the dataset and classified the target variable using different Machine Learning models, finding out which algorithm was suitable for this dataset.

##### <u>Data Fields</u>

1. <span style="color: red">age</span>
2. <span style="color: red">sex</span>
    - Male = 1
    - Female = 0
3. <span style="color: red">(cp) chest pain type</span>
    - Typical angina = 1
    - Atypical angina = 2
    - Non-anginal pain = 3
    - Asymptomatic = 4
4. <span style="color: red">(trestbps) resting blood pressure</span>
5. <span style="color: red">(chol) serum cholestrol in mg/dl</span>
6. <span style="color: red">(fbs) fasting blood sugar > 120 mg/dl</span>
    - Greater than 120 mg/ml = 1
    - Lower than 120 mg/ml = 0
7. <span style="color: red">(restecg) resting electrocardiographic results</span>
    - Normal = 0
    - ST-T wave abnormality = 1
    - Left ventricular hypertrophy = 2
8. <span style="color: red">(thalach) maximum heart rate achieved</span>
9. <span style="color: red">(exang) exercise induced angina</span>
    - Yes = 1
    - No = 0

    Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood. <br>
It may feel like pressure or squeezing in your chest.

10. <span style="color: red">(oldpeak) ST depression induced by exercise relative to rest</span>
11. <span style="color: red">(slope) the slope of the peak exercise ST segment</span>
    - Upsloping = 1
    - Flat = 2
    - Downsloping = 3
12. <span style="color: red">(ca) number of major vessels (0-3) colored by flourosopy</span>
13. <span style="color: red">(thal) displays the thalassemia</span>
    - Normal = 3
    - Fixed Defect = 6
    - Reversable Defect = 7
14. <span style="color: red">(target) whether the individual will suffer from a heart attack:</span> 
    - 0 = absence
    - 1,2,3,4 = present
