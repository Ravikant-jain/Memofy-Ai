

# from dotenv import load_dotenv
# import os
# load_dotenv()
# import google.generativeai as genai


# def poopmt(que,trpt='No instruction right now'):
#     poompt = '''
#     I made these notes: {}

#     I want you to enchance these notes by using your knowledge, make them more detailed by filling them with more content.    
#     Adding examples to them will be a plus point.
#     Also i may give you some instructions below.
#     You can add more information in my notes and make them simpler to understand.
#     Well just a suggetion that bullet points make notes easier to understand.
    
    
    
#     Instructions: {}
# '''.format(que,trpt)
#     return poompt



# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-pro')
# pmt=poopmt('DataScience- RNN,CNN,ANN,KNN')
# # print(pmt)
# answer = model.generate_content(pmt)
# print(answer.text)

