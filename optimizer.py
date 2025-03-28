import os
from pydantic import BaseModel, Field
import datetime as dt

import instructor
from openai import OpenAI
from dotenv import load_dotenv
from anthropic import Anhtropic
import google.generativeai as genai

load_dotenv()


class DataModel(BaseModel):
    name: str
    age: int
    birthday: dt.date
    gender: str = Field(..., description='Either M for male or F for female')



##Optimizing OpenAI Output
# client = instructor.from_openai(OpenAI())

# response = client.chat.completions.create(
#     model='gpt-4o',  
#     messages=[  
#         {
#             'role': 'user',
#             'content': f'Mike was born on April 4th, 1990. Today is {dt.date.today()}. Fill the data model based on this information.'
#         }
#     ],
#     response_model=DataModel

# )

# print(response)

##Ooptimizing Antrhopic Outpout(Quite the same with OpenAI but added max_tokens=1024 for defualt)
# client = instructor.from_anthropic(Anhtropic())

# response = client.chat.completions.create(
#     model='claude -3-7-sonnet-latest', 
#     max_tokens=1024, 
#     messages=[  
#         {
#             'role': 'user',
#             'content': f'Mike was born on April 4th, 1990. Today is {dt.date.today()}. Fill the data model based on this information.'
#         }
#     ],
#     response_model=DataModel

# )

# print(response)


#Gemini Output Optimization 
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

client = instructor.from_gemini(
    genai.GenerativeModel(
    model_name = 'models/gemini-2.0-flash'
),
    mode=instructor.Mode.GEMINI_JSON
)


response = client.messages.create(
    model='claude -3-7-sonnet-latest', 
    max_tokens=1024, 
    messages=[  
        {
            'role': 'user',
            'content': f'Mike was born on April 4th, 1990. Today is {dt.date.today()}. Fill the data model based on this information.'
        }
    ],
    response_model=DataModel

)

print(response)

