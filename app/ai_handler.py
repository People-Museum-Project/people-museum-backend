from app.USFGenAI_OOP import GenAILab

class AIHandler:
    def __init__(self):
        self.assistant = GenAILab()

    def generate_text(self, prompt, model='gpt-3.5-turbo'):
        try:
            self.assistant.set_model(model)
            response = self.assistant.ask_question([], prompt, "You are a helpful assistant.")
            return response['reply']
        except Exception as e:
            return {"error": str(e)}

    def ask_question(self, conversation=None, question=None, instructions=None, assistant_id=None):
        try:
            response = self.assistant.ask_question(conversation, question, instructions, assistant_id)
            return response
        except Exception as e:
            return {"error": str(e)}

    def generate_sample_prompts(self, context, num_samples, max_words, assistant_id=None, followups=None):
        try:
            prompts = self.assistant.generate_sample_prompts(context, num_samples, max_words, assistant_id, followups)
            return prompts
        except Exception as e:
            return {"error": str(e)}

    def generate_followups(self, question, response, num_samples, max_words, assistant_id=None):
        try:
            followups = self.assistant.generate_followups(question, response, num_samples, max_words, assistant_id)
            return followups
        except Exception as e:
            return {"error": str(e)}

    def text_to_speech(self, text, voice=None):
        try:
            content = self.assistant.text_to_speech(text, voice)
            return content
        except Exception as e:
            return {"error": str(e)}

    def speech_recognition(self, file):
        try:
            content = self.assistant.speech_recognition(file)
            return content
        except Exception as e:
            return {"error": str(e)}