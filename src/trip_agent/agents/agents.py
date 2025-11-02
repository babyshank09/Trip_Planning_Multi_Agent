from crewai import Agent
import re
import streamlit as st
from crewai import LLM
from src.trip_agent.tools.browser_tool import BrowserTools
from src.trip_agent.tools.calculator_tool import CalculatorTools
from src.trip_agent.tools.search_tool import SearchTools

class TripAgents():
    def __init__(self, llm = None):
        if llm is None:
            self.llm = LLM(model="gemini/gemini-2.5-flash")
        else:
            self.llm = llm

        self.search_tool = SearchTools()
        self.browser_tool = BrowserTools()
        self.calculator_tool = CalculatorTools()

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory='An expert in analyzing travel data to pick ideal destinations',
            tools=[self.search_tool, self.browser_tool],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
            about the city, it's attractions and customs""",
            tools=[self.search_tool, self.browser_tool],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
            packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
            decades of experience""",
            tools=[self.search_tool, self.browser_tool, self.calculator_tool],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    

     