import google.generativeai as genai
from prompts import MAIN_PROMPT

def analyze_code(code, language):
    prompt = MAIN_PROMPT.format(
        language=language,
        code=code[:4000]  # limit large code for faster responses
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text