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
- para entrar no ambiente virtual onde foram instalada as libs `source .venv/Scripts/activate`
- para rodar arquivo python: `python arquivo.py`

bibliotecas:
- pynput (controla teclado), Global hotkeys -> https://pypi.org/project/pynput/
- sounddevice (captura o audio)
- wave (salva no formato que precisamos de audio)
- whisper (transcreve o audio para texto)
obs: precisei instalar com:
`pip install -U openai-whisper`
`winget install ffmpeg`
`export PATH="$PATH:"` + caminho que winget instalou o ffmpeg
`find "$LOCALAPPDATA/Microsoft/WinGet/Packages" -iname "ffmpeg.exe" 2>/dev/null`
- langchain (opção de chat do modelo)
- queue (lista respostas da IA)
- io (para gerar o arquivo temporario audio buffers)
- soundfile (reproduzir o audio)
- threading (thread que roda a função convert and play em paralelo)

## Perguntas que você pode fazer Para o agente:
Mais simples:
- sobre o que são esses dados?
- quantas linhas há no conjunto de dados?

### Análises:
Com base no dataframe apresentado, que parece tratar de imóveis (aparentemente apartamentos) para locação ou venda com diversas características, podemos propor várias análises úteis para entender melhor o mercado, comportamento dos preços, oferta e demanda, entre outros aspectos. Aqui estão algumas possibilidades:

**1. Análise Descritiva dos Dados**
- Estatísticas básicas: média, mediana, desvio padrão, mínimo e máximo das variáveis numéricas como preço, tamanho, número de quartos, banheiros, vagas, etc.
- Distribuição dos tipos de propriedades (ex: quantos apartamentos, casas, etc.)
- Frequência das condições (ex: quantos imóveis são novos, quantos possuem piscina, elevador etc.)  

**2. Análise de Preços**
- Distribuição dos preços (em função do tipo de negociação: aluguel ou venda)
- Preço médio por distrito
- Preço por metro quadrado (Price/Size)
- Como as características influenciam o preço? Ex: imóveis com piscina, elevador, mobiliados, etc., tendem a ser mais caros?

**3. Análise Geográfica**
- Visualizar a localização dos imóveis usando Latitude e Longitude
- Preço médio por região ou distrito
- Identificar regiões mais caras ou mais baratas  

**4. Correlações**
- Correlação entre o preço e variáveis como tamanho, número de quartos, vagas, etc.
- Existe correlação entre ter piscina e o preço? Ou entre ser novo e o preço?

**5. Análise de Oferta**
- Quantidade de imóveis por distrito
- Quantidade de imóveis por tipo de negociação (venda, aluguel)
- Quais bairros têm mais imóveis novos? Quantos são mobiliados?

**6. Análises específicas:**
- Preço médio de imóveis novos vs usados
- Impacto do número de suítes no preço
- Comparar imóveis com e sem elevador (útil para regiões com prédios altos)

**7. Modelagem Preditiva**
- Criar um modelo para prever o preço do imóvel com base nas características (tamanho, quartos, localização, piscina, etc.)