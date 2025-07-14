# main.py

import os
from reddit_scraper import scrape_user_data
from persona_builder import build_user_persona

def main():
    print("🧠 Reddit Persona Generator")
    username = input("Enter the Reddit username (e.g., kojied): ").strip()

    if not username:
        print("❌ No username entered. Exiting.")
        return

    print(f"🔍 Fetching Reddit data for user: u/{username}")

    data = scrape_user_data(username)
    print(f"✅ Retrieved {len(data['posts'])} posts and {len(data['comments'])} comments")

    print("🤖 Generating persona")
    persona = build_user_persona(username, data["posts"], data["comments"])

    output_path = f"output/{username}_persona.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona saved to: {output_path}")

if __name__ == "__main__":
    main()
