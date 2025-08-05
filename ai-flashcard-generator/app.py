import streamlit as st
from rake_nltk import Rake
import nltk
import re

# Download stopwords if not already
nltk.download('stopwords')

def clean_text(text):
    """Clean text by removing extra spaces, special characters etc."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def extract_keywords(text, max_keywords=10):
    """Extract top keywords using RAKE"""
    rake = Rake()
    rake.extract_keywords_from_text(text)
    ranked = rake.get_ranked_phrases()
    return ranked[:max_keywords]

def main():
    st.title("📚 AI Flashcard Generator")
    st.write("Generate flashcard topics by uploading a text file or pasting your text.")

    # Text input
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    user_text = st.text_area("Or paste your text here:")

    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
    elif user_text.strip() != "":
        content = user_text
    else:
        content = None

    if content:
        cleaned = clean_text(content)
        keywords = extract_keywords(cleaned, max_keywords=10)

        st.subheader("✨ Generated Flashcard Topics:")
        for i, kw in enumerate(keywords, 1):
            st.write(f"**{i}.** {kw}")
    else:
        st.info("Please upload a text file or paste some text to generate flashcards.")

if __name__ == "__main__":
    main()

