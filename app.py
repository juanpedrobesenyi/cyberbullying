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
    background-image: url(https://nordvpn.com/wp-content/uploads/2020/07/cyberbullying_1200x628.png);
    background-size: cover;
}
"""
st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: blue !important;
}
</style>
""",
    unsafe_allow_html=True,
)

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
def borrar(text):
    a = ""
    return a

input = st.text_input('Enter any text below:')
st.button('Lets check it out!', on_click=borrar)


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


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
prediccion1 = st.write(text, unsafe_allow_html = True)
