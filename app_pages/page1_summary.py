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

# The actual layout of this summary page was taken from the Churnometer walkthrough project. 

def page1_summary():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* The **sale price** refers to the numerical value (in US Dollars) that a house sells for.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset for this project is available on [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n\n"
        f"* I would like to confirm that the app was **successful** in predicting the sale price of the 4 inherited houses. Please run Predictive Analysis"
        f" on page 3 to see this."
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Drennan98/Heritage-Housing-Issues).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"#### The project has two business requirements:\n\n"
        f"**1.**  The client is interested in discovering how house attributes correlate with "
        f"the house Sale Price. Therefore, the client expects data visualizations "
        f"of the correlated variables against Sale Price to show that.\n\n"
        f"**2.** The client is interested to predict the house sales price from their 4 "
        f"inherited houses. "
        )

