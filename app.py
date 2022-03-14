import streamlit as st
import time
from annotated_text import annotated_text
import requests
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
    background-image: url("https://aaci.org/wp-content/uploads/2020/10/27-Preventing-cyberbullying-while-learning-online-image.png");
    background-size: cover;
}
"""


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

#st.image("stop-cyberbullying.jpg",width=700)
'''
## CYBERBULLYING DETECTION
'''

input = st.text_input('Enter any text below:')
st.button('Lets check it out!')

"Analyzing text"
#my_bar = st.progress(0)
#for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete+1)

"Detecting bullying"

with st.spinner(text='In progress'):
    time.sleep(3)
    if input == text_example:
        st.warning('Bullying detected')
    else:
        st.success("No bullying detected")

# def coloreo(df):
#     resultado = []
#     words = df[df.columns[0]]
#     colors = df[df.columns[1]]
#     for i,color in enumerate(colors):
#         if color != "white":
#             resultado.append(f"({words[i]},'',{color})")
#         else:
#             resultado.append(f"{words[i]}")
#     return resultado

#prueba = ["(a,'',red)", "(b,'',yellow)", "(c,'',green)", 'd', 'e', 'f']
prueba = ('a', '', 'red'), ('b', '', 'yellow'), ('c', '', 'green'), 'd', 'e', 'f'

# if input == text_example:
#    annotated_text("I wasn't talking to you",("jerkso","",rojo)," your such an",("idiot","",rojo))

if input == text_example:
    annotated_text(prueba)

# if input == text_example:
#     annotated_text(("a",'',"red"),("b",'',"yellow"),("c",'',"green")," d, e, f")



# """I wasn't talking to you jerkso,
#       your such an idiot you cant even realize when someone
#       is talking to you. Now go back to your trailer boy!
# """," I wasn't talking to you",("jerkso","",rojo)," your such an",("idiot","",rojo)

#     annotated_text(
#     input,
#     lista_con_joins
# )
#"(a,'',red), (b,'',yellow), (c,'',green), d, e, f"

#url = 'https://taxifare.lewagon.ai/predict'

#params = {'text_input': input}

# response = requests.get(url,params)
# json_resp = response.json()

# prediction = np.round_(json_resp['fare'],2)
