#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 09:56:26 2023

@author: armsy326
"""
##
##This is malaria.ipynb file converted to .py for ease of use
##
##

import numpy as np
from sklearn.linear_model import LinearRegression
from math import floor

commodities_data = [4898535.0, 4896284.0, 4162071.5, 5930233.0, 6156400.0]
years = [2018, 2019, 2020, 2021, 2022]

def predict_for_years(n):
    print(n)
    try:
        # Reshape the years data to fit the required input format for the LinearRegression model
        X = np.array(years).reshape(-1, 1)

        # Fit the linear regression model to the data
        model = LinearRegression().fit(X, commodities_data)

        # Predict the trend in the commodity data for the next 3 years
        
        future_years = np.array([2023, 2024, 2025]).reshape(-1, 1)
        predictions = model.predict(future_years)

        predicted = []
        # Print the predicted trend in the commodity data
        for i in range(int(n)):
            predicted.append(f"Predicted commodity value for {future_years[i][0]}: {predictions[i]}")
        return predicted

    except Exception:

        return "I can not predict for more than 3 years, I'm currently using linear regression model.A lot of inaccuracies will be countered"


predict_for_years(2)