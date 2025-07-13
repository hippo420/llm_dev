from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
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

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 {input_language} 문장을 {output_language}(으)로 번역하는 도우미입니다."),
    ("human", "{text}")
])
chain = prompt | llm

result = chain.invoke({
    "input_language": "한국어",
    "output_language": "영어",
    "text": "파이썬이 좋아요!"
})
print(result.content)