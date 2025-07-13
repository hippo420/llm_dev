from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

#PromptTemplate와 체인
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL="gemini-2.0-flash"

#ChatGoogleGenerativeAI 모델 초기화
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=0,         #결적론적 출력 설정
    max_output_tokens=200, #응답길이 제한
    google_api_key=API_KEY
)

# 4) 문자열 출력 파서
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 증권사 직원이야."),
    ("human", "{text}")
])

explain_chain = prompt | llm | parser

result = explain_chain.invoke({
    "text": "삼성전자 주가알려줘"
})
#결과값에서 content만 추출하기 때문에 result.content불필요
#print(result.content)
print(result)