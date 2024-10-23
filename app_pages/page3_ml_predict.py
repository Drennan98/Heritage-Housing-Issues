import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file, load_inherited_house_data
from src.machine_learning.evaluate_regression import regression_performance, evaluate_and_display
from src.machine_learning.predictive_analysis_ui import predict_price
from datetime import date

def page3_ml_predict():

    version = 'v1'
    sale_price_pipeline = load_pkl_file(f"outputs/ml_pipeline/predictsale_price/v1/regression_pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predictsale_price/v1/X_train.csv")
                                        .columns
                                        .to_list())

    st.write("### Predict House Sale Price")

    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* The client is interested to predict the house sale price for "
        f"her 4 inherited houses, and any other house in Ames, Iowa. ")
    st.write("---")
    st.write("The data of the houses you want an estimated price for can be entered below. "
			"If you are missing any values of the data set, they're set to median. ")
    
    in_df = load_inherited_house_data()
    first_house_data = in_df.iloc[:1]

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict live data
    if st.button("Run Predictive Analysis"): 
        predict_price(first_house_data, house_features, sale_price_pipeline)

    st.write("---")
    st.write("Here is the info for the key values of the clients inherited houses. ")
	
    in_df = load_inherited_house_data()
    filtered_df = in_df[["OverallQual", "GrLivArea", "TotalBsmtSF", "GarageArea", "YearBuilt", "YearRemodAdd"]]	
		
    st.write(filtered_df)

    st.write("After running them through the prediction app, their estimated prices are the following. \n\n "
			"* $126,449 \n"
			"* $150,322 \n"
			"* $170,148 \n"
			"* $181,897 ")
	
    st.write("---")


def DrawInputsWidgets():
    # Load the dataset
    df = load_house_data()
    percentage_min, percentage_max = 0.4, 2.0

    # Define features and their respective columns
    features = [
        ("OverallQual", 0, 10, 1),
        ("GrLivArea", int(df["GrLivArea"].min() * percentage_min), int(df["GrLivArea"].max() * percentage_max), 100),
        ("TotalBsmtSF", int(df["TotalBsmtSF"].min() * percentage_min), int(df["TotalBsmtSF"].max() * percentage_max), 50),
        ("GarageArea", int(df["GarageArea"].min() * percentage_min), int(df["GarageArea"].max() * percentage_max), 50),
        ("YearBuilt", int(df["YearBuilt"].min() * percentage_min), date.today().year, 1),
        ("YearRemodAdd", int(df["YearRemodAdd"].min() * percentage_min), date.today().year, 1)
    ]

    # Create input widgets for the most important features
    X_live = pd.DataFrame([], index=[0])
    columns = st.beta_columns(2)

    # Iterate over features and columns to create widgets
    for idx, (feature, min_val, max_val, step) in enumerate(features):
        col = columns[idx % len(columns)]
        with col:
            st_widget = st.number_input(
                label=feature,
                min_value=min_val,
                max_value=max_val,
                value=int(df[feature].median()),
                step=step
            )
            X_live[feature] = st_widget

    return X_live

