import streamlit as st
from PIL import Image
from langchain_groq import ChatGroq
import speech_recognition as sr
import pyttsx3

# Initialize the ChatGroq instance
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.2,
    groq_api_key="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"
)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
    try:
        question = recognizer.recognize_google(audio)
        return question
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service."

def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Streamlit UI
img = Image.open("robo.png")
st.title("Enter your query below")
st.image(img, width=200)

# Text input
user_input = st.text_input("Your question :")

# Voice input
if st.button("Ask with Voice"):
    user_input = recognize_speech()

# Get answer
if user_input and st.button("Get answer"):
    response = llm.invoke(user_input)
    st.write("## Response :")
    st.write(response.content)
    speak_text(response.content)
