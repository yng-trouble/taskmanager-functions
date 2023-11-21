#!/usr/bin/env python

from add import *
from classes import *
from config import *
from display import *
from filter import *
from sort import *
from toggle import *
import tkinter as tk


def main():
  root = tk.Tk()
  root.title('БурЛёня: Пальто-менеджер Ирманских Задач!')

  add_button = tk.Button(root, text='Создать задачу', command=add_task)
  add_button.pack(pady=5)

  show_all_button = tk.Button(root,
                              text='Показать мои задачи',
                              command=show_all_tasks)
  show_all_button.pack(pady=5)

  show_done_button = tk.Button(root,
                               text='Показать выполненные задачи',
                               command=show_done_tasks)
  show_done_button.pack(pady=5)

  show_undone_button = tk.Button(root,
                                 text='Показать невыполненные задачи',
                                 command=show_undone_tasks)
  show_undone_button.pack(pady=5)

  sort_by_deadline_button = tk.Button(
    root,
    text='Отсортировать задачи по сроку выполнения',
    command=show_sorted_deadline)
  sort_by_deadline_button.pack(pady=5)

  sort_by_status_button = tk.Button(
    root,
    text='Отсортировать задачи по статусу выполнения',
    command=show_sorted_status)
  sort_by_status_button.pack(pady=5)

  remove_button = tk.Button(root, text='Удалить задачу', command=remove_task)
  remove_button.pack(pady=5)

  toggle_done_button = tk.Button(
    root,
    text='Отметить задачу выполненной/невыполненой',
    command=toggle_check_task)
  toggle_done_button.pack(pady=5)

  #printas = tk.Button(root, text='тасклист', command=lambda: print(task_list))
  #printas.pack(pady=5)

  root.mainloop()


main()
