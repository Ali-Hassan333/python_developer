from textwrap import dedent
from crewai import Task

class CrewTasks():
	def code_task(self, agent, code):
		return Task(description=dedent(f"""You will create python code , these are the instructions:

			Instructions
			------------
    	    {code}

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=agent,
			expected_output="The expected output is clean, well structured, bug free and updated code"
		)

	def review_task(self, agent, code):
		return Task(description=dedent(f"""\
			You are helping create a python code, these are the instructions:

			Instructions
			------------
			{code}

			Using the code you got, check for errors. Check for logic errors,
			syntax errors, missing imports, variable declarations, mismatched brackets,
			and security vulnerabilities.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=agent,
			expected_output="The expected output is clean, well structured, bug free and updated code"
		)

	def evaluate_task(self, agent, code):
		return Task(description=dedent(f"""\
			You are helping create a game using python, these are the instructions:

			Instructions
			------------
			{code}

			You will look over the code to insure that it is complete and
			does the job that it is supposed to do.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=agent,
			expected_output="The expected output is clean, well structured, bug free, updated and complete code."
		)