from flask import Blueprint, request, jsonify, Response
from app.ai_handler import AIHandler

ai_bp = Blueprint('ai_bp', __name__)

@ai_bp.route("/generateText", methods=["POST"])
def generateText():
    """
    Generates text based on a given prompt using the specified model.

    Request JSON:
        - prompt (str): The text prompt for text generation.
        - model (str, optional): The AI model to use (default: 'gpt-3.5-turbo').

    Returns:
        - JSON response with a success message and generated text.
    """
    data = request.get_json()
    prompt = data.get('prompt')
    model = data.get('model', 'gpt-3.5-turbo')  # default model if not provided
    ai_handler = AIHandler()
    result = ai_handler.generate_text(prompt, model)
    return jsonify({"message": "Text generated successfully", "data": result}), 200

@ai_bp.route("/askQuestion", methods=["POST"])
def askQuestion():
    """
    Asks a question to an AI assistant and retrieves the response.

    Request JSON:
        - question (str): The question to ask.
        - assistantId (str): ID of the AI assistant to use.

    Returns:
        - JSON response with a success message and the answer to the question.
    """
    data = request.get_json()
    question = data.get('question')
    assistant_id = data.get('assistantId')
    ai_handler = AIHandler()
    result = ai_handler.ask_question(question=question, assistant_id=assistant_id)
    return jsonify({"message": "Question answered successfully", "data": result}), 200

@ai_bp.route("/generateSamplePrompts", methods=["POST"])
def generateSamplePrompts():
    """
    Generates sample prompts based on a given context and settings.

    Request JSON:
        - context (str): Context for generating prompts.
        - num_samples (int, optional): Number of sample prompts to generate (default: 1).
        - max_words (int, optional): Maximum number of words per prompt (default: 50).
        - assistant_id (str): ID of the AI assistant to use.
        - followups (bool, optional): Whether to include follow-up prompts (default: False).

    Returns:
        - JSON response with a success message and generated sample prompts.
    """
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
    """
    Generates follow-up questions based on a given question and response.

    Request JSON:
        - question (str): The initial question.
        - response (str): The response to the question.
        - num_samples (int, optional): Number of follow-up questions to generate (default: 1).
        - max_words (int, optional): Maximum number of words per follow-up question (default: 50).
        - assistant_id (str): ID of the AI assistant to use.

    Returns:
        - JSON response with a success message and generated follow-up questions.
    """
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
    """
    Converts text to speech and returns the audio file.

    Request JSON:
        - text (str): The text to convert to speech.
        - voice (str, optional): The voice to use for speech synthesis (default: 'onyx').

    Returns:
        - Audio file in MP3 format if conversion is successful.
        - JSON response with an error message if conversion fails.
    """
    data = request.get_json()
    text = data.get('text')
    voice = data.get('voice', 'onyx')  # default voice if not provided
    ai_handler = AIHandler()
    result = ai_handler.text_to_speech(text, voice)

    if result:
        return Response(result, mimetype='audio/mpeg', status=200)
    else:
        return jsonify({"message": "Error converting text to speech"}), 500

@ai_bp.route("/speechRecognition", methods=["POST"])
def speechRecognition():
    """
    Recognizes speech from an uploaded audio file and returns the transcribed text.

    Request:
        - file (File): The audio file to transcribe.

    Returns:
        - JSON response with a success message and transcribed text.
        - JSON response with an error message if no file is provided or file is empty.
    """
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    ai_handler = AIHandler()
    result = ai_handler.speech_recognition(file)
    return jsonify({"message": "Speech recognized successfully", "data": result}), 200
