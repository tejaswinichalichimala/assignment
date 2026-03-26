import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def get_headers():
    token = os.getenv("HF_TOKEN")

    return {
        "Authorization": f"Bearer {token}" if token else "",
        "Content-Type": "application/json"
    }

def ai_insights(text):
    prompt = f"""
Analyze the logs for:
- sensitive data
- security risks
- anomalies

Logs:
{text[:500]}
"""

    try:
        response = requests.post(
            API_URL,
            headers=get_headers(),
            json={"inputs": prompt},
            timeout=30
        )

        data = response.json()

        if isinstance(data, dict) and "error" in data:
            if "loading" in data["error"].lower():
                return ["Model loading, try again"]
            return [data["error"]]

        result = data[0].get("generated_text", "")
        return result.split("\n")

    except Exception as e:
        return [f"AI error: {str(e)}"]