# reddit_scraper.py

import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    return reddit

def scrape_user_data(username, limit=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts, comments = [], []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "url": f"https://reddit.com{submission.permalink}"
            })
    except Exception as e:
        print("Error fetching posts:", e)

    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print("Error fetching comments:", e)

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }
