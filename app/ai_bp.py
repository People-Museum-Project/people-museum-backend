from flask import Blueprint, request, jsonify
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
    conversation = data.get('conversation', [])
    question = data.get('question')
    instructions = data.get('instructions', "You are a helpful assistant.")
    assistant_id = data.get('assistant_id')
    ai_handler = AIHandler()
    result = ai_handler.ask_question(conversation, question, instructions, assistant_id)
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