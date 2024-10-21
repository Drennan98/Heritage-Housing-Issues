import streamlit as st
from app_pages.multipage import MultiPage

st.set_page_config(page_title="Heritage Housing Issues", layout="wide")

# Create instance
app = MultiPage(app_name="Heritage Housing Issues")

# load pages scripts
from app_pages.page1_summary import page1_summary
from app_pages.page2_feature_correlation import page2_feature_correlation
from app_pages.page3_ml_predict import page3_ml_predict
from app_pages.page4_hypotheses import page4_hypotheses
from app_pages.page5_predict import page5_predict 

app.app_page("Project Summary", page1_summary)
app.app_page("Feature Correlation", page2_feature_correlation)
app.app_page("Sale Price Predictor", page3_ml_predict)
app.app_page("Project Hypothesis and Validation", page4_hypotheses)
app.app_page("ML Sale Price Pipeline", page5_predict)

# Run the  app
app.run()
