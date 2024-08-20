import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Claude API settings
API_URL = "https://api.anthropic.com/v1/chat/completions"
API_KEY = os.getenv("CLAUDE_API_KEY")

def generate_safety_talk(topic, language="english"):
    if not API_KEY:
        st.error("Claude API key is not set. Please set the CLAUDE_API_KEY environment variable.")
        return None

    language_prompts = {
        "english": f"Generate a safety talk about {topic} in English. The talk should be informative, engaging, and approximately 300 words long.",
        "spanish": f"Genera una charla de seguridad sobre {topic} en español. La charla debe ser informativa, atractiva y de aproximadamente 300 palabras.",
        "french": f"Générez une discussion sur la sécurité concernant {topic} en français. La discussion doit être informative, engageante et d'environ 300 mots."
    }

    prompt = language_prompts.get(language.lower(), language_prompts["english"])

    try:
        response = requests.post(
            API_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "messages": [{"role": "user", "content": prompt}],
                "model": "claude-2.0",
                "max_tokens": 500
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.RequestException as e:
        st.error(f"Error generating safety talk: {str(e)}")
        return None

def main():
    st.title("Safety Talks Generator")

    # User input
    topic = st.text_input("Enter a safety topic:")
    language = st.selectbox("Select language:", ["English", "Spanish", "French"])

    if st.button("Generate Safety Talk"):
        if topic:
            with st.spinner("Generating safety talk..."):
                safety_talk = generate_safety_talk(topic, language.lower())
            if safety_talk:
                st.subheader("Generated Safety Talk:")
                st.write(safety_talk)
                st.download_button(
                    label="Download Safety Talk",
                    data=safety_talk,
                    file_name="safety_talk.txt",
                    mime="text/plain"
                )
        else:
            st.warning("Please enter a safety topic.")

if __name__ == "__main__":
    main()
