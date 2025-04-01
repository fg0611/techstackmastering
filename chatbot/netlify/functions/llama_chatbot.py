import json
import os
from dotenv import load_dotenv
import requests

def handler(event, context):
    load_dotenv()
    model = 'mistralai/Mistral-7B-Instruct-v0.1'
    API_URL = f'https://api-inference.huggingface.co/models/{model}'
    headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

    print(headers)
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    user_input = json.loads(event["body"]).get("text")
    output = query({"inputs": user_input})

    print(output)

    msg1 = output[0].get('generated_text', '')
    # print('msg1: ', msg1)
    msg2 = msg1.split('ok?')[1]
    print('msg2: ', msg2)
    
    return {"statusCode": 200, "body": json.dumps(msg2)}