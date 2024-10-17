import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np

def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.write("### Model Evaluation")
    st.info("Train Set")
    evaluate_and_display(X_train, y_train, pipeline)
    
    st.info("Test Set")
    evaluate_and_display(X_test, y_test, pipeline)

def evaluate_and_display(X, y, pipeline):
    predictions = pipeline.predict(X)
    r2 = r2_score(y, predictions)
    mae = mean_absolute_error(y, predictions)
    st.write(f"R2 Score: {r2:.3f}")
    st.write(f"Mean Absolute Error: {mae:.3f}")
