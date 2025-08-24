import streamlit as st
from describer import describe_File
from google import genai
from google.genai import types
import mimetypes

GEMINI_API_KEY = "AIzaSyDwfBwNVK1zQ2zSYZg1u01aNMmIKEtLEIU"
client = genai.Client(api_key=GEMINI_API_KEY)

options = ['describe','caption','summarize','subtitle']                 #task to perform


st.set_page_config(page_title="AI File Describer",page_icon="🤖")           #Basic User Interface
st.title("AI File Describer")
st.write("Upload a file (image, video, pdf etc) and I'll describe it!")
uploaded_file = st.file_uploader("Choose a file")


if uploaded_file:
    task = st.multiselect(                                                      #   MULTISELECT UI
        "Select Task you want to perform",
        options
    )
    print(task)

    if task == []:                                                                 #Pass if no task is Selected
        pass

    else:
        content = describe_File(uploaded_file,task)                                #pushing uploaded file and task to the function

        if options == ['describe']:
            st.subheader("File Description")
        elif options == ['caption']:
            st.subheader("The Caption is")
        elif options == ['summarize']:
            st.subheader("File Summary")
        elif options == ['subtitle']:
            st.subheader("Subtitles")



        st.write(content)                                                           #Writing the Content
