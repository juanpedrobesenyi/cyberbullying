from math import radians
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
    choose = option_menu("CYBERBULLYING DETECTION", ["MAIN", "ABOUT"],
                         icons=['bi bi-arrow-right-square','bi bi-arrow-right-square'],
                         menu_icon="", default_index=0,
                         styles={
        "container": {"padding": "0.1rem", "background-color": "transparent"},
        "icon": {"color": "red", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(189, 215, 256, 0.541)"},
        "nav-link-selected": {"background-color": "rgba(175, 215, 260, 0.5)"},
    }
    )


###############################################################################################
### Main page ###
if choose == "MAIN":
    image_path = 'frontend/wagon.png'
    image_link = 'https://www.lewagon.com/'

    st.write(f'''<div class="title1">
             <h2>CYBERBULLYING DETECTION</h2>
             <a class="imagen" href="{image_link}">{image_tag(image_path)}</a>
             </div>
             ''', unsafe_allow_html=True)

    ## TEXT INPUT
    input = st.text_area('ENTER TEXT' )
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
        time.sleep(1)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete+1)

        ""
        ""

        with st.spinner(text='LOADING RESULTS'):
            time.sleep(0.5)
            if prediction == 1:
                st.error(f'BULLYING DETECTED: {bullying_tipe}')
                with st.container():
                    st.write(f'<p class="result">{text}</p>', unsafe_allow_html = True)
            else:
                st.success("NO BULLYING DETECTED")



###############################################################################################
### About page ###

if choose == "ABOUT":
    def link(link, text, **style):
        return a(_href=link, _target="_blank", style=styles(**style))(text)
    def image(src_as_string, **style):
        return img(src=src_as_string, style=styles(**style), )
    ## IMAGENES NUESTRAS

    pepo_link='https://media-exp1.licdn.com/dms/image/C4D03AQGzo6Moq_8oXg/profile-displayphoto-shrink_800_800/0/1647524004046?e=1652918400&v=beta&t=MukYXGMjlkpoqap4EB7bVtGkP0quF3trinWdduf0UzE'
    valen_link='https://media-exp1.licdn.com/dms/image/C4D03AQHxRb4L1NMw7w/profile-displayphoto-shrink_800_800/0/1600555429971?e=1652918400&v=beta&t=5JytF9cEE_QDCivFJrkszo20VhkvsPXJWn__zOXqQQo'
    pato_link='https://media-exp1.licdn.com/dms/image/C4E03AQHl9QCAeTJGDA/profile-displayphoto-shrink_800_800/0/1642175322042?e=1652918400&v=beta&t=XGNLZIszFA-p1bdQqGKNsIGTNA4oC7jj8YVgJJSWXGo'

    ## FUENTES
    st.markdown(""" <style> .font1 {
     font-size:25px ; font-family: 'Source Sans Pro'; color: white; width:95%; word-break: break-word}
     </style> """, unsafe_allow_html=True)

    st.markdown(""" <style> .font2 { font-family: 'Source Sans Pro'; color: white; width:95%; word-break: break-word}
     </style> """, unsafe_allow_html=True)

    ## EL EQUIPO
    st.write('''<center><div class="title1">
             <h2>-THE TEAM-</h2>
             </center>
             </div>
             ''', unsafe_allow_html=True)

    st.markdown(f"""<center><div class="row imagen-round">
                    <div class="column">{link("https://www.linkedin.com/in/juanpedrobesenyi/", image(pepo_link,width=px(100), height=px(100)))}</div>
                    <div class="column">{link("https://www.linkedin.com/in/patricio-copado/", image(pato_link,width=px(100), height=px(100)))}</div>
                    <div class="column">{link("https://www.linkedin.com/in/valengou/", image(valen_link,width=px(100), height=px(100)))}</div>
                    </div></center>
                    <center><strong><div class="row">
                    <div class="column">Juan Pedro Besenyi</div>
                    <div class="column">Patricio Copado</div>
                    <div class="column"> Valentin Gourdy</div>
                    </div></strong></center></br>
             <p class='font2'> We are a team of Data Scientist part of <strong>Batch 823</strong> on <strong>Le Wagon Data Science Bootcamp in Buenos Aires City. </strong> </p>""" , unsafe_allow_html=True)

    ## EL OBJETIVO

    st.markdown('<p class="font1"><strong>OBJECTIVE</strong></p>', unsafe_allow_html=True)

    st.markdown("""
             <p class='font2'>Motivated by the younger generations growing tendencies of spending a great amount of time
             on Social Media Platforms, we decided to tackle down one of the main problems present everywhere:</p>
             <center><div class="title1">
             <h2>CYBERBULLYING</h2>
             </div></center>
              <p class='font2'>Virtual harassment has become increasingly common, especially among teenagers, as the digital sphere has expanded, and technology has advanced.<br />
              Cyberbullying may be more harmful than traditional bullying, because there may be no escape.<br />
              Research illustrates that cyberbullying adversely affects youth to a higher degree than adolescents and adults: they are still growing mentally and physically.<br />
              Victims may have lower self-esteem, increased suicidal ideation, and a variety of emotional responses, including being scared, frustrated, angry, and depressed.</p><br />
             """ , unsafe_allow_html=True)
    ## EL MODELO

    st.markdown('<p class="font1"><strong>DEVELOPMENT</strong></p>', unsafe_allow_html=True)

    st.markdown("""<p class='font2'>
             We have developed a <strong>Natural Language Processing algorithm</strong> to detect bullying in different texts using two main Machine Learning Models,
            <strong>SVC (Support Vector Classiffier)</strong> to detect bully and <strong>ADABoost Classiffier</strong> to classiffy the type.<br /><br />
            The models have been trained with more than 250k short texts containing bullying and no bullying phrases.
            The bully phrases are also categorized in different types of categories which allows us to classiffy the type of bullying in the text in five different categories:</p>
            <ol class='font2'>
            <li><b>Religion</b>: Any discrimination act which intentionally or unintentionally degrade another person based on the bullied individuals religion.</li>
            <li><b>Gender</b>: Any kind of threatening or harassing behaviours that are based on gender role expectations.</li>
            <li><b>Ethnicity/Racial</b>: Any kind of discrimination or bullying against an individual on the basis of their skin color, or racial or ethnic origin.</li>
            <li><b>Age</b>: It occurs when a person is treated less favourably, or not given the same opportunities as others in a similar situation, because he or she is considered to be too old or too young.</li>
            <li><b>Aggression</b>: Is an action or response by an individual that delivers something unpleasant to another person.</li>
            </ol>""" , unsafe_allow_html=True)
