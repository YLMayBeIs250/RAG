import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
       api_key = os.environ.get("ARK_API_KEY"),
       base_url = "https://ark.cn-beijing.volces.com/api/v3",
       model= "ep-20250521230712-zmlbp")

# 1, 可以自己写msg
# msg = [SystemMessage(content="请将一下的内容翻译成日文"),
#        HumanMessage(content="你好啊，我喜欢中国")]

# result = model.invoke(msg)
# print(result)
# print("-" * 40)
#
# parser = StrOutputParser()
# print(parser.invoke(result))
# print("-" * 40)
#
# chain = model | parser
# print(chain.invoke(msg))
# print("-" * 40)

# 2, 也可以自己写提示模板
prompt_template = ChatPromptTemplate.from_messages([
       ('system', '请将以下内容翻译成{language}'),
       ('user', "{text}")])

parser = StrOutputParser()

chain = prompt_template | model | parser

print(chain.invoke({"language": "意大利语", "text": "我最喜欢中国"}))



