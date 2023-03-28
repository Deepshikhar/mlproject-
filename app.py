from flask import Flask,request,render_template
import numpy as np 
import pandas as pd 

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

import streamlit as st

st.title("Student Exam Performance Prediction")

def strip(txt):
    string_to_modify = txt
    modified_string = string_to_modify.replace("(", "").replace(")", "").replace(",", "")
    return modified_string.strip()

gender=st.radio("Gender",
    options=['male', 'female'])

race_ethnicity=st.radio("Ethnicity Group",
    options=['group A', 'group B','group C','group D','group E']),


parental_level_of_education=st.radio("Parental_level_of_education",
    options=["associate's degree","bachelor's degree","high school","master's degree","some college"]),


lunch=st.radio("Lunch",
    options=["free/reduced","standard"]),

test_preparation_course=st.radio("Test_preparation_course",
    options=["none","completed"]),

reading_score = st.number_input('Reading Score')
writing_score = st.number_input('Writing Score')
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)




data = CustomData(
            gender,
            race_ethnicity[0],
            parental_level_of_education[0],
            lunch[0],
            test_preparation_course[0],
            reading_score,
            writing_score
        )
pred_df=data.get_data_as_data_frame()
# print(pred_df)
# st.write(pred_df)
predict_pipeline=PredictPipeline()
results=predict_pipeline.predict(pred_df)

st.subheader(f"Predicted Maths Score : :green[{results[0]}]")
