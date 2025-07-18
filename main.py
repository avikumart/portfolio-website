import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
#from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from projects_dict import projects
from PIL import Image

st.set_page_config(page_title='Personal website' ,layout="wide",page_icon='👨🏻‍💻')

# -----------------  chatbot  ----------------- #
pronoun = info["Pronoun"]
name = info["Name"]

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(f"""<a href="{info['LinkedIn']}" target="_blank">🔗 Linkedin: {info['Full_Name']}</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['GitHub']}" target="_blank">🔗 GitHub Profile</a>""", unsafe_allow_html=True)
# kaggle and X acount links
st.sidebar.markdown(f"""<a href="{info['Kaggle']}" target="_blank">🔗 Kaggle Profile</a>""", unsafe_allow_html=True)
st.sidebar.markdown(f"""<a href="{info['X']}" target="_blank">🔗 X Profile</a>""", unsafe_allow_html=True)

image = Image.open("images/-mckof1.jpg")
with st.sidebar:
    st.image(image, width=200)
    st.markdown(f"<h1 style='text-align: center; color: #000395;'>{info['Full_Name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #e0fbfc;'>{info['Intro']}</h2>", unsafe_allow_html=True)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")

# ----------------- current interests ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader("🔍 Current Interests")
    
    inerests = ["- Machine Learning Systems",
                "- Large Language Models (LLMs)",
                "- Data Engineering",
                "- MLOps"]
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🌟 Key Areas of Focus**")
        for interest in inerests[:2]:
            st.markdown(interest)
    with col2:
        st.markdown("**🌟 Key Areas of Focus**")
        for interest in inerests[2:]:
            st.markdown(interest)

# ----------------- currently learning ------------- #
with st.container():
    col1, _ = st.columns([0.95, 0.05])
    with col1:
        with st.expander("📚 Currently Learning"):
            st.markdown("Designing Machine Learning Systems by Huyen")
            st.markdown("Pytorch ML development")
            st.markdown("LLM applications")


# ----------------- skillset ----------------- #
with st.container():
    st.subheader("⚒️ Technical Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**👨‍💻 Programming Languages**")
        st.markdown("- Python 🐍")
        st.markdown("- SQL 🗃️")

        st.markdown("**📚 ML/DL Frameworks**")
        st.markdown("- Scikit-learn")
        st.markdown("- TensorFlow")
        st.markdown("- Keras")
        st.markdown("- PyTorch")
        st.markdown("- Hugging Face Transformers")
        st.markdown("- LangChain")
        st.markdown("- LlamaIndex")
        st.markdown("- statsmodels")

    with col2:
        st.markdown("**🛠️ Tools & Platforms**")
        st.markdown("- Jupyter Notebook / PyCharm")
        st.markdown("- Git & GitHub")
        st.markdown("- Power BI / Excel / Tableau")
        st.markdown("- VScode")
        st.markdown("- MLflow")

        st.markdown("**☁️ Cloud & Deployment**")
        st.markdown("- AWS (S3, Lambda, EC2, ECR)")
        st.markdown("- Streamlit / Flask")
        st.markdown("- Prefect orchestrator")
        st.markdown("- Docker")
        st.markdown("- GitHub Actions")

        
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)

# ----------------- github feed ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('💻 GitHub Activity')
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        st.markdown("**Latest GitHub Activity**")
        st.markdown("This section displays my latest GitHub activity, including commits, pull requests, and issues.")
        github_user = "avikumart"  # Replace with your GitHub username
        github_rss = f"https://github.com/{github_user}.atom"

        github_embed_html = f"""
        <iframe src="https://rss.bloople.net/?url={github_rss}" width="100%" height="400"></iframe>
        """
        components.html(github_embed_html, height=400, scrolling=True)

# -----------------  projects  ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader("🚀 Projects")
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        st.markdown("This section showcases some of my projects, including their descriptions and links to the repositories.")
        for project in projects:
            with st.expander(project["title"], expanded=True):
                st.markdown(f"**Description:** {project['description']}")
                st.markdown(f"**Tools Used:** {', '.join(project['tools'])}")
                st.markdown(f"[🔗 View Project]({project['link']})")  



# ----------------- medium ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ Medium')
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Display my latest posts'):
            components.html(embed_rss['rss'],height=400)

        st.markdown(f"""<a href="{info['Medium']}" target="_blank">🔗 Access the link</a>""", unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👨🏼‍💼 Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
