import streamlit as st
from dotenv import load_dotenv
from crewai import Crew
from tasks import GameTasks
from agents import GameAgents

# Load environment variables if necessary
load_dotenv()

def build_game():
    tasks = GameTasks()
    agents = GameAgents()

    st.title("Welcome to Pygamer")
    st.write("-------------------------------")
    game = st.text_input("What is the game you would like to build? Write a prompt to describe its mechanics?")

    if st.button("Build Game"):
        # Create Agents
        senior_engineer_agent = agents.senior_engineer_agent()
        qa_engineer_agent = agents.qa_engineer_agent()
        chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

        # Create Tasks
        code_game = tasks.code_task(senior_engineer_agent, game)
        review_game = tasks.review_task(qa_engineer_agent, game)
        approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

        # Create Crew responsible for Copy
        crew = Crew(
            agents=[
                senior_engineer_agent,
                qa_engineer_agent,
                chief_qa_engineer_agent
            ],
            tasks=[
                code_game,
                review_game,
                approve_game
            ],
            verbose=True
        )

        game_code = crew.kickoff()

        # Define the file name
        file_name = "game.py"

        # Write the game code to the file
        with open(file_name, "w") as file:
            file.write(game_code)

        st.write("\n\n########################")
        st.write("## Here is the result")
        st.write("########################\n")
        st.write("Final code for the game:")
        st.code(game_code)
        st.write("\n\nGame code has been saved to", file_name)

def main():
    st.sidebar.title("Pygamer")
    menu_selection = st.sidebar.radio("Navigation", ["Build Game"])

    if menu_selection == "Build Game":
        build_game()

if __name__ == "__main__":
    main()
