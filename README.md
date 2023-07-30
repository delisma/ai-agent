# Researcher AI Agent
AI Research Agent

This project is an AI research agent that can perform high-quality research autonomously, without any hallucination. The agent uses Langchain, GPT, and Make.com to accomplish its tasks. This is script summarizes the content of a web page using the OpenAI GPT-3 language model. The script uses the Browserless API to render the web page and extract its content, and then uses the GPT-3 model to generate a summary of the content.

## Why AI Research Agent?

The idea of an AI research agent was inspired by a use case where an AI could write a Twitter thread every other day about how famous people got rich and automatically publish it. This could potentially attract 100K followers in just a year. However, real research is not a linear process. It involves opening multiple URLs, scraping information, and then realizing there are new topics to research further. It's a much more iterative process, and this is where our AI research agent comes in.

## Installation
Clone the repository to your local machine.
Install the required Python packages by running pip install -r requirements.txt.
Set the BROWSERLESS_API_KEY, SERP_API_KEY and OPENAI_API_KEY environment variables a .env file.

## Usage
To use the script, run the following command:

Replace <url> with the URL of the web page you want to summarize, and <objective> with a brief description of the objective of the summary (e.g. "to get an overview of the article").

The script will render the web page using the Browserless API, extract its content, generate a summary using the GPT-3 model, and print the summary to the console.

## License
This code is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This script was inspired by Jason Zhou, a product designer who shares interesting AI experiments & products on Youtube