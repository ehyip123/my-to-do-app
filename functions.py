def get_todos(filepath='C:/Users/yip_c/To do list/todolist.txt'):
    with open(filepath, 'r') as f:
        todos = f.readlines()
        return todos


def write_file(todos_arg, filepath='C:/Users/yip_c/To do list/todolist.txt'):
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)