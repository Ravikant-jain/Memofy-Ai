# Long text to be encoded
long_text = """- **Recurrent Neural Networks (RNNs)**
  - Used for sequential data with dependencies between elements
  - Examples: Natural language processing (NLP), speech recognition
  - Types of RNNs include:
    - Long short-term memory (LSTM)
    - Gated recurrent unit (GRU)

- **Convolutional Neural Networks (CNNs)**
  - Used for data with grid-like structure, such as images and audio
  - Feature extraction is done through convolutions, allowing for spatial relationships to be learned
  - Examples: Image classification, object detection
  - Layers in CNNs include:
    - Convolutional layers
    - Pooling layers
    - Fully connected layers

- **K-Nearest Neighbors (KNN)**
  - Non-parametric algorithm for classification and regression
  - Assigns a label or value to a new data point based on the majority vote or average of its k nearest neighbors in the training set
  - Examples: Handwritten digit recognition, medical diagnosis
  - Hyperparameters:
    - Number of neighbors (k)
    - Distance metric used for calculating nearest neighbors"""

import qrcode
from PIL import Image
import cv2
import pyzbar.pyzbar as pyzbar

def generate_qr_code(text, desired_width=500, desired_height=500, filename="pages\long_text_qrcode.png"):


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
    img.save(filename)

    print(f"QR code generated successfully and saved to '{filename}'!")

# Example usage
generate_qr_code("Your lengthy text here")#pass fname also 


def read_qr_code(image_path):

  try:
    # Read the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

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

# Example usage
# image_path = r"D:\Github\Notepad\qr\New Notes.png"  # Replace with your actual image path
# qr_data = read_qr_code(image_path)

# if qr_data:
#   print("QR code data:", qr_data)
# else:
#   print("No QR code found in the image.")
