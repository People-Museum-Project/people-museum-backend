from flask import Blueprint, request, jsonify, Response
from app.ai_handler import AIHandler

ai_bp = Blueprint('ai_bp', __name__)

@ai_bp.route("/generateText", methods=["POST"])
def generateText():
    data = request.get_json()
    prompt = data.get('prompt')
    model = data.get('model', 'gpt-3.5-turbo')  # default model if not provided
    ai_handler = AIHandler()
    result = ai_handler.generate_text(prompt, model)
    return jsonify({"message": "Text generated successfully", "data": result}), 200

@ai_bp.route("/askQuestion", methods=["POST"])
def askQuestion():
    data = request.get_json()
    question = data.get('question')
    assistant_id = data.get('assistantId')
    ai_handler = AIHandler()
    result = ai_handler.ask_question(question=question, assistant_id=assistant_id)
    return jsonify({"message": "Question answered successfully", "data": result}), 200

@ai_bp.route("/generateSamplePrompts", methods=["POST"])
def generateSamplePrompts():
    data = request.get_json()
    context = data.get('context')
    num_samples = data.get('num_samples', 1)
    max_words = data.get('max_words', 50)
    assistant_id = data.get('assistant_id')
    followups = data.get('followups', False)
    ai_handler = AIHandler()
    result = ai_handler.generate_sample_prompts(context, num_samples, max_words, assistant_id, followups)
    return jsonify({"message": "Sample prompts generated successfully", "data": result}), 200

@ai_bp.route("/generateFollowups", methods=["POST"])
def generateFollowups():
    data = request.get_json()
    question = data.get('question')
    response = data.get('response')
    num_samples = data.get('num_samples', 1)
    max_words = data.get('max_words', 50)
    assistant_id = data.get('assistant_id')
    ai_handler = AIHandler()
    result = ai_handler.generate_followups(question, response, num_samples, max_words, assistant_id)
    return jsonify({"message": "Follow-ups generated successfully", "data": result}), 200


@ai_bp.route("/textToSpeech", methods=["POST"])
def textToSpeech():
    data = request.get_json()
    text = data.get('text')
    voice = data.get('voice', 'alloy')  # default voice if not provided
    ai_handler = AIHandler()
    result = ai_handler.text_to_speech(text, voice)

    if result:
        return Response(result, mimetype='audio/mpeg', status=200)
    else:
        return jsonify({"message": "Error converting text to speech"}), 500


@ai_bp.route("/speechRecognition", methods=["POST"])
def speechRecognition():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    ai_handler = AIHandler()
    result = ai_handler.speech_recognition(file)
    return jsonify({"message": "Speech recognized successfully", "data": result}), 200