import streamlit as st
import getpass
import os
from ibm_watsonx_ai.foundation_models import Model

# Function to get credentials
def get_credentials():
    return {
        "url": "https://eu-de.ml.cloud.ibm.com",
        # "apikey": getpass.getpass("FwNK4ev9erRUbujANgK8HTfsAFwjYfBYVDdzfG7Lf89g")
        "apikey": "FwNK4ev9erRUbujANgK8HTfsAFwjYfBYVDdzfG7Lf89g"
    }

# Define your model ID and parameters
model_id = "sdaia/allam-1-13b-instruct"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1
}

# Set environment variables (replace with your actual project_id and space_id)
os.environ["PROJECT_ID"] = "d3e78497-d338-4f22-bdf0-4aabfefb0cd5"
os.environ["SPACE_ID"] = "https://eu-de.ml.cloud.ibm.com"

project_id = os.getenv("PROJECT_ID")
space_id = os.getenv("SPACE_ID")

# Load your model using the credentials
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=get_credentials(),
    project_id=project_id,
)

# Function to generate poetry based on user input (right hemistich)
def generate_poetry(right_hemistich):
    # Define the prompt format for the left hemistich generation
    generate_prompt = f"""<<SYS>>

    You are a creative and skilled poet. Your task is to complete the Arabic left hemistich provided by the user with a right Arabic hemistich that matches the meter and rhyming structure of the given meter which you will identify. Pay attention to the following:
    - Meter: Identify the meter of the provided right hemistich and ensure the generated left hemistich adheres to the same meter as the right. If the right hemistich is in one meter, the left hemistich should also follow the same, and so on.
    - Rhyme Scheme: The left hemistich should match the rhyming structure of the meter.
    - Tone and Emotion: The left hemistich should resonate with the tone and emotional content of the right hemistich. Keep the mood consistent—whether it's somber, joyful, romantic, or reflective.
    - Poetic Devices: Use appropriate poetic devices like alliteration, assonance, or imagery to enhance the beauty and impact of the line. Aim for elegance and depth.

    Your response format should be as follows:
    - Only provide the generated left hemistich. With no additional information.
    - Only respond in Arabic language.
    - Strip the generated text to remove any extra spaces.
    <</SYS>>

    Here is the right hemistich to complete: {right_hemistich}
    """

    # Use the model to generate the left hemistich
    response = model.generate_text(prompt=generate_prompt, guardrails=False)
    generated_left_hemistich = response.strip()  # Strip unnecessary spaces

    return generated_left_hemistich

# Streamlit app
st.image('1.jpeg')
st.title("Arabic Poetry Generation")
st.write("This application generates a poetic left hemistich based on the given right hemistich. Enter the right half, and the model will complete it with matching rhythm and tone.")

# User input
right_hemistich = st.text_input("Enter Right Hemistich")

# Generate poetry and display result
if st.button("Generate"):
    if right_hemistich:
        with st.spinner("Generating..."):
            result = generate_poetry(right_hemistich)
        st.text_area("Generated Left Hemistich", value=result, height=800)
    else:
        st.warning("Please enter a right hemistich to proceed.")
