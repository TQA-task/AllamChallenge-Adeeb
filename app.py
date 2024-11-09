import streamlit as st
import getpass
import os
from ibm_watsonx_ai.foundation_models import Model

# Function to get credentials
def get_credentials():
    return {
        "url": "https://eu-de.ml.cloud.ibm.com",
        "apikey": ""
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
    generate_prompt = f"""<<SYS>>

    You are a creative and skilled poet. You will be provided with an Arabic right hemistich and your task is to generate an Arabic left hemistich that matches the meter and rhyming structure of the given hemistich.

    Pay attention to the following:
    - Meter: Identify the meter of the provided right hemistich and ensure the generated left hemistich adheres to the same meter as the right. If the right hemistich is in from one meter, the left hemistich should also follow the same, and so on.
    - Rhyme Scheme: The left hemistich should match the rhyming structure of the meter.
    - Tone and Emotion: The left hemistich should resonate with the tone and emotional content of the right hemistich. Keep the mood consistent—whether it's somber, joyful, romantic, or reflective.
    - Poetic Devices: Use appropriate poetic devices like alliteration, assonance, or imagery to enhance the beauty and impact of the line. Aim for elegance and depth.

    Your response should be as follows:
    - Only respond in Arabic language.
    - Provide only one generated left hemistich with NO additional text or information.  
    - Strip the generated text to remove any extra spaces.
    
    Here is the right hemistich to complete: {right_hemistich}
    <</SYS>>"""

    response = model.generate_text(prompt=generate_prompt, guardrails=False)
    return response.strip()

# Function to critique the generated left hemistich
def critique_poetry(generated_left_hemistich):
    critique_prompt = f"""<<SYS>>

    You are a creative and skilled poet. Your task is to criticize the language, flow, structure, theme, style and rhythm of this given hemistich. Give tips for how to improve it and suggest a new enhnanced left hemistich.
    Your response should be as follows:
    - Translate your response to Arabic language.
    - Provide the generated left hemistich and the identified meter separated by a hash symbol
    - your response should be one line only.
    - Strip the generated text to remove any extra spaces.

    Here is the generated left hemistich: {generated_left_hemistich}
    <</SYS>>"""

    response = model.generate_text(prompt=critique_prompt, guardrails=False)
    return response.strip()

st.image('1.jpeg', width=300)
st.markdown("<h1 style='text-align: right;'>مولد الشعر العربي: أديب</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right;'>يُنشئ هذا التطبيق شطرًا شعريًا أيسر بناءً على الشطر الأيمن المُعطى. أدخل النصف الأيمن، وسيكمله النموذج بوزن وإيقاع متناسبين.</p>", unsafe_allow_html=True)

# User input
right_hemistich = st.text_input("أدخل الشطر الأيمن", key="right_hemistich")

# Initialize session state to store generated left hemistich
if "left_hemistich" not in st.session_state:
    st.session_state.left_hemistich = None

# Generate poetry and display result
if st.button("قم بالتوليد"):
    if right_hemistich:
        with st.spinner("جاري التوليد..."):
            left_hemistich = generate_poetry(right_hemistich)
            st.session_state.left_hemistich = left_hemistich  # Store in session state

        st.markdown("<h2 style='text-align: right;'>الشطر الأيسر المُولد</h2>", unsafe_allow_html=True)
        st.text_area("", value=st.session_state.left_hemistich, height=200, key="generated_text", label_visibility="collapsed")
    else:
        st.warning("يرجى إدخال شطر أيمن للمتابعة.")

# Critique button
if st.button("عرض النقد"):
    if st.session_state.left_hemistich:
        with st.spinner("توليد النقد..."):
            critique = critique_poetry(st.session_state.left_hemistich)
        st.markdown("<h2 style='text-align: right;'>النقد والتحسين</h2>", unsafe_allow_html=True)
        st.text_area("", value=critique, height=200, key="critique_text", label_visibility="collapsed")
    else:
        st.warning("يرجى توليد الشطر الأيسر أولاً.")

# Custom CSS to align text areas to the right
st.markdown(
    """
    <style>
    textarea {
        direction: RTL;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
