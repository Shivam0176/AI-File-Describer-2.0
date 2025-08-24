from google.genai import types
from google import genai
import streamlit as st
import mimetypes

GEMINI_API_KEY = "AIzaSyDwfBwNVK1zQ2zSYZg1u01aNMmIKEtLEIU"
client = genai.Client(api_key=GEMINI_API_KEY)

def describe_File(file_path,task):
    mime_type,_ = mimetypes.guess_type(file_path.name)                  #  Finding the type of Uploaded File
    print(mime_type)
    file_bytes = file_path.read()

    if task == []:
        return "Choose Task To Perform"

    else:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(
                    data=file_bytes,
                    mime_type=mime_type),

                    f'{task} this file'
            ]
        )
        print(task)
        print("response genrated")
        return response.text                                                #Returning the response


if __name__ == "__main__":
    describe_File()
