# LangChain 구성요소
## Prompt
## StrOutpuyParser
LangChain의 Runnable 파이프라인은 입력 → LLM → 출력 단계별로 모듈을 교환·조합할 수 있게 설계돼 있습니다. 하지만 LLM이 반환하는 건 AIMessage(역할·콘텐츠·메타데이터가 들어 있는 객체)이고, 다음 단계에서 그저 한 줄 문자열만 필요할 때가 많습니다.

StrOutputParser는 AIMessage → str 로 변환해 줍니다.
즉, "assistant" 부분의 순수 텍스트(AIMessage.content)만 남기고 래퍼 객체를 걷어내는 얇은 어댑터 역할을 합니다.

📌 OutputParser 계열은 “LLM 결과를 어떻게 해석할지”를 담당합니다. StrOutputParser는 그중 가장 단순한 형태입니다—형태소 분석도, JSON 검증도 하지 않고 그대로 문자열만 꺼내 줍니다.
## Memory

# MultiChain 연결하기