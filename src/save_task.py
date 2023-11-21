from classes import Task
from random import choice, randint
import string

all_lets = ''.join(string.ascii_letters, string.digits)

def save_task(task):
    with open(choice(all_lets, randint(5, 15)), 'w') as file:
        file.write(f'{task.name}: {task.description}. Срок выполнения: {task.deadline}')