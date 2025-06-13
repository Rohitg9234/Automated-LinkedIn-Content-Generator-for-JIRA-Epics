import os
import requests

api_key=os.environ.get("LLM_API")

def fix_post(last_generated_post, feedback):

    prompt = f"""
    You are a professional social media copywriter for TCS. Your job is to announce major project completions on LinkedIn.

    Below is the last generated LinkedIn post draft:

    ---
    {last_generated_post}
    ---

    The reviewer provided the following feedback:
    "{feedback}"

    Your task:
    - Revise the LinkedIn post above to address the reviewer’s feedback and incorporate any additional relevant information provided.
    - Keep the positive, professional, and engaging tone.
    - Preserve what works well in the original draft, but make improvements as per the feedback.
    - Ensure the post celebrates the accomplishment, congratulates contributors, connects to industry news, and ends with appropriate hashtags.
    - Output only the improved LinkedIn post.
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
