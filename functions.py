def get_todos(filepath = 'todolist.txt'):
    with open(filepath, 'r') as f:
        todos = f.readlines()
        return todos


def write_file(todos_arg, filepath='todolist.txt'):
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)

def get_completed(filepath = 'completed.txt'):
    with open(filepath, 'r') as f:
        completed = f.readlines()
        return completed

def write_complete(complete_arg, filepath = 'completed.txt'):
    with open(filepath,'w' ) as f:
        f.writelines(complete_arg)