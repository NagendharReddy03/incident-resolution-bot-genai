import openai
import os
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to analyze logs with OpenAI
def analyze_logs(log_text: str) -> str:
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful incident analysis assistant."},
                {"role": "user", "content": f"Analyze this log and provide insights: {log_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during analysis: {str(e)}"

# Function to match logs with context like JD or support tickets
def match_with_context(log_text: str, jd_text: str) -> str:
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Match this log with the following context:\nLog: {log_text}\nContext: {jd_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during JD matching: {str(e)}"