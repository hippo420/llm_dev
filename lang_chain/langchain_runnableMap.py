# pip install -U langchain-google-genai langchain-core
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap
from langchain_core.runnables import RunnableLambda
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

summ_prompt = ChatPromptTemplate.from_messages([
    ("system", "아래 내용을 한 문장으로 요약하세요."),
    ("human", "{text}")
])
summ_chain = summ_prompt | llm | StrOutputParser()

# RunnableMap으로 “리스트 각 요소에 summ_chain 적용” -----------------
batch_summarizer = summ_chain.map()  # 올바른 방식

# 테스트 -------------------------------------------------------------
articles = [
    "오픈AI가 새로운 GPT‑4o 모델을 발표했습니다. 성능이...",
    "삼성전자가 차세대 3나노 공정을 올해 하반기 본격 도입...",
    "테슬라가 보급형 모델을 2026년 출시한다고 밝혔습니다..."
]

summaries = batch_summarizer.invoke(articles)
for idx, s in enumerate(summaries, 1):
    print(f"{idx}. {s}")
