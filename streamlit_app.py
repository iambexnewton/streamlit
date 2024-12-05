import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
     page_title='Streamlit Layout Test',
     layout="wide",
     initial_sidebar_state="expanded",
)

#Style
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #F3F2EF;
        border-right: 1px solid #d1d3ca;
    }

     [data-testid=stHeader] {
        background-color: #F3F2EF;
height: 80px;
        border-right: 1px solid #d1d3ca;
            border-bottom: 1px solid #d1d3ca;
    }
 [type="button"]:hover {
    color: blue;
}
</style>
""", unsafe_allow_html=True)


#tabs
tab1, tab2, tab3 = st.tabs(["Chart", "Graph", "Any other"])

with tab1:
    st.header("Chart")
    st.write('A chart will go hear when I have figured that out ')
    # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("Graph")
    st.write('A graph will go hear when I have figured that out ')
    # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Any other")
    # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.header('st.write')

#sidebar
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "This is a test for a dropdown to select data",
    ("Email", "Home phone", "Mobile phone")
)



# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a radio button",
        ("First Button", "Second Button")
    )



st.write('text on the page?')


if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')