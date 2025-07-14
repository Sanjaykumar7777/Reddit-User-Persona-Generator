# persona_builder.py (OpenAI SDK v1.0+ compatible)

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_user_persona(username, posts, comments):
    content = f"Reddit profile of u/{username}\n\n"

    if posts:
        content += "\nRecent Posts:\n"
        for post in posts[:20]:
            content += f"- Title: {post['title']}\n  Content: {post['selftext'][:500]}\n  URL: {post['url']}\n\n"

    if comments:
        content += "\nRecent Comments:\n"
        for comment in comments[:30]:
            content += f"- Comment: {comment['body'][:500]}\n  URL: {comment['url']}\n\n"

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if needed
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a persona analyst. Given Reddit posts and comments, your job is to generate a concise "
                    "user persona, including interests, tone of voice, worldview, and cite example post/comment URLs "
                    "used for each insight. Output in clean readable text format."
                )
            },
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=0.7,
        max_tokens=1200
    )

    return response.choices[0].message.content
