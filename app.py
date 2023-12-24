import google.generativeai as genai
import streamlit as st

def setup():
    try:
        gemini_api_key = 'AIzaSyDZz2F4XhXnSSzRwP04grS83eD2Bil6WS4'
        genai.configure(api_key=gemini_api_key)
    except Exception as exception:
        raise Exception("An error occurred during setup:", exception)

def generate_text(prompt):
    try:
        if st.button('Generate'):
          model = genai.GenerativeModel(model_name='gemini-pro')
          formatted_prompt = (f'You are a seasoned business executive providing strategic decision for a company. \
                      Your response should reflect a deep understanding of current market business trends and provide clear, actionable decisions. \
                      also give potential risks and opportunities of your decision, and justify your decisions with sound reasoning. \
                      make sure that when you give response start with your  decision first\
                              problem or bussiness product is : ' + prompt)
          
          response = model.generate_content(formatted_prompt )
        return response.text
    except Exception as exception:
        raise Exception("An error occurred during text generation:", exception)

if __name__ == "__main__":
  try:
    setup()
    st.title('AI for Bussiness')
    prompt = st.text_area("Enter your problem :")
    response = generate_text(prompt)
    st.write(response)
    print(response)
  except Exception as exception:
    print(f"An error occurred: {exception}")