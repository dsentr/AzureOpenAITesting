import os
import logging
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

# logging.basicConfig(
#     format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

os.environ["AZURE_OPENAI_API_KEY"] = "xxxxxxxxxxxxxxxxxxxx"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://xxxxxxxxxxxxxxx.openai.azure.com/"

model = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="xxxxxopenaideploymentname",
    model_name="gpt-35-turbo",
    model_version="0301"
)

res = model([HumanMessage(content="What does USA stand for?")])
print(res)
