import streamlit as st
import time
import numpy as np
from PIL import Image
from cyberbullying.utils import predict
from streamlit_option_menu import option_menu
import base64

###############################################################################################
#Page configuration
st.set_page_config(
            page_title="Cyberbullying Detection", # => Quick reference - Streamlit
            page_icon="🤬",
            layout="centered", # wide
            initial_sidebar_state="collapsed", ) # collapsed


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

ejemplo = """@freemedialive Fuck #Islam. Mohammed was a pedophile,
            murderer, bigot, sexist, rapist, slave trader, caravan robber, and liar"""

###############################################################################################
#Background image configuration
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

###############################################################################################
### SIDE BAR###
with st.sidebar:
    choose = option_menu("CYBERBULLYING DETECTION APP", ["Main", "About", "I am angry", "I am angry", "I am angry"],
                         icons=['bi bi-emoji-angry', 'bi bi-emoji-angry', 'bi bi-emoji-angry-fill', 'bi bi-emoji-angry-fill','bi bi-emoji-angry-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "0.2rem", "background-color": "rgba(195, 217, 260, 0.541)"},
        "icon": {"color": "grey", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(189, 215, 256, 0.541)"},
        "nav-link-selected": {"background-color": "rgba(175, 215, 260, 0.5)"},
    }
    )

###############################################################################################
### Main page ###
if choose == "Main":
    image_path = 'wagon.png'
    image_link = 'https://www.lewagon.com/'

    st.write(f'''<div class="title1">
             <h2>CYBERBULLYING DETECTION</h2>
             <a class="imagen" href="{image_link}">{image_tag(image_path)}</a>
             </div>
             ''', unsafe_allow_html=True)

    ## TEXT INPUT
    input = st.text_area('ENTER TEXT')
    st.button('Submit text')

    ## MODEL RESPONSE
    if input != '':
        response = predict(input)
        prediction = response['prediction']
        text = response['text']
        bullying_tipe = response['type']

        "ANALYZING TEXT"
        my_bar  = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete+1)

        with st.spinner(text='LOADING RESULTS'):
            time.sleep(0.5)
            if prediction == 1:
                st.error(f'BULLYING DETECTED: {bullying_tipe.upper()}')
                with st.container():
                    st.write(f'<p class="result">{text}</p>', unsafe_allow_html = True)
            else:
                st.success("NO BULLYING DETECTED")
    #image = Image.open('wagon.png')
    #st.image(image, caption='', use_column_width=False)


###############################################################################################
### About page ###

if choose == "About":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Source Sans Pro'; color: black;}
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Creators</p>', unsafe_allow_html=True)
    st.write("Pepo is a github genious")
