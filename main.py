import ollama
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display

MODEL_LLAMA = 'llama3.2'

# http header that mimics real browser to bypass basic checks

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
} 

# We create an object called Website to handle data scraping. By abstracting the logic we can reuse it for any 
# url
class Website: 
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers, stream=True) #send http request to server
        soup = BeautifulSoup(response.content, 'html.parser') #get html content from server
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "img", "style", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

link = Website("https://plato.stanford.edu/entries/kant-hume-morality/")
print(link.text)




# system_prompt = "You are a very intelligent and helpful AI that is extremly good at helping programming beginners"

# user_prompt = "Please give a detailed explanation of the following question: "


# messages = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": user_prompt}
# ]

# response = ollama.chat(model=MODEL_LLAMA, messages=messages)
# reply = response['message']['content']
# print (reply)



