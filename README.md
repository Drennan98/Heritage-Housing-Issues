# Heritage Housing Issues 


This is my final project for the Full Stack Software Development diploma. In this project, I've developed a data application which is presented on Streamlit. While I'm happy to reach this part of the course, this project was extremely challenging but was very rewarding to see what I could do when it came to analysis and manipulaton of a dataset. 

![Summary](media/summary.png)


# Dataset content

- The dataset is sourced from Kaggle. We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.

- The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

| Variable      | Meaning                                                                | Units                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1stFlrSF      | First Floor square feet                                                | 334 - 4692                                                                                                                                       |
| 2ndFlrSF      | Second-floor square feet                                               | 0 - 2065                                                                                                                                         |
| BedroomAbvGr  | Bedrooms above grade (does NOT include basement bedrooms)              | 0 - 8                                                                                                                                            |
| BsmtExposure  | Refers to walkout or garden level walls                                | Gd: Good; Av: Average; Mn: Minimum; No: No Exposure; None: No Basement                                                                           |
| BsmtFinType1  | Rating of basement finished area                                       | GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average; Rec: Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement |
| BsmtFinSF1    | Type 1 finished square feet                                            | 0 - 5644                                                                                                                                         |
| BsmntUnfSF    | Unfinished square feet of basement area                                | 0 - 2336                                                                                                                                         |
| TotalBsmntSF  | Total square feet of basement area                                     | 0 - 6110                                                                                                                                         |
| GarageArea    | Size of garage in square feet                                          | 0 - 1418                                                                                                                                         |
| GarageFinish  | Interior finish of the garage                                          | Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage                                                                             |
| GarageYrBlt   | Year garage was built                                                  | 1900 - 2010                                                                                                                                      |
| GrLivArea     | Above grade (ground) living area square feet                           | 334 - 5642                                                                                                                                       |
| KitchenQual   | Kitchen quality                                                        | Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor                                                                                 |
| LotArea       | Lot size in square feet                                                | 1300 - 215245                                                                                                                                    |
| LotFrontage   | Linear feet of street connected to property                            | 21 - 313                                                                                                                                         |
| MasVnrArea    | Masonry veneer area in square feet                                     | 0 - 1600                                                                                                                                         |
| EnclosedPorch | Enclosed porch area in square feet                                     | 0 - 286                                                                                                                                          |
| OpenPorchSF   | Open porch area in square feet                                         | 0 - 547                                                                                                                                          |
| OverallCond   | Rates the overall condition of the house                               | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor          |
| OverallQual   | Rates the overall material and finish of the house                     | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor          |
| WoodDeckSF    | Wood deck area in square feet                                          | 0 - 736                                                                                                                                          |
| YearBuilt     | Original construction date                                             | 1872 - 2010                                                                                                                                      |
| YearRemodAdd  | Remodel date (same as construction date if no remodeling or additions) | 1950 - 2010                                                                                                                                      |
| SalePrice     | Sale Price                                                             | 34900 - 755000                                                                                                                                   |

# Business requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.



# Hypothesis and how to validate


In Machine Learning, a hypothesis refers to a model or function that you assume can predict the output from the given input data. It represents your best guess about how the input features relate to the target variable. 

 - Hypothesis 1 - Houses with 4 bedrooms appear to reach the highest prices, with one exceeding $700,000. 

 - Hypothesis 2 - Homes with smaller unfinished basements tend to have a wider range of sale prices. Sale prices are influenced by several factors and unfinished areas would be a major issue. 

 - Hypothesis 3 - Houses with larger amounts of square footage on the first floor generally cost more than houses with smaller amounts of square footage. 



# Rationale to map the business requirements to the data visualizations and Machine Learning tasks


# Machine Learning business case


# Dashboard design


# Unfixed bugs 


# Deployment

## The deployment process is done through Heroku. This site is used for this project as it is better for hosting backend files. Please follow the below steps to deploy this project:


- Create a Heroku accout if you haven't done so already. 

- Create a new app, give it a unique name and select your region from the options provided.

- Connect to GitHub (you might be asked to confirm login through the mobile app if you have it downloaded).

- Select the appropriate branch from which you want to deploy the project from. 

- Deploy the project. Keep an eye on the build log if the deployment fails, this will suggest any changes that need to be made in order to deploy successfully.

# Main data analysis and Machine Learning libraries


# Credits 

- My mentor Mo Shami, for his patience and guidance through the development of this project. 

- My brother Sean, for his help and input. 