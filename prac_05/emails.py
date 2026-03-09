print("""> sudo apt-get upgrade
...
After this operation, 267 kB of additional disk space will be used.
Do you want to continue? [Y/n] blah
Abort.""")
def main():
    email_to_name = {}
    email = input("Enter your email: ")
    while email !="":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm == "n":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    print(email_to_name)


def extract_name(email: str):
    """extract name from email"""
    name_part = email.split("@")[0]
    parts = name_part.split(".")
    name = "".join(parts)
    return name

main()

