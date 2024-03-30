import os
import streamlit as st

def list_txt_files(folder_path):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    return txt_files

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    st.title('Text File Viewer')

    # Hardcoded folder path
    folder_path = r'D:\Github\Notepad\Saved_notes'

    txt_files = list_txt_files(folder_path)

    if not txt_files:
        st.warning(f'Empty notes: Try writing more Dear')
    else:
        st.write('## List of your notes')
        for txt_file in txt_files:
            file_name = os.path.splitext(txt_file)[0]  
            if st.button(file_name):
                file_path = os.path.join(folder_path, txt_file)
                text_content = read_txt_file(file_path)
                # st.write('### {} :'.format(file_name))
                st.write(text_content)

if __name__ == "__main__":
    main()