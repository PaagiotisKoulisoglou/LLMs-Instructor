import os
from pydantic import BaseModel, Field
import datetime as dt
from enum import Enum
from typing import List, Optional

import instructor
from openai import OpenAI
from dotenv import load_dotenv
from anthropic import Anhtropic
import google.generativeai as genai

load_dotenv()

class MovieGenreEnum(Enum):
    ACTION = "ACTION"
    DRAMA = "DRAMA"
    MYSTERY = "MYSTERY"
    ROMANCE = "ROMANCE"
    ANIMATION = "ANIMATION"
    COMEDY = "COMEDY"
    OTHER = "OTHER"  # Corrected spelling

class Movie(BaseModel):
    title: str
    release_year: int
    genre: List[MovieGenreEnum]


class ResponseModel(BaseModel):
    reasoning_text: str = Field(..., description='Explain in long detail why you decided exactly on these five movies')
    recommended_movies: List[Movie]

#Optimized OpenAI Output
client = instructor.from_openai(OpenAI())

response = client.chat.completions.create(
    model='gpt-4o',  
    messages=[  
        {
            'role': 'user',
            'content': f'I live Shitter Island.It is one of my favorite movies. Can you recommend me some movies that are similar to it?'
        }
    ],
    response_model=ResponseModel
)

print (response.reasoning_text)
for movie in response.recommended_movies:
    print (f'Movie: {movie.title}, ({movie.release_year}), Genre: {", ".join([g.name for g in movie.geners])}')


#The same can be done for Anthropics and Gemini like optimizer.py