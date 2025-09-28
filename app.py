from flask import Flask, render_template, request
import requests
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

def fetch_top_sources(query):
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    body = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "include_answer": False,
        "include_raw_content": False,
        "max_results": 3
    }

    res = requests.post(url, headers=headers, json=body)
    data = res.json()
    return data.get("results", [])

def check_with_groq(news_input, sources):
    context = "\n\n".join([f"{s['title']}: {s.get('content', '') or s['url']}" for s in sources])
    prompt = f"""
You are a fact-checking assistant.

Given the following claim:
\"{news_input}\"

And these trusted sources:
{context}

Determine:
1. Is the news Real or Fake?
2. Provide a short reason.
3. Show the top 3 sources.

Respond in the following JSON format:
{{
  "verdict": "Real" or "Fake",
  "reason": "short reason",
  "top_sources": ["source1", "source2", "source3"]
}}
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # Updated to the latest production model
        "messages": [
            {"role": "system", "content": "You are a truthful AI that checks news authenticity using sources."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 32768  # Using the maximum allowed tokens for this model
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        reply = response.json()

        # Debug print
        print("Groq raw reply:", reply)

        # Handle error response
        if "error" in reply:
            print("Groq API Error:", reply["error"]["message"])
            return {
                "verdict": "Unknown",
                "reason": f"Groq API Error: {reply['error']['message']}",
                "top_sources": []
            }

        # Handle correct reply
        content = reply['choices'][0]['message']['content']
        json_match = re.search(r"\{.*\}", content, re.DOTALL)
        if json_match:
            json_string = json_match.group()
            parsed = json.loads(json_string)
            parsed["trust_score"] = 100 if parsed.get("verdict") == "Real" else 85
            return parsed
        else:
            raise ValueError("No valid JSON in LLM response")

    except Exception as e:
        print("Exception in Groq call:", str(e))
        return {
            "verdict": "Unknown",
            "reason": "Could not analyze properly.",
            "top_sources": []
        }

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize result with default values for GET requests
    result = {
        "input": "",
        "verdict": "Unknown",
        "reason": "Enter news text to check its authenticity",
        "sources": [],
        "trust_score": 70
    }

    if request.method == "POST":
        user_input = request.form["news"]

        sources = fetch_top_sources(user_input)
        verdict_info = check_with_groq(user_input, sources)

        # Map actual Tavily URLs using top source titles
        top_titles = verdict_info.get("top_sources", [])
        matched_sources = []
        for title in top_titles:
            for src in sources:
                if title.lower() in src["title"].lower():
                    matched_sources.append({"title": src["title"], "url": src["url"]})
                    break

        result = {
            "input": user_input,
            "verdict": verdict_info.get("verdict", "Unknown"),
            "reason": verdict_info.get("reason", "No reason provided."),
            "sources": matched_sources,
            "trust_score": verdict_info.get("trust_score", 70)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)