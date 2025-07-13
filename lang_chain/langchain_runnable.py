from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
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

# 1) 번역용 프롬프트 체인 -----------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following text to English."),
    ("human", "{text}")
])

translate_chain = prompt | llm | StrOutputParser()

# 2) Parallel 구성 ----------------------------------------
multi_chain = RunnableParallel(
    original = RunnablePassthrough(),   # 그대로 통과
    english  = translate_chain          # 번역
)

print(multi_chain.invoke("파이썬이 좋아요!"))
# → {'original': '파이썬이 좋아요!', 'english': 'I love Python!'}
