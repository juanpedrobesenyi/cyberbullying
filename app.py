import streamlit as st
import time
import numpy as np
from PIL import Image
from cyberbullying.utils import get_trained_model
from streamlit_option_menu import option_menu




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

import base64

@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded
@st.cache
def image_tag(path):
    encoded = load_image(path)
    tag = f'<img src="data:image/png;base64,{encoded}">'
    return tag
@st.cache
def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    return style
image_path = 'fondo-mediano.jpg'
st.write(background_image_style(image_path), unsafe_allow_html=True)



with st.sidebar:
    st.markdown(
     """
     <style>
       [data-testid="stSidebar"][aria-expanded="false"]
        </style>
        """,
        unsafe_allow_html=True)
    choose = option_menu("CYBERBULLYING DETECTION APP", ["Main", "About", "I am angry", "I am angry", "I am angry"],
                         icons=['bi bi-emoji-angry', 'bi bi-emoji-angry', 'bi bi-emoji-angry-fill', 'bi bi-emoji-angry-fill','bi bi-emoji-angry-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "rgba(242, 243, 244, 0.541)"},
        "icon": {"color": "red", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(166, 172, 175, 0.541)"},
        "nav-link-selected": {"background-color": "rgba(202, 207, 210, 0.9)"},
    }
    )


#if st.checkbox('Inject CSS', value=True):
#    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#'''## CYBERBULLYING DETECTION'''

if choose == "Main":
    col1, col2 = st.columns((4,1))

    with col1:
        st.markdown('<h2 class="titulo">CYBERBULLYING DETECTION</h2>' , unsafe_allow_html = True)
        #'''## CYBERBULLYING DETECTION'''
    with col2:
        image = Image.open('wagon.png')
        st.image(image, caption='', use_column_width=False,)

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
            time.sleep(0.5)
            if prediction == 1:
                st.error('Bullying detected')
                #st.warning('Bullying detected')
                with st.container():
                    st.write(f'<p class="result">{text}</p>', unsafe_allow_html = True)
            else:
                st.success("No bullying detected")



if choose == "About":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Creators</p>', unsafe_allow_html=True)
    st.write("Pepo is a github genious")
