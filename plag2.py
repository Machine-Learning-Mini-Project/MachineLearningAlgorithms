import os
from dotenv import load_dotenv
import requests

load_dotenv()

PREPOSTSEO_API_KEY = os.getenv('PREPOSTSEO_API_KEY')

url = " https://www.prepostseo.com/ajax/checkPlagv5 "

payload={
    # 'key': PREPOSTSEO_API_KEY,
    'query_list': 'Inside that cage there was a green teddy bear'
    }
headers = {}

response = requests.post(url, headers=headers, data=payload)
response_json = response.text
print(response_json)


