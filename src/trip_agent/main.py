import streamlit as st
from src.trip_agent.UI.streamlit.load_ui import LoadStreamlitUI   
from src.trip_agent.crew.crew import TripCrew


def load_trip_planner(): 

    ui_loader = LoadStreamlitUI() 
    user_controls = ui_loader.load_ui()   


    if not user_controls["gemini_api_key"] or not user_controls["serper_api_key"] or not user_controls["browserless_api_key"]: 
        st.warning("Please enter all API keys in the sidebar to proceed.") 
        st.stop()  

   
    st.session_state["serper_api_key"] = user_controls["serper_api_key"] 
    st.session_state["gemini_api_key"] = user_controls["gemini_api_key"]
    st.session_state["browserless_api_key"] = user_controls["browserless_api_key"]
         
            
    location = st.text_input("Where are you currently located?", placeholder="San Mateo, CA")
    cities = st.text_input("City and country are you interested in vacationing at?", placeholder="Bali, Indonesia")
    date_range = st.date_input("Select your travel dates:", [], format="DD/MM/YYYY")  
    interests = st.text_area("What are your interests and preferences for this trip?", placeholder="e.g., beaches, hiking, cultural experiences, food")
    
    
    if user_controls["start_planning"]:    
        with st.spinner("Planning your trip... This may take a few minutes."):
                trip_crew = TripCrew(
                origin=location,
                cities=cities,
                date_range=date_range,
                interests=interests, 
                user_controls=user_controls
                )
                result = trip_crew.run() 
        st.markdown("Your Personalized Trip Plan:")  
        st.markdown(result)  



