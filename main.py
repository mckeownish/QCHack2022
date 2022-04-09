##
import streamlit as st

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

st.set_page_config(layout="centered", page_icon="💬", page_title="Commenting app")

# Data visualisation part

st.title("Initial Front End Push!")
st.write("Our exciting first step!")

# if __name__ == '__main__':
#     main()