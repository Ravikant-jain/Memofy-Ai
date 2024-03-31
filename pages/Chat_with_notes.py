import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai


def poopmt(notes,que):
    poompt = '''
    I made these notes: {}

    I want you to go through these notes and answer my question: {}   
    
    If you can't find answer through these notes , use your knowledge , but then specify by saying that 'The answer can be found in your note , but according to my knowledge:'
    you can also answer by using examples it will be a plus point.
    Also i may give you some instructions below.
    Just a suggetion that bullet points make notes easier to understand.
    
    Instructions: No intructions right now

'''.format(notes,que)
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
def ans(text,que):
    # Placeholder enhancement function, you can replace it with your actual enhancement logic
    
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    pmt=poopmt(text,que)
    # print(pmt)
    answer = model.generate_content(pmt)
    # print(answer.text)
    
    # enhanced_text = text.upper() # For example, converting text to uppercase
    # print(enhanced_text)
    return answer.text

def uptxt(notes,que,ans):
    fn='''
    {}
    
    Question: {}
    
    Answer: {}
    
    '''.format(notes,que,ans)
    
    return fn

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
    st.write(selected_file)
    # if st.toggle("Show notes"):
    #     st.markdown(file_content)
    with st.expander("Click to see selected note"):
        st.markdown(file_content)

    # st.markdown(file_content)
    que = st.text_input('Your Question')
    
# Text areas for displaying file content and enhanced text
left_text = st.empty()
right_text = st.empty()

# Button to enhance text in the right textbox
if left_text.text:
    if st.checkbox('Ask'):
        
        with st.spinner('Let me think...'):
            enhanced_text = ans(file_content,que)
        st.markdown(enhanced_text)
        # print(enhanced_text)
        
        cheg='According to my knowledge'
        if cheg in enhanced_text:
            if st.checkbox("As it isn't in your notes , you want to add the QnA in the notes?"):
                print(1)
                index = enhanced_text.index(cheg) + len(cheg)
                info_after_cheg = enhanced_text[index+2:].strip()
                print(2)
                fn=uptxt(file_content,que,info_after_cheg)
                write_txt_file(file_path, fn)
                print(fn)
                print(3)
                st.success('Added in Notes successfully!')
                
                with st.expander("Click to see the updated note"):
                    st.markdown(fn)

        

