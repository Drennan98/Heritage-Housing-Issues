import streamlit as st

# Function for page navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Project Summary", "Feature Correlation", 
                                          "Predicted Sale Price", "Hypotheses", 
                                          "Model Performance"])

    if page == "Project Summary":
        project_summary()
    elif page == "Feature Correlation":
        feature_correlation()
    elif page == "Predicted Sale Price":
        predicted_sale_price()
    elif page == "Hypotheses":
        hypotheses()
    elif page == "Model Performance":
        model_performance()

def page1_summary():
    pass
