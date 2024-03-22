from flask import Flask, request, jsonify
from ctransformers import AutoModelForCausalLM

app = Flask(__name__)

model_load_path = r"D:\nabil\pfe\scripts\hosting\llama_2\app\llama-2-7b-chat.Q4_K_M.gguf"
# Load the model from the local path
llama = AutoModelForCausalLM.from_pretrained(model_load_path, gpu_layers=0)

def ask_llama(question,context):
  system_prompt = "you are a professional legal contractor ,answer the question based on the provided context"
  user_message=f"context:{context} , the question is : {question}"

  prompt = f"<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{user_message} [/INST]"
  answer=llama(prompt)
  return answer
@app.route('/ask_llama', methods=['POST'])
def get_llama_response():
    data = request.json
    question = data.get('question')
    context = data.get('context')

    if not question or not context:
        return jsonify({'error': 'Question and context are required.'}), 400

    answer = ask_llama(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all interfaces on port 5000
