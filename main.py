import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise Exception("no api key")

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model='gemini-2.5-flash', contents= prompt)
    
if  response.usage_metadata is None:
    raise RuntimeError('no tokens used')

usage=response.usage_metadata
prompt_tokens = usage.prompt_token_count
completion_tokens = usage.candidates_token_count
total_used = usage.total_token_count


print(f'Prompt: {prompt}')
print(f'Response: {response.text}')
print(f'Prompt tokens: {prompt_tokens}')
print(f'Response tokens: {completion_tokens}')
print(f'Total tokens: {total_used}')


