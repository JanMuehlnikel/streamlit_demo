import streamlit as st
from PIL import Image


def app():
    # Sidebar
    st.sidebar.title('Check Coherence')

    for i in range(6):
        st.sidebar.write(' ')
    st.sidebar.selectbox('Select NDC', ('South Africa', 'Ethiopia'))

    # Container
    st.markdown("<h1 style='text-align: center; color: white;'>SDSN X GIZ Policy Tracing</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2,7,1])
    image = Image.open('pic1.PNG')
    c2.image(image)