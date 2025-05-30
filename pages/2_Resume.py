import streamlit as st
import base64
from PIL import Image
from constant import *
import streamlit.components.v1 as components
from pdfreader import SimplePDFViewer, PageDoesNotExist



st.set_page_config(page_title='Resume', layout="wide", page_icon='📄')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(f"""<a href="{info['LinkedIn']}" target="_blank">🔗 Linkedin: {info['Full_Name']}</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['GitHub']}" target="_blank">🔗 GitHub Profile</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['Kaggle']}" target="_blank">🔗 Kaggle Profile</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['X']}" target="_blank">🔗 X Profile</a>""", unsafe_allow_html=True)


image = Image.open("images/-mckof1.jpg")
st.sidebar.image(image, caption="Avikumar Talaviya", width=150)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://drive.google.com/file/d/1Bl8vvTCM8K-P7OKkM0zvLiXt8ydOSndB/view?usp=sharing)")

pdf_url = f"https://mypfp.s3.ap-south-1.amazonaws.com/Resume+-+Avi+Kumar+Talaviya.pdf"

with pdf_url as pdf_file:
    pdf_data = pdf_file.read()
    b64_pdf = base64.b64encode(pdf_data).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="600px"></iframe>'
    components.html(pdf_display, height=600, scrolling=True)