import streamlit as st

st.markdown("""
    <style>
    .stTabs [role="tablist"] {
        display: flex;
        justify-content: space-evenly;
        width: 100%;
    }
    .stTabs [role="tab"] {
        flex: 1;
        text-align: center;
        padding: 12px;
        font-size: 18px;
        background-color: #2b2b2b; /* Background for tabs */
        border: 1px solid #555; /* Border color */
        color: #fff; /* Font color */
        border-radius: 4px;
    }
    .stTabs [role="tab"]:hover {
        background-color: #4c4c4c; /* Hover effect */
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b; /* Active tab color */
        color: #ffffff; /* Active tab text color */
    }
    .stTabs [role="tab"]:disabled {
        color: #9e9e9e; /* Disabled tab color */
        background-color: #3e3e3e; /* Background for disabled tab */
    }
    </style>
""", unsafe_allow_html=True)


@st.dialog("Contact Me")
def show_contact_form():
    with st.form("contact_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        st.form_submit_button("Send")


col1, col2 = st.columns([1, 2])

with col1:
    st.image("./asset/shariq.jpg", width=230)

with col2:
    st.title("Shariq Nauman")
    st.write("Aspiring Data Scientist, passionate about AI and Data Science. Currently enhancing my data analysis and programming skills, preparing to pursue a degree in Computer Science.")
    if st.button("✉️ Contact Me"):
        show_contact_form()

st.write("\n"); st.write("\n"); st.write("\n")
tab1, tab2, tab3 = st.tabs(["Experience", "Skills", "Education"])

with tab1:
    st.header("Experience")
    st.write("""
    - Currently learning Python and data analysis through online courses and certifications.
    - Completed 'Data Analysis with Python' certification from FreeCodeCamp.
    - Experience in exploratory data analysis (EDA) and visualization through personal projects, including the Google Playstore EDA project.
    - Strong problem-solving mindset and enthusiastic about data-driven decision-making.
    """)

with tab2:
    st.header("Skills")
    st.write("""
    - **Programming**: Python (Pandas, NumPy, Matplotlib, Scikit-learn), SQL
    - **Data Visualization**: Matplotlib, Seaborn, Plotly
    - **Modeling**: Linear regression, data preprocessing, exploratory data analysis (EDA)
    - **Tools**: Jupyter Notebook, Google Colab
    - **Databases**: SQLite (basic experience)
    """)

with tab3:
    st.header("Education")
    st.write("""
    - High School Senior
    - Certified in 'Data Analysis with Python' from FreeCodeCamp
    - Currently studying online courses in data science, machine learning, and AI.
    """)

