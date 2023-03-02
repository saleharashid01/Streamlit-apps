import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from streamlit_pandas_profiling import st_profile_report 
from pandas_profiling import ProfileReport

# Webb app Title

st.markdown(''' 
# **Exploratory Data Analysis Web Application**
This app is developed by **Saleha Rashid, Environmental Engineer**, Known as **EDA APP**''')
# How to upload a file from pc

with st.sidebar.header('Upload Your Dataset (.CSV, .xlsx, pdf)'):
    uploaded_file=st.sidebar.file_uploader('Upload your File', type=['csv', 'xlsx','pdf'])
    df = sns.load_dataset('titanic')
    
# with st.sidebar.header('Upload Your Dataset (.xlsx)'):
#     uploaded_file=st.sidebar.file_uploader('Upload your File', type=['xlsx'])
#     df = sns.load_dataset('titanic')

if uploaded_file is not None:
    
    def load_csv():
        csv =pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st. header('**Input Dataframe**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report wih Pandas**')
    st_profile_report(pr)

else:
    st.info('Awaiting for CSV File, Upload')
    if st.button('Press to use example'):
    # example dataset

     @st.cache
     def load_data():
        a= pd.DataFrame(np.random.rand(100,5), columns=['age', 'ball', 'cat', 'dog','ear'])
        return a
    df =load_data()
    pr = ProfileReport(df, explorative=True)
    st. header('**Input Dataframe**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report wih Pandas**')
    st_profile_report(pr)