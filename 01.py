import streamlit as st
import os

def main():
    st.title("Note Taking App")
    
    # Get the default note title
    default_title = get_default_title()
    
    # Text input for users to input the note title
    note_title = st.text_input("Enter note title:", default_title)
    
    # Text area for users to input their note
    note_content = st.text_area("Write your note here:")
    
    # Button to save the note
    if st.button("Save Note"):
        save_note_to_file(note_title, note_content)
        st.success("Note saved successfully!")

def get_default_title():
    # Define the folder path where notes will be saved
    folder_path = r"D:\Github\Notepad\Saved_notes"  # Update this with your desired folder path
    
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Check for existing files in the folder
    existing_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    
    # If there are existing files, find the next available note number
    if existing_files:
        note_number = 1
        while f"note{note_number:02d}.txt" in existing_files:
            note_number += 1
        return f"note{note_number:02d}"
    else:
        return "note01"

def save_note_to_file(note_title, note_content):
    # Define the folder path where notes will be saved
    folder_path = r"D:\Github\Notepad\Saved_notes"  # Update this with your desired folder path
    
    # Save the note with the provided title in the specified folder
    file_path = os.path.join(folder_path, f"{note_title}.txt")
    with open(file_path, "w") as file:
        file.write(note_content)

if __name__ == "__main__":
    main()
