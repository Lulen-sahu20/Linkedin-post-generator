import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# App-wide settings
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #4a4a4a;
            text-align: center;
            margin-bottom: 1rem;
        }
        .subtext {
            text-align: center;
            font-size: 1rem;
            color: #6c757d;
            margin-bottom: 2rem;
        }
        .stButton > button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            margin-top: 1rem;
        }
        .stButton > button:hover {
            background-color: #0056b3;
        }
        .post-box {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid #e3e3e3;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)


# Options for dropdowns
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    st.markdown('<div class="title">💼 LinkedIn Post Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Generate engaging LinkedIn posts in seconds using AI 🚀</div>', unsafe_allow_html=True)

    fs = FewShotPosts()
    tags = fs.get_tags()

    # Layout for dropdowns
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("📌 Topic", options=tags)
    with col2:
        selected_length = st.selectbox("📏 Length", options=length_options)
    with col3:
        selected_language = st.selectbox("🗣️ Language", options=language_options)

    # Generate post
    if st.button("Generate"):
        with st.spinner("✨ Generating your LinkedIn post..."):
            post = generate_post(selected_length, selected_language, selected_tag)

        st.markdown("### ✅ Generated Post:")
        st.markdown(f'<div class="post-box">{post}</div>', unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()
