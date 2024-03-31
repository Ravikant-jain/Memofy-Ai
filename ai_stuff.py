from dotenv import load_dotenv
import os
load_dotenv()
import google.generativeai as genai

dt='''

Today was a mixed bag of emotions. The day started with a challenging session on machine learning in college. It was tough, but I know it's all part of the learning process in pursuing my passion for data science.

During lunch, I had a great time with my friends. Good food and laughter always lighten up the day. However, once back home, I struggled to focus on my studies. My phone proved to be a major distraction, and I can't help but feel disappointed in my lack of concentration.

Talking with my family made me realize how much I miss them. Living away from home for college isn't easy, especially when special occasions like Holi are around the corner. Knowing I won't be able to be there for it made me feel sad, as it'll be the first time celebrating without them. Yet, I understand that these sacrifices are necessary steps toward a brighter future.

Despite the challenges and emotions, I'm determined to stay focused on my goals and make the most of each day, knowing that every sacrifice today will pave the way for a better tomorrow.

'''
# Do not reply in markdown format

ait='''

Craft a reply in speech format , that i can read it out , so means i need direct speech,
not any points or heading and all
also you may use multiple emoji so that it looks good
and it should be short and simple 


'''

def poopmt(que,trpt='No instruction right now'):
    poompt = '''
    Suppose you are psychologist and your patient is telling you about his day, and it goes like this: {}

    what will be your reply(in 3-4 sentences) to this , analize his sentiments via his day and craft a beautiful reply which will be 
    claming and motivating for him , you may also rant about things he told gone bad with him through out day 
    and may also include motivational quotes( which would be in bold)
    
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
    print(answer.text)
    return answer.text
