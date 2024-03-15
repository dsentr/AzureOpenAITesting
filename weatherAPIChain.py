import os
import logging
from langchain.chains import LLMChain, APIChain
from langchain.chains.api import open_meteo_docs
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate


os.environ["AZURE_OPENAI_API_KEY"] = "xxxxxxxxxxxxxxxxxxxx"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://xxxxxxxxxxxx.openai.azure.com/"

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="yourdeploymentnamehere",
    model_name="gpt-35-turbo",
    model_version="0301",
    temperature=0.5,
    max_tokens=2000
)


chain = APIChain.from_llm_and_api_docs(
    llm=llm,
    api_docs=open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"],
)

response = chain.invoke(
    input=[HumanMessage(content="What is the weather like right now in Chiacgo, Illinois, USA in degrees Fahrenheit?")]
)

print(response)
