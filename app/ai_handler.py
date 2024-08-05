from app.USFGenAI_OOP import GenAILab

class AIHandler:
    def __init__(self):
        # Initialize the AIHandler instance with an instance of GenAILab.
        self.assistant = GenAILab()

    def generate_text(self, prompt, model='gpt-3.5-turbo'):
        """
        Generates a response based on the provided prompt using a specified model.

        Args:
            prompt (str): The prompt text to generate a response for.
            model (str): The model to use for generating the response (default is 'gpt-3.5-turbo').

        Returns:
            str: The generated response text or an error message if an exception occurs.
        """
        try:
            self.assistant.set_model(model)
            response = self.assistant.ask_question([], prompt, "You are a helpful assistant.")
            return response['reply']
        except Exception as e:
            return {"error": str(e)}

    def ask_question(self, conversation=None, question=None, instructions=None, assistant_id=None):
        """
        Asks a question and retrieves a response from the AI assistant.

        Args:
            conversation (list, optional): The conversation history (default is None).
            question (str, optional): The question to ask the AI (default is None).
            instructions (str, optional): Instructions for the AI (default is None).
            assistant_id (str, optional): Identifier for the specific assistant (default is None).

        Returns:
            dict: The response from the AI assistant or an error message if an exception occurs.
        """
        try:
            response = self.assistant.ask_question(conversation, question, instructions, assistant_id)
            return response
        except Exception as e:
            return {"error": str(e)}

    def generate_sample_prompts(self, context, num_samples, max_words, assistant_id=None, followups=None):
        """
        Generates a set of sample prompts based on the provided context.

        Args:
            context (str): The context for generating prompts.
            num_samples (int): The number of sample prompts to generate.
            max_words (int): The maximum number of words for each prompt.
            assistant_id (str, optional): Identifier for the specific assistant (default is None).
            followups (list, optional): A list of follow-up prompts (default is None).

        Returns:
            list: A list of generated sample prompts or an error message if an exception occurs.
        """
        try:
            prompts = self.assistant.generate_sample_prompts(context, num_samples, max_words, assistant_id, followups)
            return prompts
        except Exception as e:
            return {"error": str(e)}

    def generate_followups(self, question, response, num_samples, max_words, assistant_id=None):
        """
        Generates follow-up questions based on the provided question and response.

        Args:
            question (str): The initial question.
            response (str): The response to the initial question.
            num_samples (int): The number of follow-up questions to generate.
            max_words (int): The maximum number of words for each follow-up question.
            assistant_id (str, optional): Identifier for the specific assistant (default is None).

        Returns:
            list: A list of generated follow-up questions or an error message if an exception occurs.
        """
        try:
            followups = self.assistant.generate_followups(question, response, num_samples, max_words, assistant_id)
            return followups
        except Exception as e:
            return {"error": str(e)}

    def text_to_speech(self, text, voice=None):
        """
        Converts the provided text to speech using a specified voice.

        Args:
            text (str): The text to convert to speech.
            voice (str, optional): The voice to use for the speech conversion (default is None).

        Returns:
            bytes: The audio content of the speech or an error message if an exception occurs.
        """
        try:
            content = self.assistant.text_to_speech(text, voice)
            return content
        except Exception as e:
            return {"error": str(e)}

    def speech_recognition(self, file):
        """
        Converts speech from the provided audio file to text.

        Args:
            file (str): Path to the audio file for speech recognition.

        Returns:
            str: The transcribed text from the audio file or an error message if an exception occurs.
        """
        try:
            content = self.assistant.speech_recognition(file)
            return content
        except Exception as e:
            return {"error": str(e)}
