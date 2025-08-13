import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title='Loan_predictor')
st.header('Welcome to Loan predictor')
st.subheader('Enter the details')
df = pd.read_csv('cleaned_str.csv')
genders = list(df['person_gender'].unique())
educationl =list(df['person_education'].unique())
home_ownerships = list(df['person_home_ownership'].unique())
loan_intents = list(df['loan_intent'])
previous_loan_defaults_on_files = list(df['previous_loan_defaults_on_file'])

with open('rfmodel.pkl','rb')as file:
    rfmodel = pickle.load(file)

with st.container(border=True):
    col1,col2,col3 = st.columns([1,1,1])
    age = col1.number_input('Person_age:', min_value=18,max_value=90)
    gender = col2.selectbox('Person_gender',options=genders)
    education = col3.selectbox('Person_education', options=educationl)
    income = col1.number_input('Person_income',min_value=1000)
    experience = col2.number_input('Person_experience', min_value=0)
    home_ownership = col3.selectbox('Person_home_ownership',options = home_ownerships)
    loan_amount = col1.number_input('Loan_amount',min_value = 500)
    loan_intent =col2.selectbox('Loan_intent', options = loan_intents)
    loan_int_rat_income = col3.number_input('Loan_percent_income')
    loan_percent_income = col1.number_input('loan_percent_income')

    cb_person_cred_hist_length = col1.number_input('cb_person_cred_hist_length')
    credit_score = col2.number_input('credit_score', )
    previous_loan_defaults_on_file = col3.selectbox('previous_loan_defaults_on_file',options = previous_loan_defaults_on_files)

    genders.sort()
    educationl.sort()
    home_ownerships.sort()

    input_values = [(age,genders.index(gender),educationl.index(education),income,experience,
                     home_ownerships.index(home_ownership),
                     loan_amount,loan_intents.index(loan_intent),loan_int_rat_income,loan_percent_income,
                     cb_person_cred_hist_length,credit_score,previous_loan_defaults_on_files.index(previous_loan_defaults_on_file))]
    
    if st.button('Predict'):
         out=rfmodel.predict(input_values)
         if out[0]==1:
            st.subheader('Loan can be sanctioned')
         else:
             st.subheader('Loan can not be sanctioned')







