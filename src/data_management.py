import streamlit as st
import pandas as pd
import numpy as np
import joblib

# This code was taken from the Churnometer project by Code Institute. 

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_data():
    df = pd.read_csv("outputs/datasets/datacollection/HousePrices.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_house_data():
    df_h = pd.read_csv("outputs/datasets/datacollection/HousePrices.csv")
    return df_h

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)