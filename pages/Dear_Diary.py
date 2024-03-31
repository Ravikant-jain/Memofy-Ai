#diary
import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai




ait='''

Craft a reply in speech format , that i can read it out , so means i need direct speech,
not any points or heading and all
you should address them as buddy or friend
also you may use multiple emoji so that it looks good
and it should be short and sweet


'''

def poopmt(que,trpt='No instruction right now'):
    poompt = '''
    Suppose you are psychologist and your patient is telling you about his day, and it goes like this: {}

    what will be your reply(in 3-4 sentences) to this , analize his sentiments via his day and craft a beautiful reply which will be 
    claming and motivating for him , you may also rant about things he told gone bad with him through out day 
    and may also include motivational quotes( which would be in bold, in diffrent line)
    Also i may give you some instructions below.
    
    
    
    Additional Instructions: {}
'''.format(que,trpt)
    return poompt


def gen_rpl(dt):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    pmt=poopmt(dt,ait)
    # print(pmt)
    answer = model.generate_content(pmt)
    return answer.text



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





def main():
    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    page_title = f"My Day: {current_date}"
    st.title(page_title)
    
    # Get the default note title
    default_title = get_default_title()
    
    # Text area for users to input their diary entry
    diary_entry = st.text_area("Hey , how was your day ?", height=200)
    
    # Button to save the diary entry
    if st.button("Save Entry"):
        save_diary_entry(default_title, diary_entry)
        st.balloons()
        st.success("Diary entry saved successfully!")
        with st.spinner('Let me read about your day 😊...'):
            es=gen_rpl(diary_entry)
        st.markdown(es)
        st.caption('-Your Diary 😊')

if __name__ == "__main__":
    main()
