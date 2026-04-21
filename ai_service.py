from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
  if not client.api_key:
    return ["Error:OpenAI API key not found. Please set it in the .env file."]
  
  try:
    prompt = f"""The following task shall be broken down into a list of 3 to 5 smaller and more manageable subtasks.
    
    Task: {description}
    
    Response format:
    - Subtask 1
    - Subtask 2
    - Subtask 3
    -etc.
    
    Only the list of subtasks shall be provided, one per line, with each line beginning with a hyphen."""

    params = {
      "model": "gpt-5",
      "messages": [
        {"role": "system", "content": "Complex tasks are broken down into smaller, more manageable subtasks by an expert assistant in task management and productivity."},
        {"role": "user", "content": prompt}
      ],
      "verbosity": "medium",
      "max_completion_tokens": 300,
      "reasoning_effort": "minimal"
    }

    response = client.chat.completions.create(**params)

    content = response.choices[0].message.content.strip()

    subtasks = []

    for line in content.split("\n"):
      line = line.strip()
      if line and line.startswith("-"):
        subtask = line[1:].strip()
        if subtask:
          subtasks.append(subtask)
    
    return subtasks if subtasks else ["Error: No subtasks were generated. Please try again with a different task description."]

  except Exception as e:
    return ["Error: An error occurred while creating tasks. Please try again later." + str(e)]
  