# # import streamlit as st
# import transformers
# from transformers import pipeline
# from transformers import AutoModelForSeq2SeqLM
# from transformers import AutoTokenizer
# # import dalle2
# generator = pipeline('text-generation', model = 'gpt2')
# asd=generator("Hello, I'm a language model", max_length =330, num_return_sequences=1)
# print(asd[0]["generated_text"])
# # Initialize text generation model
# tokenizer = AutoTokenizer.from_pretrained("gptj-6b")
# model = AutoModelForSeq2SeqLM.from_pretrained("gptj-6b")

# # Initialize image generation model
# dalle = dalle2.Dalle2()

# def generate_text(topic):
#     # Generate text based on the input topic
#     input_ids = tokenizer(topic, return_tensors="pt")
#     outputs = model.generate(input_ids=input_ids, max_length=512)
#     generated_text = tokenizer.decode(outputs.last_output_ids, skip_eos=True)
#     return generated_text

# def generate_images(text):
#     # Extract keywords and phrases for image generation
#     keywords = extract_keywords(text)

#     # Generate images for each keyword
#     generated_images = []
#     for keyword in keywords:
#         image = dalle.generate(keyword)
#         generated_images.append(image)

#     return generated_images

# st.title("AI Post Generator")

# # Create text input field
# topic = st.text_input("Enter a topic for your post:")

# # Generate button
# if st.button("Generate Post"):
#     # Generate text and images
#     generated_text = generate_text(topic)
#     generated_images = generate_images(generated_text)

#     # Split generated text into sections
#     sections = split_text_into_sections(generated_text)

#     # Display generated content
#     for section, image in zip(sections, generated_images):
#         st.markdown("## Section")
#         st.markdown(section)
#         st.image(image)










import streamlit as st
from PIL import Image
from transformers import pipeline

# Load the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Streamlit app
st.title("Text and Image Generation")

# Text input
user_input = st.text_area("Enter your text:", "I want to create a post about AI in healthcare.")

# Button to generate text and image
if st.button("Generate"):
    # Generate text
    generated_text = generator(user_input, max_length=330, num_return_sequences=1)[0]["generated_text"]

    # Display generated text
    st.subheader("Generated Text:")
    st.write(generated_text)

    # Image generation logic (replace this with your actual image generation code)
    # For example, let's generate a placeholder image
    placeholder_image = Image.new("RGB", (300, 300), color="lightblue")

    # Display generated image
    st.subheader("Generated Image:")
    st.image(placeholder_image, caption="Generated Image", use_column_width=True)

# Note: Replace the placeholder image generation logic with your actual image generation code.
# You can use libraries like PIL, OpenCV, or any other image processing libraries for image generation.