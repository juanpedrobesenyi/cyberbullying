import streamlit as st
import time
import numpy as np
ejemplo = """@freemedialive Fuck #Islam. Mohammed was a pedophile,
            murderer, bigot, sexist, rapist, slave trader, caravan robber, and liar"""

CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url('https://thumbs.dreamstime.com/z/cyberbullying-concept-faceless-hooded-male-person-low-key-red-blue-lit-image-digital-glitch-effect-133406104.jpg');
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

CSS = """
orange {
   background-color: #ffa500;
   color: white;
}
yellow {
   background-color: #ffd700;
   color: black;
}
red {
   background-color: #8b0000;
   color: white;
}
.result {
    font-size: 30px;
}
"""

from cyberbullying.utils import get_trained_model
model = get_trained_model()

'''## CYBERBULLYING DETECTION
        '''
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


input = st.text_area("Enter multiline text")
#input = st.text_input('Enter any text below:')
st.button('Lets check it out!')

#<div width="704" data-testid="stVerticalBlock" class="css-1n76uvr e1tzin5v4"><div data-stale="false" width="704" class="element-container css-1hynsf2 e1tzin5v1"><div class="row-widget stTextInput css-pb6fr7 edfmue0" width="704"><label class="css-qrbaxs effi0qh0">Enter any text below:</label><div data-baseweb="input" class="st-ba st-b4 st-bb st-b7 st-bc st-bd st-be st-bf st-bg st-bh st-bi st-bj st-bk st-b2 st-bl st-av st-ay st-aw st-ax st-ae st-af st-ag st-ah st-ai st-aj st-bm st-bn st-bo st-bp st-bq st-br st-bs"><div data-baseweb="base-input" class="st-b4 st-b7 st-bt st-b2 st-bl st-ae st-af st-ag st-ah st-ai st-aj st-bu st-bq"><input aria-invalid="false" aria-required="false" autocomplete="" inputmode="text" name="" placeholder="" type="text" class="st-ba st-bv st-bw st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-b7 st-c5 st-c6 st-c7 st-c8 st-c9 st-ca st-cb st-ae st-af st-ag st-ah st-ai st-aj st-bu st-cc st-cd st-ce st-cf" value=""></div></div><div class="css-1s0xhnp effi0qh2"></div></div></div><div data-stale="false" width="704" class="element-container css-1hynsf2 e1tzin5v1"><div class="row-widget stButton" style="width: 704px;"><button kind="primary" class="css-1cpxqw2 edgvbvh1">Lets check it out!</button></div></div></div>
local_css("fondo.css")
response = model.predict_phrase(input)
#response = {'prediction':1,'text':'a'}
prediction = response['prediction']
text = response['text']

"Analyzing text"
my_bar  = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete+1)

"Detecting bullying"

with st.spinner(text='In progress'):
    time.sleep(1)
    if prediction == 1:
        st.warning('Bullying detected')
    else:
        st.success("No bullying detected")

# cualquier_cosa = f'<div style="background-color:white;">{input}{boton}</div>'
# st.markdown(cualquier_cosa, unsafe_allow_html=True)
with st.container():
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
    st.write(f'<p class="result">{text}</p>', unsafe_allow_html = True)
