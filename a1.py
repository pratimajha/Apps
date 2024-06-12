todos = []

while True:
    user_input = input("Type add, edit, show or exit")
    user_text = user_input.strip()

    match user_text:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo.capitalize())
            print(f"{todo} added to your list")

        case 'edit':
            number = int(input("Enter the number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter the todo:")
            todos[number] = new_todo.capitalize()

        case 'show':
            for i in todos:
                print(i)

        case 'exit':
            break
    
for index,item in enumerate(todos):
    row = f"{index +1} - {item}"
    print("The total number of todos you have are:/n", row)

# print("Goodbye!")
