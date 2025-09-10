import streamlit as st
from describer import describe_File
from google import genai
from google.genai import types
import mimetypes
from Keyword_extractor import Keyword_Extractor
from searching_keywords import google_search


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


    if Generate_Button:
        print(task)
        if task in options:
            st.subheader(task)
        
        
        for file in uploaded_file:

            content = describe_File(file,task)              #pushing uploaded file and task to the function
            st.write(content)                               #Writing the Content
            keywords = Keyword_Extractor(content)           #Extracting keywords from the content
            results = google_search(keywords)               #Searching the keywords using Google search engine
            if results:
                print("="*30)

                for i, item in enumerate(results):
                    print(f"{i+1}. {item.get("title")}")
                    print(f"     Link: {item.get('link')}")
                    print(f"     Snippet:{item.get('snippet')}\n")

            else:
                print("No results found or an error occurred")





                                                               
