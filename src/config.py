from tkinter import simpledialog, messagebox
from classes import Task

task_list = []


def remove_task():
  task_to_remove = simpledialog.askstring("Ввод", "Введите имя задачи:")
  global task_list

  if task_list:
    for tasks in task_list:
      if tasks.name == task_to_remove:
        task_list.remove(tasks)
        mapman = messagebox.showinfo('Успех!', 'Задача успешно удалена!')

      else:
        mapman = messagebox.showinfo('Хм...', 'Такой задачи не существует')

  elif task_to_remove is None:
    mapman = messagebox.showinfo('Внимание',
                                 'Вы не выбрали задачу для удаления')

  else:
    mapman = messagebox.showinfo('Ошибка!', 'Список задач пуст!')
