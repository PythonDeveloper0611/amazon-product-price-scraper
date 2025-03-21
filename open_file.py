import os
import webbrowser
import subprocess

# Define the test command with HTML reporting
pytest_command = "pytest --html=report.html --self-contained-html"

# Run the test command
print("Running tests...")
subprocess.run(pytest_command, shell=True)

# Get the absolute path of the report
report_path = os.path.abspath("report.html")

# Open the HTML report in the default web browser
print(f"Opening test report: {report_path}")
webbrowser.open("file://" + report_path)
