import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise Exception("no api key")

client = genai.Client(api_key=api_key)
response = Client.models.generate_content("Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
                                          
print(response.text)

