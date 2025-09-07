from google.genai import types
from google import genai
import streamlit as st
import mimetypes

GEMINI_API_KEY = "AIzaSyDwfBwNVK1zQ2zSYZg1u01aNMmIKEtLEIU"
client = genai.Client(api_key=GEMINI_API_KEY)

def describe_File(file,task):                                                
    # print(mime_type)
    

    if task == []:
        return "Choose Task To Perform"

    else:
        input_data = []
        print("pointer is here")

                                         # To detect type and append data of multiple files
        mime_type,_ = mimetypes.guess_type(file.name)
        file_bytes = file.read()
        part = types.Part.from_bytes(data=file_bytes,
                                        mime_type=mime_type)
            

        input_data.append(f"Task: {task}")
        print(input_data)
        print("File pointer 2nd position")

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[part,f'{task}']
        )
        
        print(f"response genrated for file : {file.name}")
        return response.text                                                #Returning the response


if __name__ == "__main__":
    describe_File()
