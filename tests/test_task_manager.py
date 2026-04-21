import unittest
from unittest.mock import patch, mock_open
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    @patch("task_manager.json.dump")
    def test_add_task(self, mock_json_dump, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.add_task("Test task")
        self.assertEqual(len(tm._tasks), 1)
        self.assertEqual(tm._tasks[0].description, "Test task")
        mock_print.assert_any_call("Task added: Test task")
        mock_json_dump.assert_called()

    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    @patch("task_manager.json.dump")
    def test_delete_task(self, mock_json_dump, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.add_task("Task to delete")
        task_id = tm._tasks[0].id
        tm.delete_task(task_id)
        self.assertEqual(len(tm._tasks), 0)
        mock_print.assert_any_call(f"Task deleted: Task to delete")
        mock_json_dump.assert_called()

    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    @patch("task_manager.json.dump")
    def test_delete_nonexistent_task(self, mock_json_dump, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.add_task("Task to keep")
        tm.delete_task(999)
        mock_print.assert_any_call("Task with ID 999 not found.")
        self.assertEqual(len(tm._tasks), 1)

    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    @patch("task_manager.json.dump")
    def test_complete_task(self, mock_json_dump, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.add_task("Task to complete")
        task_id = tm._tasks[0].id
        tm.complete_task(task_id)
        self.assertTrue(tm._tasks[0].completed)
        mock_print.assert_any_call(f"Task completed: Task to complete")
        mock_json_dump.assert_called()

    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    def test_list_tasks(self, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.add_task("Task 1")
        tm.add_task("Task 2")
        tm.list_tasks()
        mock_print.assert_any_call(tm._tasks[0])
        mock_print.assert_any_call(tm._tasks[1])

    @patch("builtins.print")
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.json.load", return_value=[])
    def test_list_tasks_empty(self, mock_json_load, mock_file, mock_print):
        tm = TaskManager()
        tm.list_tasks()
        mock_print.assert_any_call("No tasks available.")

if __name__ == "__main__":
    unittest.main()
