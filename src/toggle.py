from tkinter import simpledialog, messagebox
from config import task_list


def toggle_check_task():
  task = simpledialog.askstring("Ввод", "Введите имя задачи:")
  needed_task = 'something'
  global task_list
  if task_list:
    for tasks in task_list:
      if tasks.name == task:
        needed_task = tasks
        break

  if needed_task.status == 2:
    needed_task.status = 1
    getman = messagebox.showinfo(
      'Успех!', f'{needed_task.name} отмечена невыполненной!')
  else:
    needed_task.status = 2
    getman = messagebox.showinfo(
      'Успех!', f'{needed_task.name} отмечена выполненной! Поздравляем!')

  return needed_task


def final_toggle():
  toggle_check_task()
