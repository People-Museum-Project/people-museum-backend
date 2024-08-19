import io

from openai import OpenAI
from app.secret_manager import GCPSecretManager
from settings import OPENAI_API_KEY

DEFAULT_MODEL = "gpt-3.5-turbo"


class AIComponent:
    _client_initialized = False

    def __init__(self):
        self._api_key = GCPSecretManager().access(OPENAI_API_KEY)
        if not self._api_key:
            raise Exception("Error: The API key is not set. Set the environment variable 'OPENAI_API_KEY'.")
        self._settings = {"model": DEFAULT_MODEL}

    def _initialize_client(self):
        if not self._client_initialized:
            self._client = OpenAI(api_key=self._api_key)
            self._client_initialized = True

    def set_model(self, model_name):
        self._settings['model'] = model_name


class AssistantManager(AIComponent):
    def create_assistant(self, name, instruction):
        self._initialize_client()
        assistant = self._client.beta.assistants.create(
            name=name,
            instructions=f"You are {name}, {instruction}, you answer questions in {name}'s tone.",
            description=f"{name}'s assistant",
            model=self._settings["model"]
        )
        return assistant

    def ask_assistant(self, question, assistant_id):
        self._initialize_client()
        thread = self._client.beta.threads.create()
        self._client.beta.threads.messages.create(thread_id=thread.id, role="user", content=question)
        run = self._client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id)

        if run.status == 'completed':
            messages = self._client.beta.threads.messages.list(thread_id=thread.id)
            latest_message = next((m.content[0].text.value for m in messages.data if m.role == "assistant"), None)
            return latest_message
        return None

    def generate_assistant_prompts(self, context, instructions, assistant_id):
        self._initialize_client()
        thread = self._client.beta.threads.create()
        self._client.beta.threads.messages.create(thread_id=thread.id, role="user", content=context)
        run = self._client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id, instructions=instructions)

        if run.status == 'completed':
            messages = self._client.beta.threads.messages.list(thread_id=thread.id)
            prompts = [m.content[0].text.value for m in messages.data if m.role == "assistant"]
            return prompts[0].split('\n') if prompts else []
        return []

    def ask_assistant_gender(self, assistant_id):
        question = "What is your gender? Please respond with only `1` if you are male and `0` if you are not. Reply only `0` or `1`, Do not include any additional words or explanations."
        return self.ask_assistant(question, assistant_id)


class PromptGenerator(AIComponent):
    def generate_sample_prompts(self, context, num_samples, max_words, followups=False):
        self._initialize_client()
        instructions = f"Generate {num_samples} {'follow-up questions' if followups else 'sample prompts'} from the user perspective. Each should be no more than {max_words} words."
        response = self._client.chat.completions.create(
            model=self._settings["model"],
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": context}
            ]
        )
        return response.choices[0].message.content.strip().split('\n')


class ConversationManager(AIComponent):
    def ask_question(self, conversation, question, instructions=None):
        self._initialize_client()
        messages = [{"role": "system", "content": instructions}] + conversation if instructions else conversation
        messages.append({"role": "user", "content": question})

        response = self._client.chat.completions.create(
            model=self._settings["model"],
            messages=messages
        )
        answer = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": answer})
        return {"reply": answer, "conversation": conversation}


class SpeechManager(AIComponent):
    def text_to_speech(self, text, voice="onyx"):
        self._initialize_client()
        try:
            response = self._client.audio.speech.create(model="tts-1", voice=voice, input=text)
            return response.content
        except Exception as e:
            print(f"Error converting text to speech: {e}")
            return None

    def speech_recognition(self, audio_io):
        self._initialize_client()
        try:
            audio_data = audio_io.read()
            audio_file = io.BytesIO(audio_data)
            translation = self._client.audio.translations.create(model="whisper-1", file=audio_file)
            return translation.text
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return None


class GenAILab:
    def __init__(self):
        self._assistant_manager = None
        self._prompt_generator = None
        self._conversation_manager = None
        self._speech_manager = None

    def _get_assistant_manager(self):
        if self._assistant_manager is None:
            self._assistant_manager = AssistantManager()
        return self._assistant_manager

    def _get_prompt_generator(self):
        if self._prompt_generator is None:
            self._prompt_generator = PromptGenerator()
        return self._prompt_generator

    def _get_conversation_manager(self):
        if self._conversation_manager is None:
            self._conversation_manager = ConversationManager()
        return self._conversation_manager

    def _get_speech_manager(self):
        if self._speech_manager is None:
            self._speech_manager = SpeechManager()
        return self._speech_manager

    def set_model(self, model_name):
        self._get_assistant_manager().set_model(model_name)
        self._get_prompt_generator().set_model(model_name)
        self._get_conversation_manager().set_model(model_name)
        self._get_speech_manager().set_model(model_name)

    def create_assistant(self, name, instruction):
        return self._get_assistant_manager().create_assistant(name, instruction)

    def ask_question(self, conversation, question, instructions=None):
        return self._get_conversation_manager().ask_question(conversation, question, instructions)

    def generate_sample_prompts(self, context, num_samples, max_words, followups=False):
        return self._get_prompt_generator().generate_sample_prompts(context, num_samples, max_words, followups)

    def ask_assistant(self, question, assistant_id):
        return self._get_assistant_manager().ask_assistant(question, assistant_id)

    def generate_assistant_prompts(self, context, instructions, assistant_id):
        return self._get_assistant_manager().generate_assistant_prompts(context, instructions, assistant_id)

    def ask_assistant_gender(self, assistant_id):
        return self._get_assistant_manager().ask_assistant_gender(assistant_id)

    def text_to_speech(self, text, voice=None):
        return self._get_speech_manager().text_to_speech(text, voice)

    def speech_recognition(self, audio_io):
        return self._get_speech_manager().speech_recognition(audio_io)
