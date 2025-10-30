import dotenv 
from dotenv import load_dotenv  
import os

load_dotenv("api.env") 

# serper_api_key = = os.getenv("SERPER_API_KEY") 
serper_api_key = os.getenv("SERPER_API_KEY")
print(serper_api_key)