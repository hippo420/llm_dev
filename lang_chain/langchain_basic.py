from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

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

#시스템 메시지와 사용자 메시지를 포함한 메시지 리스트를 생성
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "LLM은 어떤 원리로 작동하나요? 100자 이내로 설명해주세요."},
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)