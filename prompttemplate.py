import os
import logging
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# logging.basicConfig(
#     format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)


k8s_assistant_template ="""
You are a Kubernetes expert. You are a chatbot assistant for our Kubernetes infrastructure. You can only answer
questions about Kubernetes. You do not provide information outside of this scope. If a question is not about Kubernetes
infrastructure, or about anything inside the kubernetes cluster, you respond with "I only can answer questions
about Kubernetes."
Question: {question}
Answer: """


k8s_assistant_prompt_template = PromptTemplate(
    input_variables=["question"],
    template=k8s_assistant_template
)

os.environ["AZURE_OPENAI_API_KEY"] = "xxxxxxxxxxxxxxxxxxxx"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://xxxxxxxxxxxxxx.openai.azure.com/"

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="youropenaideployment",
    model_name="gpt-35-turbo",
    model_version="0301",
    temperature=0.5
)

llm_chain = LLMChain(llm=llm, prompt=k8s_assistant_prompt_template)


def query_llm(question):
    print(llm_chain.invoke({'question': question})['text'])


if __name__ == '__main__':
    question = "What is the state of my pod named backendapp?"
    print(llm_chain.invoke({'question': question})['text'])
