from typing import Optional

from mcp.server import MCPServer

from todo_list_mcp_server import storage
from todo_list_mcp_server.models import Priority

mcp = MCPServer("todo_list_mcp_server")


@mcp.tool()
def add_todo(title: str, priority: Priority = Priority.medium) -> str:
    """Add a new task to todo list.

    Args:
        title: A title of task needs to do
        priority: A priority of task
    """

    todo = storage.add_todo(title, priority)
    return f"Added a new todo item #{todo.id}: {todo.title} (priority: {todo.priority.value})"


@mcp.tool()
def list_todos(show_done: bool = True) -> str:
    """List todo tasks.

    Args:
        show_done: Whether to include already completed tasks
    """

    todos = storage.list_todos(show_done)
    if not todos:
        return "No todo items found."

    lines = [
        f"[{'x' if t.done else ' '}] #{t.id}: {t.title} (priority: {t.priority.value})"
        for t in todos
    ]
    return "\n".join(lines)


@mcp.tool()
def complete_todo(id: int) -> str:
    """Mark a todo task as done.

    Args:
        id: The id of the task to complete
    """

    todo = storage.complete_todo(id)
    if todo is None:
        return f"No todo item found with id #{id}"
    return f"Completed todo item #{todo.id}: {todo.title}"


@mcp.tool()
def delete_todo(todo_id: int) -> str:
    """Delete a todo task.

    Args:
        todo_id: The id of the task to delete
    """

    deleted = storage.delete_todo(todo_id)
    if not deleted:
        return f"No todo item found with id #{todo_id}"
    return f"Deleted todo item #{todo_id}"


@mcp.tool()
def update_todo(
    todo_id: int, title: Optional[str] = None, priority: Optional[Priority] = None
) -> str:
    """Update a todo task's title and/or priority.

    Args:
        todo_id: The id of the task to update
        title: The new title for the task, if changing it
        priority: The new priority for the task, if changing it
    """

    todo = storage.update_todo(todo_id, title, priority)
    if todo is None:
        return f"No todo item found with id #{todo_id}"
    return f"Updated todo item #{todo.id}: {todo.title} (priority: {todo.priority.value})"
