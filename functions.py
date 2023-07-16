def get(filepath="todos.txt"):
    '''Read a text file and return the list of to_do items'''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write(todos_arg,filepath="todos.txt"):
    ''' Write the todo item in text file.'''
    with open(filepath,'w') as file:
        file.writelines(todos_arg)