import google.generativeai as gemini
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL="gemini-2.0-flash"
query ="대한민국의 통계상 인구수는? "

gemini.configure(api_key=API_KEY)
model = gemini.GenerativeModel(GEMINI_MODEL)

res = model.generate_content(query)
print("질문 : ",query)
print("   >>> ",res.text)