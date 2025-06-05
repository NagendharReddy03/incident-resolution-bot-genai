import openai
import yaml

# Load API key from config
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)
    openai.api_key = config.get("OPENAI_API_KEY")

def analyze_logs(log_text: str) -> str:
    """Use OpenAI to analyze log text and suggest resolutions."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful IT support assistant."},
                {"role": "user", "content": f"Analyze the following log and suggest a fix:\n{log_text}"}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error during analysis: {e}"

