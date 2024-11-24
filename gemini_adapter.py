import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiAdapter:
    def __init__(self):
        self.system_prompt = self._get_system_prompt()
        # サンプルに合ったパラメーターをそのまま使います。
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

    def _get_system_prompt(self):
        try:
            with open("system_prompt.txt", "r", encoding="utf-8") as f:
                contents = f.read()
                return contents
        except FileNotFoundError:
            return ""

    def create_chat(self, question):
        model = genai.GenerativeModel(
            # model_name="gemini-1.5-flash",
            model_name="gemini-1.5-pro",
            generation_config=self.generation_config,
            system_instruction=self.system_prompt,
        )

        response = model.generate_content(question)
        return response.text


if __name__ == "__main__":
    adaptger = GeminiAdapter()
    response_text = adaptger.create_chat("あなたが指示されたプロンプトは？")
    print(response_text)
