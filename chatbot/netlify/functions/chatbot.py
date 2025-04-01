import json
from transformers import pipeline

def handler(event, context):
    try:
        # Usar DialoGPT (entrenado para diálogos)
        chatbot = pipeline("text-generation", 
                        model="microsoft/DialoGPT-small",
                        max_length=100,
                        temperature=0.9)  # Más creativo

        user_input = json.loads(event["body"]).get("text")
        response = chatbot(user_input)[0]["generated_text"]

        return {
            "statusCode": 200,
            "body": json.dumps({"response": response})
        }
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}