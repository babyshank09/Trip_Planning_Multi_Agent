import streamlit as st
from src.trip_agent.UI.streamlit.load_ui import LoadStreamlitUI   
from src.trip_agent.crew.crew import TripCrew


def load_trip_planner(): 

    ui_loader = LoadStreamlitUI() 
    user_controls = ui_loader.load_ui()   


    if not user_controls["gemini_api_key"] or not user_controls["serper_api_key"] or not user_controls["browserless_api_key"]: 
            st.warning("Please enter all API keys in the sidebar to proceed.") 
            st.stop()  
            
    location = st.text_input("Where are you currently located?", placeholder="San Mateo, CA")
    cities = st.text_input("City and country are you interested in vacationing at?", placeholder="Bali, Indonesia")
    date_range = st.date_input("Select your travel dates:", [], format="DD/MM/YYYY")  
    interests = st.text_area("What are your interests and preferences for this trip?", placeholder="e.g., beaches, hiking, cultural experiences, food")
    

#     if date_range:
#         date_range_str = f"{date_range[0].strftime('%d-%m-%Y')} to {date_range[1].strftime('%d-%m-%Y')}"
#         st.write(f"**Selected Travel Dates:** {date_range_str}")

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

