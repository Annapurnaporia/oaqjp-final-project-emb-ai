import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function sends text to Watson NLP Emotion API
    and returns the 'text' part of the response.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request
    response = requests.post(url, json=input_json, headers=headers)

    # Convert response to JSON
    response_json = response.json()

    # Return only the 'text' part of response
    return response_json["document_tone"]["tones"]
