# Reddit-User-Persona-Generator

**Persona Generator** is an AI-powered tool that analyzes a Reddit user's public activity to build a detailed **user persona** — including their interests, tone of voice, worldview, and behavior patterns — while citing specific posts/comments to justify each trait.

This is powered by **Reddit’s official API (PRAW)** and **OpenAI’s GPT-4** for persona inference.

---

## 🔍 Use Case

This tool can be used for:

- Social media research
- User profiling for community moderation
- AI-generated audience insights
- Psychographic marketing
- Competitive subreddit analysis

---

## 🚀 Key Features

### 🧬 1. Reddit Data Collection (PRAW)
- Fetches the latest **posts** and **comments** from any public Reddit profile.
- Includes URL citations to each post/comment used for analysis.

### 🤖 2. Persona Generation (GPT-4)
- Summarizes Reddit activity into:
  - **Top Interests**
  - **Tone of Communication**
  - **Beliefs / Worldview**
- Uses a structured prompt for consistent and explainable results.
- All insights are backed with **textual evidence and links**.

### 📄 3. Output
- Clean `.txt` file stored in `/output/`
- Automatically named based on Reddit username (e.g., `kojied_persona.txt`)

---

## 🧪 How It Works

1. User enters a Reddit username (e.g., `kojied`)
2. Script pulls 50 latest posts & comments
3. Content is formatted into a prompt for GPT
4. GPT generates a concise persona, citing source posts
5. Output is saved and printed

---

## ⚙️ Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/Sanjaykumar7777/Reddit-User-Persona-Generator.git

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Configure .env

- Create a .env file in the root folder with:

   ```bash
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USERNAME=your_reddit_username
   REDDIT_PASSWORD=your_reddit_password
   REDDIT_USER_AGENT=PersonaGenerator/0.1 by u/your_username
  
   OPENAI_API_KEY=your_openai_api_key

4. Run the App
   ```bash
   python main.py

-Then type the Reddit username when prompted.

---

### 📁 Folder Structure

```

Reddit-User-Persona-Generator/
│
├── main.py                  # Main CLI app
├── reddit_scraper.py        # Reddit data fetching module
├── persona_builder.py       # LLM-powered persona generator
├── output/                  # Stores persona .txt files
├── requirements.txt
└── README.md

```

---

### 💡 Sample Output

User Persona of u/kojied:

Interests:
1. Technology (Vision Pro, iOS Dev)
2. Gaming (Manor Lords)
3. Anime (One Piece)
...

Tone of Voice:
- Analytical and helpful
...

Worldview:
- Curious, open-minded, values knowledge sharing
...

Sources:
- https://reddit.com/r/visionosdev/comments/...
- https://reddit.com/r/ManorLords/comments/...

---

### ⚠️ Challenges Faced

1. API Rate Limiting
Reddit API enforces strict request limits. We optimized by batching and reducing data size.

2. Noise in Comments
Not all Reddit activity is persona-relevant. GPT helps filter signal from noise.

3. OpenAI Prompt Engineering
Designing a prompt that generates a coherent, evidence-backed persona was key. We iterated to balance structure and creativity.

...

---

### 🌱 Future Improvements

✅ Support for bulk usernames or full subreddit scraping

✅ Auto-detect toxic behavior or sentiment drift over time

✅ Output formats: PDF, HTML report, or dashboard

✅ LLM fine-tuning on Reddit-style data for sharper personas

