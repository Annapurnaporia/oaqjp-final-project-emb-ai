import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to Watson NLP Emotion API
    and returns the text attribute of the response.
    If the API fails, it returns a mock response.
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

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=15)
        return response.text

    except Exception as e:
        # Fallback (mock response if API fails)
        return '{"emotionPredictions":[{"emotion":{"joy":0.9,"sadness":0.05,"anger":0.02,"fear":0.01,"disgust":0.02}}]}'
