#qr gen
import os
import streamlit as st
import segno
import time 
from PIL import Image
import qrcode
from PIL import Image
import cv2
import pyzbar.pyzbar as pyzbar

def qr(fname,text, desired_width=500, desired_height=500):
    bpath=r'D:\Github\Notepad\qr'
    qpath = os.path.join(bpath, f"{fname}.png")
    # Create a QRCode object with appropriate settings for long text
    qr = qrcode.QRCode(
        version=10,  # Adjust version for more data (up to 40 for very long text)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each QR code box
        border=4,  # Margin around the QR code
    )
    qr.add_data(text)
    qr.make(fit=True)  # Optimize QR code for best fit

    # Generate the QR code data (black and white squares)
    qr_data = qr.make_image(fill_color="black", back_color="white")

    # Create a blank image with the desired size
    img = Image.new("L", (desired_width, desired_height), 255)  # White background

    # Calculate scaling factor based on aspect ratio preservation
    x_scale = desired_width / qr_data.size[0]
    y_scale = desired_height / qr_data.size[1]
    scale = min(x_scale, y_scale)  # Maintain aspect ratio

    # Resize the QR code data while preserving sharp edges
    resized_qr = qr_data.resize((int(qr_data.size[0] * scale), int(qr_data.size[1] * scale)), Image.ANTIALIAS)

    # Paste the resized QR code onto the blank image, centered
    paste_x = int((desired_width - resized_qr.size[0]) / 2)
    paste_y = int((desired_height - resized_qr.size[1]) / 2)
    img.paste(resized_qr, (paste_x, paste_y))

    # Save the final QR code image
    img.save(qpath)
    print(f"QR code generated successfully and saved to '{qpath}'!")
    return qpath

def read_qr_code(image_path):

  try:
    # Read the image in grayscale mode
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = image_path

    # Detect QR codes in the image
    decoded_objects = pyzbar.decode(img)

    # Extract data from the first detected QR code (if available)
    if decoded_objects:
      return decoded_objects[0].data.decode("utf-8")
    else:
      return None

  except (FileNotFoundError, cv2.error):
    print(f"Error: Could not read image at '{image_path}'.")
    return None

def list_txt_files(folder_path):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    return txt_files

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def qr2(fname,data):
    bpath=r'D:\Github\Notepad\qr'
    qpath = os.path.join(bpath, f"{fname}.png")
    
    qrcode = segno.make_qr(data)
    qrcode.save(
        qpath,
        scale=5,
        border=1,)
    return qpath


def main():
    st.title('Notes on the Goo..')

    # Hardcoded folder path
    folder_path = r'D:\Github\Notepad\Saved_notes'

    txt_files = list_txt_files(folder_path)

    if not txt_files:
        st.warning(f'Empty notes: Try writing more Dear')
    else:
        if st.toggle("Generate QR"):
            st.write('## List of your notes')
            for txt_file in txt_files:
                file_name = os.path.splitext(txt_file)[0]  
                if st.checkbox(file_name):
                    
                    file_path = os.path.join(folder_path, txt_file)
                    text_content = read_txt_file(file_path)
                    
                    
                    
                    # st.write('### {} :'.format(file_name))
                    # st.write(text_content)
                    qp=qr(file_name,text_content)
                    time.sleep(2)
                    
                    with open(qp, "rb") as file:
                        btn = st.download_button(
                                label="Download image",
                                data=file,
                                file_name=file_name,
                                mime="image/png"
                            )
                    if st.toggle('Show QR'):
                        img= Image.open(qp)
                        st.image(img, caption=file_name)
        if st.toggle('Read QR'):
            st.title("QR Code Reader")
            uploaded_file = st.file_uploader("Choose a QR Code image")
            qr_text = st.empty()  # Placeholder for decoded text

            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                # st.image(image, caption="Uploaded QR Code Image", use_column_width=True)
                # st.write(image)
                qr_data = read_qr_code(image)
                
                if qr_data:
                    qr_text.markdown(qr_data)
                else:
                    qr_text.text("No QR code found in the image.")


                

if __name__ == "__main__":
    main()