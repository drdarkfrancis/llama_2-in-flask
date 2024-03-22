import requests
import json

# Replace this with the actual URL of your Flask app
# If you are testing locally and using ngrok, use the ngrok URL instead
url = 'http://127.0.0.1:5000/ask_llama'

# Example question and context
question = "What is the capital of France?"
context = "Geography questions about European countries."

# Prepare the data for the POST request
data = {
    'question': question,
    'context': context
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response from the server
if response.status_code == 200:
    print("Response from server:", response.json())
else:
    print("Error:", response.status_code, response.text)
