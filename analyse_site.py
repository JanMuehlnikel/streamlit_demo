import streamlit as st

def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: white;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)
        pic = st.file_uploader('Upload', type=['pdf'])

        if pic is not None:
            st.image(pic)
        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h1 style='text-align: center; color: white;'>no PDF uploaded ...</h1>",
                        unsafe_allow_html=True)
