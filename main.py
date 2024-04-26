import streamlit as st
import requests

API_URL = 'API URL'
API_KEY = 'YOUR KEY' 

def initiate_login():
    try:
        response = requests.post(API_URL, headers={'Authorization': f'Bearer {API_KEY}'})
        if response.status_code == 200:
            st.success('Login initiated successfully')
        else:
            st.error(f'Error initiating login: {response.text}')
    except Exception as e:
        st.error(f'Error initiating login: {e}')
st.title('Radix Wallet Authentication')
if st.button('Initiate Login'):
    initiate_login()
