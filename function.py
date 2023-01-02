def gettodo(filepath="todo.txt"):
    with open(filepath,"r") as file:
        todos=file.readlines()
    return todos
def writetodo(todos,filepath="todo.txt"):
    with open(filepath,"w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print(gettodo())