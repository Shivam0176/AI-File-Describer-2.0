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
    print(task)
    Generate_Button = st.button("Generate")


    if Generate_Button:
        if task == ['describe']:
            st.subheader("File Description")
        elif task == ['caption']:
            st.subheader("The Caption is")
        elif task == ['summarize']:
            st.subheader("File Summary")
        elif task == ['subtitle']:
            st.subheader("Subtitles")
        
        
        for file in uploaded_file:

            content = describe_File(file,task)              #pushing uploaded file and task to the function
            st.write(content)                               #Writing the Content
        # print(content)                                
        # print("Now it's here")




                                                               
