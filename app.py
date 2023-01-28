# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:27:24 2023

@author: USER
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
house_price_model = pickle.load(open("C:/Users/USER/Desktop/ML/models/house_model.pkl", "rb"))

 #Get input from the user
 
 Surface_covered_in_m2 = st.text_input("Surface_covered_in_m2")
 lat = st.text_input("Latitude")
 lon = st.text_input("Longitude")
 borough = st.text_input("Borough")
 
 #code for prediction
 House_price = ""
 #Creating button for prediction
 if st.button("Predict House Price"):
     House_price = make_prediction(Surface_covered_in_m2, lat, lon, borough)
     
 st.success(House_price)

