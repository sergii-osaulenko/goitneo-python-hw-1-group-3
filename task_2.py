def parse_input(user_input):
    # Parses user input into a command and arguments
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def add_contact(args, contacts):
    # Adds a contact to the dictionary. Format: add [name] [phone number]
    if len(args) != 2:
        return "Invalid command. Format: add [name] [phone number]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    # Changes the phone number of an existing contact. Format: change [name] [new phone number]
    if len(args) != 2:
        return "Invalid command. Format: change [name] [new phone number]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    # Displays the phone number of a contact. Format: phone [name]
    if len(args) != 1:
        return "Invalid command. Format: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    # Displays all contacts
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

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