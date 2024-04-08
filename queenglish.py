import os
from openai import OpenAI
from flask import Flask
# import openai
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import unicodedata
import html
html.entities.html5


# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_input = request.form['user_input']
#         return f"You entered: {user_input}"
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# openai.organization = "org-MbdHE411imWBGbOfYcvOw21T"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()
# OpenAI.api_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI()
# # openai.api_key = api_key



# print('test1')

# userLyrics = input('Enter your lyrics\n')

# userRegion = input("Choose a language/dialect\n 1 for Queen's English\n 2 for Ausie\n 3 for Irish\n 4 for South African\n 5 for Cockney\n")

# chatPrompt = "queen's english: "

# dialect = "co.uk"

# language = 'en'

# if userRegion == "2":
#     chatPrompt = " Australian slang: "
#     dialect = "com.au"
# elif userRegion == "3":
#     chatPrompt = "English-Irish slang: "
#     dialect = "ie"
# elif userRegion == "4":
#     chatPrompt = "South African slang: "
#     dialect = "co.za"
# elif userRegion == "5":
#     chatPrompt = "cockney slang: "
#     dialect = "co.uk"
#     pass

# # completion = openai.ChatCompletion.create(
# #   model="gpt-3.5-turbo",
# #   messages=[
# #     {"role": "user", "content": "Please translate the following text into " + chatPrompt + userLyrics}
# #   ]
# # )

# # translatedText = completion.choices[0].message.content

# prompt = "Please translate the following text into " + chatPrompt + userLyrics

# # Call the OpenAI API to generate a response
# # completion = client.completions.create(
# #     model="gpt-3.5-turbo",
# #     prompt=prompt,
# #     max_tokens=100,
# #     temperature=0
# # )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Please translate the following text into " + chatPrompt + userLyrics}
#     # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     # {"role": "user", "content": "Where was it played?"}
#   ]
# )

# # Get the generated translation
# translatedText = completion.choices[0].message.content

# print(translatedText)

# # Language in which you want to convert

# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=translatedText, lang=language, tld=dialect, slow=False)

# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("queenglish.mp3")

# # Playing the converted file
# os.system("start queenglish.mp3")

# print('test2')