from config import task_list
from filter import *
from tkinter import messagebox
from sort import *


def show_all_tasks():
  global task_list
  if task_list == []:
    nepman = messagebox.showinfo('Пусто!', 'У вас пока что нет задач!')

  else:
    for task in task_list:
      nepman = messagebox.showinfo(
        f'{task.name}', f'Задача: {task.description}\nДата: {task.deadline}')


def show_sorted_deadline():
  global task_list
  if task_list == []:
    nepman = messagebox.showinfo('Пусто!', 'У вас пока что нет задач!')
  else:
    sort_by_deadline()
    show_all_tasks()


def show_sorted_status():
  global task_list
  if task_list == []:
    nepman = messagebox.showinfo('Пусто!', 'У вас пока что нет задач!')
  else:
    sort_by_status()
    show_all_tasks()


def show_done_tasks():
  global task_list
  if task_list == []:
    nepman = messagebox.showinfo('Пусто!', 'У вас пока что нет задач!')
  else:
    dont = show_done()
    if dont == []:
      nepman = messagebox.showinfo('Пусто!', 'У вас нет выполненных задач!')
    else:
      for task in dont:
        mipman = messagebox.showinfo(
          f'{task.name}', f'Задача: {task.description}\nДата: {task.deadline}')


def show_undone_tasks():
  global task_list
  if task_list == []:
    nepman = messagebox.showinfo('Пусто!', 'У вас пока что нет задач!')
  else:
    undont = show_undone()
    if undont == []:
      nepman = messagebox.showinfo('Пусто!', 'У вас нет невыполненных задач!')
    else:
      for task in undont:
        mipman = messagebox.showinfo(
          f'{task.name}', f'Задача: {task.description}\nДата: {task.deadline}')


