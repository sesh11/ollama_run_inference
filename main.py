import streamlit as st
import json
# This is where you'll interact with the LLaMA model using Ollama API
def invoke_llama_model(user_input):
    # For demonstration purposes, we'll assume a basic API call to Ollama
    import requests
    response = requests.post('http://localhost:11434/api/generate', json={'prompt': user_input, 'model': 'llama3.1:latest', 'stream':False})
    print(response.status_code) 
    print(response.text)
    response_data = response.json()
    generated_text = response_data.get('response')
    return generated_text
    # responses = []
    # for obj in json.loads(response.content):
    #     # For each JSON object in the response, extract the relevant data
    #     response_data = {}
            
    #     for key, value in obj.items():
    #         if key == 'response':
    #             # If the key is 'response', we only care about its value
    #             response_data[key] = value
                    
    #     responses.append(response_data)
    # return responses
   

# Main app function
def main():
    st.title("LLaMA 3.1 Model Invoker")
    
    # Input field for user text
    input_field = st.text_area("Enter text to invoke the model...")
    
    # Button to trigger invocation
    if st.button('Invoke Model'):
        user_input = input_field
        llama_response = invoke_llama_model(user_input)
        st.write(llama_response)


if __name__ == '__main__':
    main()





