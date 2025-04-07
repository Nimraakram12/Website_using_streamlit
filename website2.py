import streamlit as st

# Configure page
st.set_page_config(
    page_title="TechVision Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Main content styling */
    .main {
        background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        padding: 2rem;
    }
    
    /* Title styling */
    .main-title {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 3.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    
    /* Navigation styling */
    .nav-button {
        background-color: #3498db !important;
        color: white !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 25px !important;
        margin: 0.5rem 0;
    }
    
    /* Contact form styling */
    .contact-form {
        max-width: 600px;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Navigation functions
def navigate(page):
    st.session_state.current_page = page

# Page content definitions
def home_page():
    st.markdown('<div class="main-title">🚀 TechVision Analytics</div>', unsafe_allow_html=True)
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
            <h2>Transform Your Business with Data Insights</h2>
            <p>Leverage cutting-edge AI and machine learning solutions to drive innovation and growth.</p>
            <ul>
                <li>📊 Advanced Analytics</li>
                <li>🤖 AI-Powered Solutions</li>
                <li>🔒 Secure Cloud Infrastructure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800", 
                caption="Data Analytics Visualization")

    # Features Section
    st.markdown('<h2 style="text-align: center; margin: 2rem 0;">Our Services</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    features = [
        ("📈", "Predictive Analytics", "Forecast trends and make data-driven decisions"),
        ("🤖", "AI Automation", "Streamline operations with intelligent automation"),
        ("🔐", "Cybersecurity", "Protect your digital assets with enterprise-grade security")
    ]
    
    for col, (icon, title, text) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="font-size: 2.5rem; text-align: center;">{icon}</div>
                <h3 style="text-align: center;">{title}</h3>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

def about_page():
    st.markdown('<div class="main-title">📖 About Us</div>', unsafe_allow_html=True)
    
    st.markdown("""



<div class="card">
    <h2>Who We Are..?</h2>
    <p>We are a team of data scientists, engineers, and business strategists 
    dedicated to transforming raw data into actionable insights. We empower businesses through innovative technology solutions and 
    data-driven decision making.</p>
    
   
</div>
""", unsafe_allow_html=True)

    # Team Section
    st.markdown('<h2 style="margin: 2rem 0;">Meet the Team</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    team = [
        ("Sarah Johnson", "CEO & Founder", "https://images.unsplash.com/photo-1580489944761-15a19d654956"),
        ("Michael Chen", "CTO", "https://images.unsplash.com/photo-1544725176-7c40e5a71c5e"),
        ("Emma Wilson", "Lead Data Scientist", "https://images.unsplash.com/photo-1544005313-94ddf0286df2")
    ]
    
    for col, (name, role, img) in zip(cols, team):
        with col:
            st.markdown(f"""
            <div class="card">
                <img src="{img}" style="width: 100%; border-radius: 10px; margin-bottom: 1rem;">
                <h3>{name}</h3>
                <p>{role}</p>
            </div>
            """, unsafe_allow_html=True)

def contact_page():
    st.markdown('<div class="main-title">📧 Contact Us</div>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        st.markdown("""
        <div class="contact-form">
            <div class="card">
                <h2>Get in Touch</h2>
                <p>We'd love to hear from you! Please fill out the form below:</p>
        """, unsafe_allow_html=True)
        
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                st.success("Message sent successfully! We'll respond within 24 hours.")
            else:
                st.error("Please fill in all required fields")
        
        st.markdown("</div></div>", unsafe_allow_html=True)

# Navigation Sidebar
with st.sidebar:
    st.image("logo.png", width=200)
    st.markdown("## Navigation")
    
    pages = {
        "🏠 Home": "Home",
        "📖 About": "About",
        "📧 Contact": "Contact"
    }
    
    for label, page in pages.items():
        if st.button(label, key=page, use_container_width=True, 
                    type="primary" if st.session_state.current_page == page else "secondary"):
            navigate(page)
    
    st.markdown("---")
    st.markdown("""
    **Connect with us:**
    - [LinkedIn](#)
    - [Twitter](#)
    - [GitHub](#)
    """)

# Page routing
if st.session_state.current_page == "Home":
    home_page()
elif st.session_state.current_page == "About":
    about_page()
elif st.session_state.current_page == "Contact":
    contact_page()