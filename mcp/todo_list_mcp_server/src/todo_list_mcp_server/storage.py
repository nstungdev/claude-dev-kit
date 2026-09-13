import json
from os import path
from typing import Optional

from todo_list_mcp_server.models import Priority, TodoItem

TODO_FILE = path.join(path.dirname(__file__), "todo.json")


def _load() -> list[TodoItem]:
    if not path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [TodoItem.from_dict(item) for item in raw]


def _save(todos: list[TodoItem]) -> None:
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in todos], f, indent=2, ensure_ascii=False)


def add_todo(title: str, priority: Priority = Priority.medium) -> TodoItem:
    todos = _load()
    new_id = (max((t.id for t in todos), default=0)) + 1
    new_item = TodoItem(id=new_id, title=title, priority=priority)
    todos.append(new_item)
    _save(todos)
    return new_item


def list_todos(show_done: bool = True) -> list[TodoItem]:
    todos = _load()
    if not show_done:
        return [t for t in todos if not t.done]
    return todos


def complete_todo(id: int) -> Optional[TodoItem]:
    todos = _load()
    found_item = next((t for t in todos if t.id == id), None)
    if found_item is None:
        return None
    found_item.done = True
    _save(todos)
    return found_item


def delete_todo(todo_id: int) -> bool:
    todos = _load()
    new_todos = [t for t in todos if t.id != todo_id]
    if len(todos) == len(new_todos):
        return False
    _save(todos)
    return True


def update_todo(
    todo_id: int, title: Optional[str] = None, priority: Optional[Priority] = None
) -> Optional[TodoItem]:
    todos = _load()
    for t in todos:
        if t.id == todo_id:
            if title is not None:
                t.title = title
            if priority is not None:
                t.priority = priority
            _save(todos)
            return t
    return None
