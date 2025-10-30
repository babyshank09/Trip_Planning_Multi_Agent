import streamlit as st 
from pydantic import Field, BaseModel 
import json 
import requests 
from crewai.tools import BaseTool 
import dotenv 
from dotenv import load_dotenv  
import os

load_dotenv("api.env") 
serper_api_key = os.getenv("SERPER_API_KEY")

class SearchQuery(BaseModel): 
    query: str = Field(..., description = "The search query to look up") 

class SearchTools(BaseTool): 
    name: str = "Search the internet" 
    description: str = "Useful to search the internet about a given topic and return relevant results" 
    args_schema: type[BaseModel] = SearchQuery 

    def _run(self, query: str): 
        try:  
            print(f"Performing search query for {query}...")
            top_result_to_return = 4
            url = "https://google.serper.dev/search" 
            payload = json.dumps({"q": query})
            headers = {
                "Content-Type": "application/json", 
                "X-API-Key": serper_api_key
            } 

            response = requests.request("POST", url, headers = headers, data = payload ) 

            if response.status_code != 200:
                return f"Error: Search API request failed. Status code: {response.status_code}" 
            
            data = response.json() 
            if "organic" not in data: 
                return "No organic results found or API error occurred." 
            
            results = data["organic"]  
            string = [] 

            for result in results[:top_result_to_return]:  
                try: 
                    string.append("\n".join([
                        f"Title: {result["title"]}",
                        f"Link: {result["link"]}", 
                        f"Snippet {result["snippet"]}" 
                    ])) 
                except KeyError: 
                    continue 

            print(f"Search results:\n\n{'\n\n'.join(string)}")
            return "\n".join(string) if string else "No valid results found" 
        
        except Exception as e:
            return f"Error during search: {str(e)}"





            

