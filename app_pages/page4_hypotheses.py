import streamlit as st

def page4_hypotheses():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"**Hypothesis 1** - Houses with 4 bedrooms appear to reach the highest prices, with one exceeding $700,000\n\n"
        f"In my Sale Price Study notebook, I hypothesised that houses with 4 bedrooms appears to reach the highest prices,"
        f"we can see the scatterplot shows this as we have two blue dots above the $700,000 mark. So this hypothesis is **correct**.\n\n"
        f"**Hypothesis 2** - Homes with smaller unfinished basements tend to have a wider range of sale prices. Sale prices"
        f"are influenced by several factors and unfinished areas would be a major issue. "
        f"We can see in the Sale Price Study notebook that there is a cluster of properties between 0-1000 square feet range,\n"
        f"and we can see that the properties are evenly distributed here across a range of price ranges and square footage. "
        f"There is also a couple of outliers in $700,000 price range also which may suggest that other factors have come into play here. "
        f"The correlation is not as strong here as a house so you can argue that this hypothesis is **correct** and/or **incorrect**.\n\n"
        f"**Hypothesis 3** - Houses with larger amount of square footage on the first floor generally cost more than houses with smaller"
        f"amounts of square footage. The scatterplot shows us in the Sale Price Study notebook shows that this hypothesis is **correct**. "
        f"When the 1st floor square foot value increases we can see that the price also increases."
    )

    st.write (
        f"**Definition of outlier:** This is a data point that is significantly different from other observations."
    )