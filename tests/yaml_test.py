import yaml  
from unstructured.partition.html import partition_html 
import json  
import requests 
import streamlit as st 
import dotenv 
from dotenv import load_dotenv 

load_dotenv("api.env") 

serper_api_key = os.getenv("SERPER_API_KEY") 
print(serper_api_key)

yaml_path = r"src\custom_tools_agent\config\agents.yaml" 

with open(yaml_path, "r") as file: 
    config = yaml.safe_load(file) 

role_value = config["researcher"]["role"]
print(role_value) 




import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/content?token=2SuasXau0MBArlk8c91aa2d28d78708245143ce80c4f9757f"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}
data = {
    "url": "https://example.com/"
}

response = requests.post(url, headers=headers, json=data)  
elements = partition_html(text=response.text)
content = "\n\n".join([str(el) for el in elements])
print(content)  





import json
import requests

def search_query():
    try:
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = {"q": "What is Outergrid"}
        headers = {
            "X-API-Key": "0fe3e8fe9c91996ac2e6c3b1bf58ee396acd3a76",
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            return f"Error: Search API request failed. Status code: {response.status_code}"

        data = response.json()
        if "organic" not in data:
            return "No results found or API error occurred."

        results = data["organic"]
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append("\n".join([
                    f"Title: {result['title']}", 
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError: 
                continue

        return "\n".join(string) if string else "No valid results found"

    except Exception as e:
        return f"Error during search: {str(e)}"


# Example run
print(search_query())
