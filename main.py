import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


dotenv.load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

result = chat.invoke(
    [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="What is the purpose of model regularization?"),
]
)
print(result.content)