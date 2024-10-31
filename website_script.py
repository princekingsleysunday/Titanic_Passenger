import streamlit as st
import joblib

# Load your model
model = joblib.load('Titanicprediction.model')

# Set page configuration
st.set_page_config(
    page_title='Titanic Survival Prediction',
    page_icon='🚢',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS to enhance page appearance
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        text-align: center;
        color: #2c3e50;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #2c3e50;
        text-align: center;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Add a background image or color
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1579674020484-cca5c79c7ad2");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the app
st.title('🚢 Titanic Survival Prediction', anchor='center')
st.write('---')  # Add a divider for a cleaner look

# Add an image at the top
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/RMS_Titanic_3.jpg", caption='RMS Titanic', use_column_width=True)

# Arrange the input fields in columns
st.subheader('Enter Passenger Information:')
col1, col2 = st.columns(2)

# Collect user inputs
Pclass = col1.selectbox("Passenger Class (1, 2, or 3)", options=[1, 2, 3])
Sex = col2.selectbox("Gender", options=['Male', 'Female'])
Age = col1.number_input("Age", min_value=0, max_value=80, step=1)
SibSp = col2.number_input("Number of Siblings/Spouses", min_value=0, max_value=10, step=1)
ParentChildren = col1.number_input("Number of Parents/Children", min_value=0, max_value=10, step=1)

# Convert categorical input (Sex) to numeric
Sex = 1 if Sex == 'Male' else 0

# Create a button for prediction
st.write('---')  # Add a divider before the button
if st.button('Make Your Prediction'):
    # Prepare the input data for the model
    input_data = [[Pclass, Sex, Age, SibSp, ParentChildren]]
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Display the result with different color messages
    if prediction == 1:
        st.success('🚢 The Passenger Survived!')
    else:
        st.error('💀 The Passenger Did Not Survive.')

# Add extra information in the sidebar
st.sidebar.header('About this App')
st.sidebar.info(
    """
    This app predicts whether a passenger would have survived the Titanic disaster.
    The prediction is based on several factors like passenger class, gender, age, 
    and number of relatives on board.
    """
)

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Titanic Prediction App - Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
