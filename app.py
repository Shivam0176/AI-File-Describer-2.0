import streamlit as st
from describer import describe_File
from google import genai
from google.genai import types
import mimetypes


options = ['describe','caption','summarize','subtitle']                 #task to perform


st.set_page_config(page_title="AI File Describer",page_icon="🤖")           #Basic User Interface
st.title("AI File Describer")
st.write("Upload a file (image, video, pdf etc) and I'll describe it!")
uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=True)        # File Uploader


if uploaded_file:
    task = st.selectbox(                                                      #   SELECTBOX UI
        "Select Task you want to perform",
        options,
        accept_new_options=True
    )
    Generate_Button = st.button("Generate")
    st.subheader("Hello this is a subheader")


    if Generate_Button:
        print(task)
        if task in options:
            st.subheader(task)
        
        
        for file in uploaded_file:

            content = describe_File(file,task)              #pushing uploaded file and task to the function
            st.write(content)                               #Writing the Content




                                                               
