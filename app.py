import streamlit as st
import time
import numpy as np

azul="#8ef"
rojo="#faa"
amarillo="#fea"
verde="#afa"
text_example = "(a,'',red), (b,'',yellow), (c,'',green), d, e, f"
#text_example = "I wasn't talking to you jerkso, your such an idiot"


CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://thumbs.dreamstime.com/z/cyberbullying-concept-faceless-hooded-male-person-low-key-red-blue-lit-image-digital-glitch-effect-133406104.jpg);
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
"""

from cyberbullying.utils import get_trained_model
model = get_trained_model()

'''
## CYBERBULLYING DETECTION
'''
col = st.columns(1)
with col:
    input = st.text_input('Enter any text below:')
    st.button('Lets check it out!')


response = model.predict_phrase(input)
#response = {'prediction':1,'text':'a'}
prediction = response['prediction']
text = response['text']

"Analyzing text"
my_bar = st.progress(0)
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
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
st.write(text, unsafe_allow_html = True)
