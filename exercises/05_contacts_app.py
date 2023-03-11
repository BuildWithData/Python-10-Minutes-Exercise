import json


__doc__ = """

Write a contacts app which let:

    - add new contacts
    - delete any existing contact
    - search for any contact

Next steps:

    - the code should not let the user add a contact with the same
    name of an existing one, refactor such this is not allowed and 
    a "contact already exist" message is displayed instead

    - add Edit action to modify an existing contact

    - add Display All action to show the name of all available contacts

    - Don't Repeat Yourself (DRY) is a good coding principle, do you see
    any way to apply it here ?

"""

BANNER = """
  ______                         __                            __
 /      \                       /  |                          /  |
/$$$$$$  |  ______   _______   _$$ |_     ______    _______  _$$ |_    _______
$$ |  $$/  /      \ /       \ / $$   |   /      \  /       |/ $$   |  /       |
$$ |      /$$$$$$  |$$$$$$$  |$$$$$$/    $$$$$$  |/$$$$$$$/ $$$$$$/  /$$$$$$$/
$$ |   __ $$ |  $$ |$$ |  $$ |  $$ | __  /    $$ |$$ |        $$ | __$$      \
$$ \__/  |$$ \__$$ |$$ |  $$ |  $$ |/  |/$$$$$$$ |$$ \_____   $$ |/  |$$$$$$  |
$$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ $$    $$ |$$       |  $$  $$//     $$/
 $$$$$$/   $$$$$$/  $$/   $$/    $$$$/   $$$$$$$/  $$$$$$$/    $$$$/ $$$$$$$/
"""

try:
    file = open("./contacts.json", "r")
    contacts = json.load(file)
    file.close()
except FileNotFoundError:
    contacts = {}

action = None
quit = False

print(BANNER)

while quit is False:

    print("\nAvailable actions:\n")
    print("    - Add")
    print("    - Delete")
    print("    - Search")

    while action not in ["add", "delete", "search"]:
        action = input("\nType in your choice: ").lower()

    if action == "add":
        print("\n    New Contact\n")
        name  = input("    name: ")
        phone = input("    phone: ")
        email = input("    email: ")

        contacts[name] = {"phone": phone, "email": email}
        file = open("./contacts.json", "w")
        json.dump(contacts, file)
        file.close()
        print("\n   ", name, "added to contacts")

    if action == "search":
        name = input("\n    name: ")
        infos = contacts.get(name)

        if infos is None:
            print("\n    Not found")
        else:
            print("\n    phone: ", infos["phone"])
            print("    email: ", infos["email"])

    if action == "delete":
        name = input("\n    name: ")

        if name in contacts:
            contacts.pop(name)
            file = open("./contacts.json", "w")
            json.dump(contacts, file)
            file.close()
            print("\n    Deleted")
        else:
            print("\n    Not found")

    quit = input("\nType yes to quit: ").lower() == "yes"
    action = None
