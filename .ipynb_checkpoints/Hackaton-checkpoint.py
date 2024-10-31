import streamlit as st
import joblib

# load your model
model = joblib.load('Titanicprediction.model')

# set your title
st.title('Welcome to Titanic Survival Prediction')

# arrange how your column should look
col1 , col2 = st.columns(2)

# Collect user inputs
Pclass = col1.number_input("Enter Passenger Class (1, 2, or 3)", min_value=1, max_value=3, step=1)
Sex = col2.selectbox("Select Gender", options=['Male', 'Female'])
Age = col1.number_input("Enter the Passenger's Age", min_value=0, max_value=80, step=1)
SibSp = col2.number_input("Enter Number of Siblings/Spouses", min_value=0, max_value=10, step=1)
ParentChildren = col1.number_input("Enter Number of Parents/Children", min_value=0, max_value=10, step=1)

# Convert categorical input (Sex) to numeric
Sex = 1 if Sex == 'Male' else 0

# Create the prediction button
if st.button('Make your prediction'):
    # Prepare the input data for the model
    input_data = [[Pclass, Sex, Age, SibSp, ParentChildren]]
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction == 1:
        st.success('The Passenger Survived')
    else:
        st.warning('The Passenger Died')
