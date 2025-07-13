from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# ── 0. 환경 변수 ───────────────
load_dotenv()
API_KEY   = os.getenv("GEMINI_API_KEY")          # .env:  GEMINI_API_KEY=AIza...
LLM_MODEL = "gemini-2.0-flash"                   # 계정에 맞는 모델 확인

# ── 1. LLM 초기화 ──────────────
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=0,
    max_output_tokens=200,
    google_api_key=API_KEY
)

# ── 2. 간단 retriever (샘플) ────
def fake_retriever(query: str) -> list[str]:
    # 실제 프로젝트에선 벡터스토어 retriever나 DB 호출
    return [f"문서 스니펫1 about '{query}'", f"문서 스니펫2 about '{query}'"]

# ── 3. 프롬프트 + LLM + 파서 ───
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "아래 context를 참고해 질문에 답하세요."),
    ("human",  "Context: {context}\n\nQuestion: {question}")
])
answer_chain = qa_prompt | llm | StrOutputParser()

# ── 4. 전체 파이프라인 ──────────
pipeline = (
        RunnableLambda(                             # 입력 dict → context‧question 생성
            lambda d: {
                "context": fake_retriever(d["question"]),
                "question": d["question"]
            }
        )
        | answer_chain                              # LLM 호출
)

# ── 5. 실행 ─────────────────────
print(pipeline.invoke({"question": "Gemini는 언제 출시됐어?"}))
