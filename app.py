import streamlit as st
import os
from ibm_watsonx_ai.foundation_models import Model

# Function to get credentials
def get_credentials():
    return {
        "url": "https://eu-de.ml.cloud.ibm.com",
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


def save_first_arabic_text(output):
    # Split by newline and check if the first line is Arabic
    lines = output.splitlines()
    for line in lines:
        # Check if the line contains Arabic characters
        if any("\u0600" <= char <= "\u06FF" for char in line):
            # Save the first Arabic line to a file
            with open("first_arabic_text.txt", "w", encoding="utf-8") as file:
                file.write(line.strip())
            return line.strip()  # Return the Arabic line for verification
    return "No Arabic text found"
    
# Function to generate poetry based on user input (right hemistich)
def generate_poetry(right_hemistich):
    generate_prompt = """<<SYS>>
        You are a creative and skilled poet. You will be provided with an Arabic right hemistich and your task is to generate an Arabic left hemistich that matches the meter and rhyming structure of the given hemistich.

        Pay attention to the following:
        - Meter: Identify the meter of the provided right hemistich and ensure the generated left hemistich adheres to the same meter as the right. If the right hemistich is in from one meter, the left hemistich should also follow the same, and so on.
        - Rhyme Scheme: The left hemistich should match the rhyming structure of the meter.
        - Tone and Emotion: The left hemistich should resonate with the tone and emotional content of the right hemistich. Keep the mood consistent—whether it's somber, joyful, romantic, or reflective.
        - Poetic Devices: Use appropriate poetic devices like alliteration, assonance, or imagery to enhance the beauty and impact of the line. Aim for elegance and depth.

        Your response format should be as follows:
        - Provide the generated left hemistich with no additional information.
        - Only respond in Arabic language.
        - Strip the generated text to remove any extra spaces.
        <</SYS>>"""
    
    formattedQuestion = f"""<s>[/INST]Here is the right hemistich to complete: {right_hemistich}[/INST]"""
    prompt = f"""{generate_prompt}{formattedQuestion}"""
    generated_response = model.generate_text(prompt=prompt, guardrails=False)
        
    response = save_first_arabic_text(generated_response)
    return response.strip() if response else "No response generated."
    
# Function to critique the generated left hemistich
def critique_poetry(r_hemistich, generated_left_hemistich):
    critique_prompt = """<<SYS>>
        You are a creative and skilled poet. Your task is to criticize the language, flow, structure, theme, style and rhythm of this given hemistich. Give tips for how to improve it and suggest a new and different enhnanced left hemistich.
        Your response format should be as follows:
        - Only respond in Arabic language.
        <</SYS>>"""
        
    formattedQuestion = f"""<s>[/INST]Right hemistich: {r_hemistich}, Left hemistich: {generated_left_hemistich}[/INST]"""
    prompt = f"""{critique_prompt}{formattedQuestion}"""
    generated_response = model.generate_text(prompt=prompt, guardrails=False)
 
    return generated_response.strip() if generated_response else "No critique generated."


# Streamlit Interface
st.image('Adeeb2.png', width=300)
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
            critique = critique_poetry(right_hemistich, st.session_state.left_hemistich)
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
