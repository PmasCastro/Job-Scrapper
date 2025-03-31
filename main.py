import ollama
from IPython.display import Markdown, display, update_display


MODEL_LLAMA = 'llama3.2' 

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

system_prompt = "You are a very intelligent and helpful AI that is extremly good at helping programming beginners"

user_prompt = "Please give a detailed explanation of the following question: " + question


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = ollama.chat(model=MODEL_LLAMA, messages=messages)
reply = response['message']['content']
print (reply)