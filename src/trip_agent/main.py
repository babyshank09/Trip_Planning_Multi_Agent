import streamlit as st
from src.trip_agent.UI.streamlit.load_ui import LoadStreamlitUI   
from src.trip_agent.crew.crew import TripCrew
from datetime import datetime


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
        # Validate inputs
        if not location or not cities or not interests:
            st.error("❌ Please fill in all fields before planning.")
            st.stop()
        
        if not date_range or len(date_range) == 0:
            st.error("❌ Please select travel dates.")
            st.stop()
        
        with st.spinner("✨ Planning your trip... This may take a few minutes."):
            try:
                trip_crew = TripCrew(
                    origin=location,
                    cities=cities,
                    date_range=date_range,
                    interests=interests, 
                    user_controls=user_controls
                )
                result = trip_crew.run()
                
                # Store in session state
                if result:
                    st.session_state['trip_result'] = str(result)
                    st.session_state['trip_cities'] = cities
                else:
                    st.error("❌ No trip plan generated. Please try again.")
                    st.stop()
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.stop()
        
        st.success("✅ Your trip plan is ready!")
        st.balloons()
    
    # Display result if exists
    if 'trip_result' in st.session_state:
        result = st.session_state['trip_result']
        cities = st.session_state['trip_cities']
        
        # Display the plan
        st.markdown("### 📋 Your Personalized Trip Plan")
        st.markdown(
            f'<div class="neon-markdown">{result}</div>',
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Download button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 DOWNLOAD TRIP PLAN",
                data=result,
                file_name=f"Trip_Plan_{cities.replace(',', '_').replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
                use_container_width=True,
                type="primary"
            )


