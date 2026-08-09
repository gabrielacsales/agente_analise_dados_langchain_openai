# agente_analise_dados_langchain_openai

#### passos

1. Usar um atalho para gravar minha voz
2. Transcrever minha voz para texto (em português) -> Whispper
3. Enviar o texto para o LLM e receber a resposta -> Agente Analise de Dados (LangChain + OpenAI)
4. Converter a resposta do LLM para áudio (em português) -> Modelo de TTS (API OpenAI)

Uso: de classe python, a razão de uso de classe ao inves de funções em módulos: esse program possui estado:
existem várias informações que precisam continuar existinfo e ser compartilhada entre diferentes partes do programa enquanto ele roda.

Estados: está gravando? | áudio atual | modelo Whisper | LLM | agente | fila de respostas
Comportamentos: | iniciar gravação | parar gravação | transcrever | perguntar ao agente | falar resposta

comandos

- para criar o ambiente virtual: `python3 -m venv .venv`
- para instalar as libs das versões requeridas para o projeto `pip install -r requirements.txt`
- para entrar no ambiente virtual onde foram instalada as libs `source .venv/bin/activate`
- para rodar arquivo python: `python arquivo.py`

bibliotecas:
pynput (controla teclado), Global hotkeys -> https://pypi.org/project/pynput/
(arquivo.AV tipo MP3)
