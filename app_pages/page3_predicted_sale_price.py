import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance, evaluate_and_display

def page3_predicted_sale_price():

    # Load pipeline files
    version = 'v1'
    regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predictsale_price/regressor_pipeline.pkl")
    house_features = pd.read_csv(f"outputs/ml_pipeline/predictsale_price/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predictsale_price/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predictsale_price/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predictsale_price/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predictsale_price/y_train.csv")
    y_test = pd.read_csv(f"outputs/ml_pipeline/predictsale_price/y_test.csv")

# Display ML pipeline summary
st.write("### ML Pipeline: Predict Sale Price")    
st.info(
    f"* The ML Pipeline addresses the **second business requirement**: \n\n"
    f"* Delivering an ML system for predicting the sale price of the inherited houses. \n\n"
    f"* A **Regressor model** was selected for predicting the **Sale Price**, following additional data cleaning and feature engineering. "
    f"The client set a target R2 score of at least 0.75 on both train and test sets. \n\n"
    f"* Achieved R2 score: **0.93** on the test set and **0.83** on the train set. \n\n"
)

st.write("---")

# Display pipeline details
st.write("* ML pipeline used for predicting Sale Price")
st.write(regressor_pipeline)
st.write("---")

# Display feature importance and model features
st.write("* Features used for training and their importance")
st.write(X_train.columns.to_list())
st.image(sale_price_importance)
st.write("---")

# Evaluate and display performance
st.write("### Pipeline Performance")
regression_performance(
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    pipeline=regressor_pipeline
)
