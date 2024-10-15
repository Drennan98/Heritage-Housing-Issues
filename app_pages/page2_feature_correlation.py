import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
import numpy as np
import plotly.express as px

from src.data_management import load_house_data
from feature_engine.discretisation import ArbitraryDiscretiser

sns.set_style("whitegrid")

def page2_feature_correlation():
    """
    Display correlated features and visualize house prices per variable.
    """
    df = load_house_data()
    vars_to_study = [
        '1stFlrSF', 'GarageArea', 'GrLivArea', 'KitchenQual',
        'MasVnrArea', 'OpenPorchSF', 'OverallQual',
        'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd'
    ]

    st.write("### Housing Prices Correlation Study (BR1)")
    st.info(
        "* **BR1** - The client is interested in discovering how house attributes correlate with sale prices. "
        "Therefore, the client expects data visualizations of the correlated variables against the sale price."
    )

    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns."
            " Below are the first 10 rows.\n"
            "* SalePrice is our target variable, and we want to identify features correlated to it."
        )
        st.write(df.head(10))

    st.write("---")
    st.write(
        f"* We conducted a correlation study to understand how "
        "variables correlate with the sale price of a property, addressing BR1. \n"
        f"* The most correlated variables are: **{vars_to_study}**"
    )
    
    st.info(
        "Key observations from the analysis:\n"
        "* Higher values of 1stFlrSF, GarageArea, GrLivArea, MasVnrArea, and TotalBsmtSF are associated with higher sale prices.\n"
        "* Recently built houses (YearBuilt) and remodeled ones (YearRemodAdd) tend to have higher prices.\n"
        "* Quality indicators like KitchenQual and OverallQual show a positive correlation with sale price.\n"
        "* However, at higher values, the relationship between some variables and sale price becomes less clear."
    )

    df_eda = df[vars_to_study + ['SalePrice']]
    if st.checkbox("Distribution of SalePrice"):
        plot_histogram(df_eda, 'SalePrice')

    if st.checkbox("House Prices per Variable"):
        plot_house_price_per_variable(df_eda, vars_to_study)

    if st.checkbox("Correlation Heatmaps: Pearson, Spearman, and PPS"):
        display_correlation_heatmaps(df)


def plot_histogram(df, target_var):
    """
    Plot a histogram of the target variable.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df[target_var], kde=True, ax=ax)
    plt.title(f"Distribution of {target_var}", fontsize=20)
    st.pyplot(fig)


def plot_house_price_per_variable(df, vars_to_study):
    """
    Generate box, line, or scatter plots for each variable against SalePrice.
    """
    target_var = 'SalePrice'
    time_features = ['YearBuilt', 'YearRemodAdd']

    for col in vars_to_study:
        if len(df[col].unique()) <= 10:
            plot_box(df, col, target_var)
        elif col in time_features:
            plot_line(df, col, target_var)
        else:
            plot_scatter(df, col, target_var)


def plot_box(df, col, target_var):
    """
    Generate a box plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x=col, y=target_var, ax=ax)
    plt.title(f"Box plot of {target_var} vs {col}", fontsize=20)
    st.pyplot(fig)


def plot_line(df, col, target_var):
    """
    Generate a line plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x=col, y=target_var, ax=ax)
    plt.title(f"Line plot of {target_var} vs {col}", fontsize=20)
    st.pyplot(fig)


def plot_scatter(df, col, target_var):
    """
    Generate a scatter plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.regplot(data=df, x=col, y=target_var, ci=None, ax=ax)
    plt.title(f"Scatter plot of {target_var} vs {col}", fontsize=20)
    st.pyplot(fig)


def display_correlation_heatmaps(df):
    """
    Display Pearson, Spearman, and PPS correlation heatmaps.
    """
    df_corr_pearson, df_corr_spearman, pps_matrix = calculate_correlations(df)
    plot_heatmap(df_corr_pearson, "Pearson Correlation", 0.4)
    plot_heatmap(df_corr_spearman, "Spearman Correlation", 0.4)
    plot_heatmap(pps_matrix, "PPS Correlation", 0.2, cmap='rocket_r')


def calculate_correlations(df):
    """
    Calculate Pearson, Spearman correlations, and PPS.
    """
    df_corr_pearson = df.corr(method='pearson')
    df_corr_spearman = df.corr(method='spearman')
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.pivot(index='y', columns='x', values='ppscore')

    return df_corr_pearson, df_corr_spearman, pps_matrix


def plot_heatmap(corr_matrix, title, threshold=0.2, cmap='viridis'):
    """
    Plot a heatmap of a correlation matrix with a threshold.
    """
    mask = np.abs(corr_matrix) < threshold
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, mask=mask, annot=True, cmap=cmap, linewidths=0.5, ax=ax)
    plt.title(title, fontsize=18)
    st.pyplot(fig)
