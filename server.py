from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is working"

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('text')
    print("Received text:", text_to_analyze)

    try:
        result = emotion_detector(text_to_analyze)
        print("Result:", result)
        return str(result)
    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
