from flask import Flask, request, jsonify, render_template
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os
import json
def load_api_key():
    with open("secrets.json", "r") as file:
        secrets = json.load(file)
    return secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = load_api_key()

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 1024
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')
    return GPTSimpleVectorIndex.load_from_disk('index.json')

def chatbot(input_text, index):
    response = index.query(input_text, response_mode="compact")
    print(response)
    return response.response

app = Flask(__name__)
index = None

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot_api():
    global index
    input_text = request.json.get("input_text", "")
    response = chatbot(input_text, index)
    return jsonify({"response": response})

if __name__ == "__main__":
    src_directory = os.path.dirname(os.path.abspath(__file__))
    docs_directory = os.path.join(src_directory, '..', 'data')
    index = construct_index(docs_directory)
    
    app.run(debug=True)
