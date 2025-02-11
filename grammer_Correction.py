import streamlit as st
from langchain_groq import ChatGroq

# Initialize the ChatGroq instance
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    groq_api_key="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"  
)

def correct_grammar(text):
    prompt = f"Check the grammar of the following text. If it's correct, return it as is. If it has grammar mistakes, correct them without changing the meaning or adding extra words. Also, list the incorrect words and provide feedback on what went wrong.\nText: {text}"
    
    response = llm.invoke(prompt)  # Get AIMessage object
    corrected_text = response.content  # Extract actual text
    
    return corrected_text

def extract_incorrect_words(response_text):
    # This will depend on how the LLM outputs feedback, here assuming a simplified approach
    incorrect_words = []
    lines = response_text.splitlines()
    for line in lines:
        if "incorrect" in line.lower():
            incorrect_words.append(line.strip())
    return incorrect_words

# Streamlit UI
st.title("Grammar Correction with Feedback")
input_text = st.text_area("Enter a sentence to check grammar:")

if st.button("Correct Grammar"):
    if input_text:
        corrected_text = correct_grammar(input_text)
        
        if corrected_text.strip() == input_text.strip():
            st.write("## Sentence is already correct:")
            st.write(input_text)
        else:
            st.write("## Corrected Text:")
            st.write(corrected_text)
            
            if "incorrect words" in corrected_text.lower():
                incorrect_words_feedback = extract_incorrect_words(corrected_text)
                st.write("## Incorrect Words and Feedback:")
                for feedback in incorrect_words_feedback:
                    st.write(feedback)
    else:
        st.write("Please enter a sentence to check.")