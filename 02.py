import streamlit as st
import os
from datetime import datetime

def main():
    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    page_title = f"My Day: {current_date}"
    st.title(page_title)
    
    # Get the default note title
    default_title = get_default_title()
    
    # Text area for users to input their diary entry
    diary_entry = st.text_area("Hey , how was your day ?")
    
    # Button to save the diary entry
    if st.button("Save Entry"):
        save_diary_entry(default_title, diary_entry)
        st.success("Diary entry saved successfully!")

def get_default_title():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    return f"The day-{current_date}"

def save_diary_entry(diary_title, diary_content):
    # Define the folder path where diary entries will be saved
    folder_path = r"D:\Github\Notepad\Saved_notes\Diary"  # Update this with your desired folder path
    
    # Save the diary entry with the provided title in the specified folder
    file_path = os.path.join(folder_path, f"{diary_title}.txt")
    with open(file_path, "w") as file:
        file.write(diary_content)

if __name__ == "__main__":
    main()
