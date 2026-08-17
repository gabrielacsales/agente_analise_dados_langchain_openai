## código criad para teste antes de criar o método que cria o agente nó código principal


from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd

from langchain_classic.agents.agent_types import AgentType

from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("df_rent.csv")

agent = create_pandas_dataframe_agent(
  ChatOpenAI(model="gpt-4.1-mini"),
  df,
  verbose=True,
  agent_type=AgentType.OPENAI_FUNCTIONS,
  allow_dangerous_code=True,
)

agent.invoke("Quero saber o Preço médio de imóveis novos vs usados")