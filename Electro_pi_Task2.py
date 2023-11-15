import streamlit as st
import openai
import requests
import black
import spacy

# Load spaCy model for named entity recognition
nlp = spacy.load("en_core_web_lg")

# Set your OpenAI GPT-3 API key
openai.api_key = "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"
UNSPLASH_ACCESS_KEY = "eN4u15zCIln3IkJv91HW6sEkkjkuxi1jplNkrVsGoJ8"

def generate_text(prompt):
    # Use OpenAI GPT-3 to generate text based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,  # Increase the maximum number of tokens to get more content
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_image(description):
    # Use Unsplash API to get a relevant image based on the description
    response = requests.get(
        f"https://api.unsplash.com/photos/random?query={description}&client_id={UNSPLASH_ACCESS_KEY}"
    )
    data = response.json()
    return data["urls"]["regular"] if data else None

def formate_code(code):
    return code

def main():
    st.title("Text and Image Generator")

    # Input for the user's prompt
    user_input = st.text_area("Enter your prompt for text generation:")

    if st.button("Generate"):
        # Generate text based on the user's input
        generated_text = generate_text(user_input)

        # Format the generated code
        formatted_code = formate_code(generated_text)

        # Display the generated text
        st.subheader("Generated Text:")
        st.code(formatted_code, language='python')

        # Generate an image based on the entire generated text
        st.subheader("Image for the Entire Text")
        generated_image = generate_image(generated_text)

        # Display the generated image
        st.image(generated_image, caption="Image for the Entire Text", use_column_width=True)

if __name__ == "__main__":
    main()

