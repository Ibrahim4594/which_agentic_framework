import json
import requests

def load_config(path: str):
    """Load configuration from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def save_log(action: str, prompt: str, response: str):
    """Save log messages to a specified log file."""
    with open("agent.log", "a") as f:
        f.write(f"{action.upper()} | PROMPT: {prompt} | RESPONSE: {response}\n")

def format_response(response: str) -> str:
    """Format the response for better readability."""
    return response.strip()

def search_web(query: str) -> str:
    """Search the web using DuckDuckGo API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("AbstractText") or "No summary found."
        else:
            return "Web search failed."
    except Exception as e:
        return f"Web search error: {e}"