import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(f"""<a href="{info['LinkedIn']}" target="_blank">🔗 {info['Name']}</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['GitHub']}" target="_blank">🔗 GitHub</a>""", unsafe_allow_html=True)

image = Image.open("images/-mckof1.jpg")
st.sidebar.image(image, caption="Avikumar Talaviya", width=150)

img_1 = Image.open("images/1.jpg")
img_2 = Image.open("images/2.png")
img_3 = Image.open("images/3.png")

st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
   st.image(img_1)
   
with col2:
   st.image(img_2)

with col3:
   st.image(img_3)

