# from dotenv import load_dotenv
# import os
# load_dotenv()
# import google.generativeai as genai

# dt='''

# Today was a mixed bag of emotions. The day started with a challenging session on machine learning in college. It was tough, but I know it's all part of the learning process in pursuing my passion for data science.

# During lunch, I had a great time with my friends. Good food and laughter always lighten up the day. However, once back home, I struggled to focus on my studies. My phone proved to be a major distraction, and I can't help but feel disappointed in my lack of concentration.

# Talking with my family made me realize how much I miss them. Living away from home for college isn't easy, especially when special occasions like Holi are around the corner. Knowing I won't be able to be there for it made me feel sad, as it'll be the first time celebrating without them. Yet, I understand that these sacrifices are necessary steps toward a brighter future.

# Despite the challenges and emotions, I'm determined to stay focused on my goals and make the most of each day, knowing that every sacrifice today will pave the way for a better tomorrow.

# '''
# # Do not reply in markdown format

# ait='''

# Craft a reply in speech format , that i can read it out , so means i need direct speech,
# not any points or heading and all
# also you may use multiple emoji so that it looks good
# and it should be short and simple 


# '''

# def poopmt(que,trpt='No instruction right now'):
#     poompt = '''
#     Suppose you are psychologist and your patient is telling you about his day, and it goes like this: {}

#     what will be your reply(in 3-4 sentences) to this , analize his sentiments via his day and craft a beautiful reply which will be 
#     claming and motivating for him , you may also rant about things he told gone bad with him through out day 
#     and may also include motivational quotes( which would be in bold)
    
#     Also i may give you some instructions below.
    
    
    
#     Additional Instructions: {}
# '''.format(que,trpt)
#     return poompt


# def gen_rpl(dt):
#     genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#     model = genai.GenerativeModel('gemini-pro')
#     pmt=poopmt(dt,ait)
#     # print(pmt)
#     answer = model.generate_content(pmt)
#     print(answer.text)
#     return answer.text


#cheg stuff

ans='''
The notes do not mention what a sigmoid function is.

According to my knowledge, the sigmoid function is a mathematical function that is commonly used in neural networks to introduce non-linearity. It is defined as:

```
sigmoid(x) = 1 / (1 + e^(-x))
```

The sigmoid function takes a real-valued input and outputs a value between 0 and 1. It is often used as an activation function in neural networks because it is non-linear and differentiable. This allows neural networks to learn complex relationships between input and output data.

For example, in a binary classification problem, a sigmoid function can be used to output a probability that a given data point belongs to a particular class.
'''

cheg='According to my knowledge'


if cheg in ans:
    index = ans.index(cheg) + len(cheg)
    info_after_cheg = ans[index+2:].strip()
    print(info_after_cheg)
