from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is working"

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get('text')

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid text! Please try again."

    return jsonify(result)

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)