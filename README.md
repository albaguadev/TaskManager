# Task Manager

A Python-based task management application designed for streamlined task organisation, completion tracking, and AI-assisted task decomposition.

## Overview

Task Manager is a command-line application that facilitates the management of tasks through basic operations such as adding, deleting, completing, and listing tasks. Integration with OpenAI's API enables the breakdown of complex tasks into smaller, manageable subtasks.

## Features

- **Task Creation**: New tasks may be created with descriptive text.
- **Task Deletion**: Existing tasks can be removed from the task list.
- **Task Completion**: Tasks may be marked as completed whilst maintaining their records.
- **Task Listing**: All tasks shall be displayed with their current status and identifiers.
- **AI-Assisted Decomposition**: Complex tasks are broken down into 3-5 smaller subtasks via OpenAI's API.
- **Persistent Storage**: Tasks are stored in JSON format for persistence between sessions.

## Requirements

- Python 3.8 or higher
- Dependencies as specified in `requirements.txt`

## Installation

### Setup

1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   cd TaskManager
   ```

2. A virtual environment shall be created:
   ```bash
   python3 -m venv venv
   ```

3. The virtual environment shall be activated:
   ```bash
   # On Linux/macOS
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

4. Dependencies shall be installed:
   ```bash
   pip install -r requirements.txt
   ```

5. An `.env` file shall be created in the project root with the following content:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Running the Application

The application may be executed by running:
```bash
python main.py
```

### Menu Options

Upon execution, the following menu shall be displayed:

```
--- Task Manager ---

1. Add Task
2. Add complex Task (with AI)
3. Delete Task
4. Complete Task
5. List Tasks
6. Exit
```

#### Add Task (Option 1)
A prompt shall request a task description. The task is then added to the list and persisted to storage.

#### Add complex Task (with AI) (Option 2)
A prompt shall request a complex task description. The OpenAI API shall be utilised to decompose the task into 3-5 smaller, manageable subtasks. Each generated subtask shall be automatically added to the task list.

#### Delete Task (Option 3)
A prompt shall request the task ID to be deleted. The specified task shall be removed from the list.

#### Complete Task (Option 4)
A prompt shall request the task ID to be marked as completed. The task status shall be updated accordingly.

#### List Tasks (Option 5)
All tasks shall be displayed with their current status (Completed or Pending) and identifiers.

#### Exit (Option 6)
The application shall be terminated.

## Project Structure

```
TaskManager/
├── main.py                  # Command-line interface
├── task_manager.py          # Core TaskManager and Task classes
├── ai_service.py            # OpenAI integration for task decomposition
├── requirements.txt         # Project dependencies
├── tasks.json              # Persistent task storage
├── README.md               # Project documentation
└── tests/
    └── test_task_manager.py # Unit tests
```

## Core Components

### Task Class
The `Task` class represents an individual task with the following attributes:
- `id`: Unique identifier
- `description`: Task description text
- `completed`: Boolean status (default: False)

Methods:
- `mark_completed()`: Updates task status to completed
- `__str__()`: Returns formatted task representation

### TaskManager Class
The `TaskManager` class manages task operations with the following key methods:

- `add_task(description)`: Creates and stores a new task
- `delete_task(id)`: Removes a task by identifier
- `complete_task(id)`: Marks a task as completed
- `list_tasks()`: Displays all tasks
- `save_tasks(filename)`: Persists tasks to JSON file
- `load_tasks(filename)`: Retrieves tasks from JSON file

### AI Service Module
The `ai_service.py` module provides OpenAI API integration:

- `create_simple_tasks(task)`: Breaks down a complex task into 3-5 smaller, manageable subtasks

The AI service communicates with OpenAI's API to generate subtask recommendations based on the original task description.

## Testing

Unit tests have been provided to verify the functionality of core components.

### Running Tests

Tests may be executed using Python's unittest framework:
```bash
python3 -m unittest tests/test_task_manager.py
```

### Test Coverage

The test suite verifies the following functionalities:

- **test_add_task**: Task creation and storage
- **test_delete_task**: Task deletion for existing tasks
- **test_delete_nonexistent_task**: Handling of deletion attempts for non-existent tasks
- **test_complete_task**: Task completion status updates
- **test_list_tasks**: Display of multiple tasks
- **test_list_tasks_empty**: Handling when no tasks are available

## Dependencies

The project depends upon the following packages:

- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management
- Additional dependencies are listed in `requirements.txt`

## File Persistence

Tasks are persisted in `tasks.json` using the JSON format. The file is automatically created upon first use and updated whenever modifications are made to the task list.

Example `tasks.json` structure:
```json
[
    {
        "id": 1,
        "description": "Complete project documentation",
        "completed": false
    },
    {
        "id": 2,
        "description": "Review code changes",
        "completed": true
    }
]
```

## Error Handling

The application includes error handling for:

- Missing OpenAI API keys
- File I/O errors during task persistence
- Invalid user input
- Non-existent task identifiers

Appropriate messages shall be displayed when errors are encountered.

## Future Enhancements

Potential improvements for future releases:

- Database integration for improved scalability
- Task prioritisation and categorisation
- Due date and reminder functionality
- Multi-user support with authentication
- Web interface
- Task filtering and searching capabilities

## License

The project is provided as-is for educational and personal use purposes.

## Support

For issues, questions, or contributions, please refer to the project repository or contact the development team.
