#qr gen
import os
import streamlit as st
import segno
import time 
from PIL import Image


def list_txt_files(folder_path):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    return txt_files

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def qr(fname,data):
    bpath=r'D:\Github\Notepad\qr'
    qpath = os.path.join(bpath, f"{fname}.png")
    
    qrcode = segno.make_qr(data)
    qrcode.save(
        qpath,
        scale=5,
        border=1,)
    return qpath


def main():
    st.title('Share notes')

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
                # st.write(text_content)
                qp=qr(file_name,text_content)
                time.sleep(3)
                img= Image.open(qp)
                st.image(img, caption=file_name, width=150)
                
                

if __name__ == "__main__":
    main()
    
    
# import segno
# import os

    
# qr('newqr','naya mall')


# import streamlit as st
# from PIL import Image

# def main():
#     st.title("Display Image on Button Click")
    
#     # Define the path to the image
#     image_path = r"D:\Github\Notepad\qr\newqr.png"
    
#     # Load the image
#     image = Image.open(image_path)
    
#     # Create a button
#     button_clicked = st.button("Display Image")
    
#     # Check if the button is clicked
#     if button_clicked:
#         # Display the image
#         st.image(image, caption="Your Image", width=150)

# if __name__ == "__main__":
#     main()
