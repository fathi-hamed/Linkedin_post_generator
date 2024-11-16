# import streamlit as st
# from few_shot import FewShotPosts
# from post_generator import generate_post


# # Options for length and language
# length_options = ["Short", "Medium", "Long"]
# language_options = ["English", "French","Arabic"]


# # Main app layout
# def main():
#     st.subheader("LinkedIn Post Generator")

#     # Create three columns for the dropdowns
#     col1, col2, col3 = st.columns(3)

#     fs = FewShotPosts()
#     tags = fs.get_tags()
#     with col1:
#         # Dropdown for Topic (Tags)
#         selected_tag = st.selectbox("Topic", options=tags)

#     with col2:
#         # Dropdown for Length
#         selected_length = st.selectbox("Length", options=length_options)

#     with col3:
#         # Dropdown for Language
#         selected_language = st.selectbox("Language", options=language_options)



#     # Generate Button
#     if st.button("Generate"):
#         post = generate_post(selected_length, selected_language, selected_tag)
#         st.write(post)


# # Run the app
# if __name__ == "__main__":
#     main()


import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "French", "Arabic"]

# Custom CSS to improve styling
st.markdown("""
    <style>
        .main {
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .header {
            font-size: 2.5rem;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 1.5rem;
            color: #FF5722;
            text-align: center;
        }
        .stSelectbox>div>div>input {
            padding: 10px;
            font-size: 1.1rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.2rem;
            border-radius: 5px;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stText {
            font-size: 1.1rem;
            padding: 15px;
            background-color: #f7f7f7;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main app layout
def main():
    st.markdown('<div class="header">LinkedIn Post Generator</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Generate the perfect LinkedIn post with ease</div>', unsafe_allow_html=True)

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags, help="Choose a tag that matches your content's focus.")

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options, help="Select how long you want your post to be.")

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options, help="Select the language for your post.")

    # Add some space
    st.markdown("<br>", unsafe_allow_html=True)

    # Generate Button
    if st.button("Generate", help="Click here to generate your LinkedIn post!"):
        post = generate_post(selected_length, selected_language, selected_tag)
        
        # Display the generated post in a nice box
        st.markdown(f'<div class="stText">{post}</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
