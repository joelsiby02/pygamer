from textwrap import dedent
from crewai import Agent

import os
from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature = 0.3)



class GameAgents():
	def senior_engineer_agent(self):
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech that this world has every seen.
				Your expertise in programming in python. and do your best to produce perfect clean and struchured code with appropriate proper comments
				"""),
            llm = llm,
			allow_delegation=False,
			verbose=True
		)

	def qa_engineer_agent(self):
		return Agent(
			role='Software Quality Control Engineer',
  		goal='create prefect code, by analizing the code that is given for errors',
  		backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors & also its quality. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets, proper comments and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
        llm = llm,
		allow_delegation=False,
		verbose=True
		)

	def chief_qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
  		goal='Ensure that the code does the job that it is supposed to do',
  		backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
        llm = llm,
		allow_delegation=True,
		verbose=True
		)