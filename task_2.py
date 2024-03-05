def parse_input(user_input):
    """
    Parses user input and returns a command and its arguments.

    Args:
        user_input (str): The user's input string.

    Returns:
        tuple: A tuple containing the command (str) and a list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Adds a contact to the contacts dictionary.

    Args:
        args (list): A list containing the name and phone number.

    Returns:
        str: A message indicating whether the contact was added successfully.
    """
    if len(args) != 2:
        return "Invalid input. Please provide a name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Similar updates for other functions...

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()