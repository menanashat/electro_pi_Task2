import streamlit as st
import openai
import requests
import black
import spacy

# Load spaCy model for named entity recognition
nlp = spacy.load("en_core_web_lg")

# Set your OpenAI GPT-3 API key
openai.api_key = "Your_API_KEY"


def generate_text(prompt):
    # Use OpenAI GPT-3 to generate text based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,  # Increase the maximum number of tokens to get more content
        n=1,    
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_image(description):

    url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Your_API_KEY}'
    }

    data = {
        'model': 'dall-e-3',
        'prompt': description,
        'n': 1,
        'size': '1024x1024'
    }

    response = requests.post(url, json=data, headers=headers)



    # Extract the URL from the response
    return response.json()['data'][0]['url']

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
        generated_image = generate_image(user_input)

        # Display the generated image
        st.image(generated_image, caption="Image for the Entire Text", use_column_width=True)

if __name__ == "__main__":
    main()

