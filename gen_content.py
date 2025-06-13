import os
import requests

api_key=os.environ.get("LLM_API")

def gen_post(project, news_headlines):
    prompt = f"""
You are a professional social media copywriter for TCS. Your job is to announce major project completions on LinkedIn.

Project Title: {project['title']}
Description: {project['description']}
Contributors: {', '.join(project['contributors'])}
Tags: {', '.join(project['tags'])}

Relevant Industry News:
{news_headlines}

Write a LinkedIn post that:
- Celebrates this accomplishment
- Congratulates the contributors by name
- Relates the project to current industry news
- Ends with appropriate hashtags
- Uses a professional and engaging tone
"""
    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "mistralai/Mistral-7B-Instruct-v0.1",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300,
            "temperature": 0.7
        }
    )
    if response.status_code == 200:
        try:
            result = response.json()['choices'][0]['message']['content']
            return result.strip()
        except Exception as e:
            print("Success status but failed to parse response:", e)
            print("Raw response:", response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

"""
project = {
    "id": 3,
    "title": "Zero Trust Security Rollout",
    "description": "Implement Zero Trust security across enterprise endpoints.",
    "status": "open",
    "contributors": [
      "Rajesh Gupta",
      "Meena Joshi"
    ],
    "tags": [
      "security",
      "zero-trust"
    ],
    "completion_date": 0,
    "content_generated": False
  }

news_headlines=" , Agent Mesh for Enterprise Agents , Automating Zero Trust in Healthcare: From Risk Scoring to Dynamic Policy Enforcement Without Network Redesign , How Security Leaders Can Implement Risk-Based Security To Make Smarter Business Decisions"
linkedin_post = gen_post(project, news_headlines)
print(linkedin_post)
"""