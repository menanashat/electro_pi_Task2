
import streamlit as st
import openai
import requests
import spacy


# Set your OpenAI GPT-3 API key
openai.api_key = "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"

def generate_text(prompt, num_sections=7):
        # Define the chat messages with user prompt and system message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate an Blog blog post {num_sections} sections on the topic of: {prompt}"}
    ]

    # Add user messages for each section
    for section_number in range(1, num_sections + 1):
        user_message = {"role": "user", "content": f"Section {section_number}:"}
        messages.append(user_message)

        # Add assistant message (initially empty for the model to generate)
        assistant_message = {"role": "assistant", "content": ""}
        messages.append(assistant_message)

    # Define the parameters for the chat completion
    params = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    # Make the API call
    response = openai.ChatCompletion.create(**params)

    # Extract and return the generated article
    return response['choices'][0]['message']['content']

def generate_image(description):

    url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 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'
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
        try :

            # Generate an image based on the entire generated text
            st.subheader("Image for the Entire Text")
            generated_image = generate_image(user_input)

            # Display the generated image
            st.image(generated_image, caption="Image for the Entire Text", use_column_width=True)

            # Generate text based on the user's input
            generated_text = generate_text(user_input)

            # Format the generated code
            formatted_code = formate_code(generated_text)

            # Display the generated text
            st.subheader("Generated Text:")
            st.write(formatted_code)
        except Excwption as a:
            st.error(f"An error occurred: {a}")


if __name__ == "__main__":
    main()





