from classes import Task
from config import task_list


def sort_by_deadline():
  task_list.sort(key=Task.get_deadline)

def sort_by_status():
  task_list.sort(key=Task.get_status)