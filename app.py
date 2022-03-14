import streamlit as st
import time
import numpy as np
from PIL import Image
from cyberbullying.utils import get_trained_model

st.set_page_config(
            page_title="Cyberbullying Detection", # => Quick reference - Streamlit
            page_icon="🤬",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

ejemplo = """@freemedialive Fuck #Islam. Mohammed was a pedophile,
            murderer, bigot, sexist, rapist, slave trader, caravan robber, and liar"""


model = get_trained_model()

#if st.checkbox('Inject CSS', value=True):
#    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#'''## CYBERBULLYING DETECTION'''


col1, col2 = st.columns((3,1))

with col1:
    st.write("<h2>CYBERBULLYING DETECTION</h2>", unsafe_allow_html = True)

with col2:
    image = Image.open('wagon.png')
    st.image(image, caption='Le Wagon', use_column_width=False)


input = st.text_area("Enter text")
st.button('Submit text')

if input != '':
    response = model.predict_phrase(input)
    prediction = response['prediction']
    text = response['text']

    "Analyzing text"
    my_bar  = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete+1)

    with st.spinner(text='In progress'):
        time.sleep(1)
        if prediction == 1:
            st.error('Bullying detected')
            #st.warning('Bullying detected')
        else:
            st.success("No bullying detected")

    with st.container():
        st.write(f'<p class="result">{text}</p>', unsafe_allow_html = True)
