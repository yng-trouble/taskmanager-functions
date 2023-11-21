from config import task_list
from classes import Task
from tkinter import simpledialog


def add_task():
  task_name = simpledialog.askstring("Ввод", "Введите имя задачи:")
  task_description = simpledialog.askstring("Ввод", "Введите описание задачи:")
  task_deadline = simpledialog.askstring(
    "Ввод", "Введите крайний срок выполнения задачи:")

  my_task = Task(task_name, task_description, task_deadline, 1)
  task_list.append(my_task)
