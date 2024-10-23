import streamlit as st

def predict_price(X_live, house_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(house_features)

	# predict
	sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)

	# create a logic to display the results
	proba = sale_price_prediction_proba
	value = float(proba.round(1))
	amount = '${:,.2f}'.format(value)
	statement = (
		f'### With the values given, we estimate this house to be worth {amount} '
	)

	st.write(statement)
		
	st.write(proba)

def predict_inherited_house_price(X_inherited, house_features, price_pipeline):

	# From inherited houses data, subset features related to this pipeline
		X_inherited_price = X_inherited.filter(house_features)

		# predict

		price_prediction_inherited = price_pipeline.predict(X_inherited_price)
		# st.write(tenure_prediction_proba)
		
		this_price = price_prediction_inherited[0]
		# create a logic to display the results
		
		return this_price