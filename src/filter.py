from config import *


def is_done(task):
  return task.status == 2


def show_done():
  global task_list
  done_tasks = list(filter(is_done, task_list))
  return done_tasks


def show_undone():
  global task_list
  undone_tasks = list(filter(lambda x: not is_done(x), task_list))
  return undone_tasks
