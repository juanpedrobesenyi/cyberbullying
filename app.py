import streamlit as st
import time
import numpy as np
from PIL import Image
from cyberbullying.utils import predict
from streamlit_option_menu import option_menu
import base64
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb




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

local_css("frontend/style.css")

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
image_path = 'frontend/fondo-mediano.jpg'
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
    image_path = 'frontend/wagon.png'
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

        ""
        ""
        #"ANALYZING TEXT"
        my_bar  = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete+1)

        ""
        ""

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



############################################################################################
###foooter



def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="grey",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by ",
        br(),
        link("https://github.com/juanpedrobesenyi", "@Pepo"),
        link("https://www.linkedin.com/in/juanpedrobesenyi/",
             image('https://media-exp1.licdn.com/dms/image/D4E35AQGgPS7tFgNBfg/profile-framedphoto-shrink_800_800/0/1637119377864?e=1647468000&v=beta&t=qqVtRGdFllXM8FSg2eJKKkVypwoUuyBmO87Oh6NUoKM',width=px(25), height=px(25))),
        ' -- ',link("https://github.com/pjcopado", "@Patricio Copado"),
        link("https://www.linkedin.com/in/patricio-copado/",
             image('https://media-exp1.licdn.com/dms/image/C4E03AQHl9QCAeTJGDA/profile-displayphoto-shrink_800_800/0/1642175322042?e=1652918400&v=beta&t=XGNLZIszFA-p1bdQqGKNsIGTNA4oC7jj8YVgJJSWXGo',width=px(25), height=px(25))),
        ' -- ',link("https://github.com/Valengou", "@Valengou"),
        link("https://www.linkedin.com/in/valengou/",
             image('https://media-exp1.licdn.com/dms/image/C4D03AQHxRb4L1NMw7w/profile-displayphoto-shrink_800_800/0/1600555429971?e=1652918400&v=beta&t=5JytF9cEE_QDCivFJrkszo20VhkvsPXJWn__zOXqQQo',width=px(25), height=px(25))),

    ]
    layout(*myargs)

footer()


###############################################################################################
### About page ###

if choose == "About":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Source Sans Pro'; color: black;}
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Creators</p>', unsafe_allow_html=True)
    st.write("Pepo is a github genious")
