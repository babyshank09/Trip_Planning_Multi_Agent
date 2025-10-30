import streamlit as st  
from src.trip_agent.agents.agents import TripAgents
from src.trip_agent.tasks.tasks import TripTasks
from crewai import Crew
from crewai import LLM

class TripCrew:

    def __init__(self, origin, cities, date_range, interests, user_controls):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        # Convert date_range to string format for better handling
        self.date_range = f"{date_range[0].strftime('%d-%m-%Y')} to {date_range[1].strftime('%d-%m-%Y')}" 
        self.output_placeholder = st.empty()
        self.llm = LLM(model="gemini/gemini-2.0-flash", api_key=user_controls["gemini_api_key"])
        # self.llm = OpenAI(
        #     temperature=0.7,
        #     model_name="gpt-4",
        # )

    def run(self):
        try:
            agents = TripAgents(llm=self.llm)
            tasks = TripTasks()

            city_selector_agent = agents.city_selection_agent()
            local_expert_agent = agents.local_expert()
            travel_concierge_agent = agents.travel_concierge()

            identify_task = tasks.identify_task(
                city_selector_agent,
                self.origin,
                self.cities,
                self.interests,
                self.date_range
            )

            gather_task = tasks.gather_task(
                local_expert_agent,
                self.origin,
                self.interests,
                self.date_range
            )

            plan_task = tasks.plan_task(
                travel_concierge_agent,
                self.origin,
                self.interests,
                self.date_range
            )

            crew = Crew(
                agents=[
                    city_selector_agent, local_expert_agent, travel_concierge_agent
                ],
                tasks=[identify_task, gather_task, plan_task],
                verbose=True
            )

            result = crew.kickoff()
            # self.output_placeholder.markdown(result) 
            # print(f"{self.output_placeholder}")
            # print("\n\n")
            # print(f"{self.output_placeholder.markdown}")
            return result

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            return None