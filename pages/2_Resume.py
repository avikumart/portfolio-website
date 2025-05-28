import streamlit as st
import base64
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

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open("images/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
