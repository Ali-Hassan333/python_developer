# Import necessary libraries
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
import streamlit as st
from tasks import CrewTasks
from agents import CrewAgents

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Define the Streamlit app
def main():
    st.title('Python Developer')

    # User input for game details
    code = st.text_input("What is the problem you want to solve?")

    # Create Agents and Tasks
    tasks = CrewTasks()
    agents = CrewAgents()

    senior_engineer_agent = agents.senior_engineer_agent()
    qa_engineer_agent = agents.qa_engineer_agent()
    chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

    code_task = tasks.code_task(senior_engineer_agent, code)
    review_task = tasks.review_task(qa_engineer_agent, code)
    approve_task = tasks.evaluate_task(chief_qa_engineer_agent, code)

    crew = Crew(
        agents=[
            senior_engineer_agent,
            qa_engineer_agent,
            chief_qa_engineer_agent
        ],
        tasks=[
            code_task,
            review_task,
            approve_task,
        ],
        verbose=True
    )

    # Add a button to manually run the Crew
    if st.button("Run Crew"):
        # Display a loading indicator while the Crew is running
        with st.spinner("Running Your crew..."):
            # Execute the game building process
            code = crew.kickoff()

        # Display the final code
        st.write("Final code:")
        st.code(code)

if __name__ == '__main__':
    main()