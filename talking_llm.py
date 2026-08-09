# 1. Usar um atalho para gravar minha voz
# 2. Transcrever minha voz para texto (em português) -> Whispper
# 3. Enviar o texto para o LLM e receber a resposta -> Agente Analise de Dados (LangChain + OpenAI)
# 4. Converter a resposta do LLM para áudio (em português) -> Modelo de TTS (API OpenAI)

from dotenv import load_dotenv, find_dotenv # find para encontrar o arquivo .env mesmo que esteja em outro diretório
from openai import OpenAI # antes era: import openai

load_dotenv(find_dotenv())

client = OpenAI() # antes era: openai.Client()

class TalkingLLM():
    # configurar atributos ou dependencias logo na criação do objeto
    # tipo estado/ configuração inicial
    def __init__(self):
        pass

    # Atalho p/ gravar audio
    def start_or_stop_recording(self):
        pass

    # criar o agente de analise de dados
    def create_agent(self):
        pass

    # Salva e Transcrever audio para texto
    def save_and_transcribe_audio(self):
        pass
    
    # Pega o texto do agente para audio
    def convert_and_play(self):
        pass
    
    # Roda tudo
    def run(self):
        pass

if __name__ == "__main__":
    talking_llm = TalkingLLM()
    talking_llm.run()