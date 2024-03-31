import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai


def poopmt(que,trpt='No instruction right now'):
    poompt = '''
    I made these notes: {}

    I want you to enchance these notes by using your knowledge, make them more detailed by filling them with more content.    
    Adding examples to them will be a plus point.
    Also i may give you some instructions below.
    You can add more information in my notes and make them simpler to understand.
    Well just a suggetion that bullet points make notes easier to understand.
    
    Instructions: {}
'''.format(que,trpt)
    return poompt

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-pro')
# pmt=poopmt('DataScience- RNN,CNN,ANN,KNN')
# # print(pmt)
# answer = model.generate_content(pmt)
# print(answer.text)

# Function to read text file
def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content



def write_txt_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Function to enhance text (temporary function)
def enhance_text(text):
    # Placeholder enhancement function, you can replace it with your actual enhancement logic
    
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    pmt=poopmt(text)
    # print(pmt)
    answer = model.generate_content(pmt)
    # print(answer.text)
    
    # enhanced_text = text.upper() # For example, converting text to uppercase
    # print(enhanced_text)
    return answer.text

# Path to the folder containing text files
folder_path = r"D:\Github\Notepad\Saved_notes"

# Get list of all text files in the folder
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Sidebar with buttons for each text file
selected_file = st.sidebar.selectbox('Select a file:', txt_files)

# Display selected file content in left textbox
if selected_file:
    file_path = os.path.join(folder_path, selected_file)
    file_content = read_txt_file(file_path)
    st.write('Your Nukes')
    st.markdown(file_content)
    
# Text areas for displaying file content and enhanced text
left_text = st.empty()
right_text = st.empty()

# Button to enhance text in the right textbox
if left_text.text:
    if st.checkbox('Enhance'):
        enhanced_text = enhance_text(file_content)
        st.markdown(enhanced_text)
        
        if st.button('Save'):
            write_txt_file(file_path, enhanced_text)
            st.markdown('Notes Enhanced successfully!')