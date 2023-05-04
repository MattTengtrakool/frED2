# frED2: Custom-trained AI Chatbot for Education

This repository contains code for a custom-trained AI chatbot based on OpenAI's GPT-3.5-turbo model. The chatbot is designed to help answer questions related to specific educational content. This modified bot was designed to provide more accurate and contextually relevant responses based on the indexed information as well as provide a basis for research on context bounding for educational purposes. Read more here. 

## Prerequisites

1. Python 3.7 or later
2. Gradio
3. OpenAI API Key

## Installation

1. Clone the repository:
git clone https://github.com/MattTengtrakool/frED2.git
cd frED2

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install the required packages:
pip install -r requirements.txt

## Setup

1. Add your educational content as text files in the `docs` directory. Each file should contain a separate piece of content, such as a lesson or a chapter.

2. Set the OpenAI API key as an environment variable:
export OPENAI_API_KEY='your_api_key_here'

3. Make sure your working directory is set to the script's location. Add the following lines at the beginning of your script:

```python
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)'''

## Running the Chatbot

1. Run the chatbot script:
python app.py

## License
This project is licensed under the MIT License.
