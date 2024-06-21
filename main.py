import random
import termcolor

def generate_password(length, difficulty):
    if difficulty == "easy":
        character_list = "abcdefghijklmnopqrstuvwxyz"
    elif difficulty == "medium":
        character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif difficulty == "hard":
        character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_#@£_¥~*"
    else:
        raise ValueError("Invalid difficulty level")

    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = []
    for _ in range(length):
        password.append(random.choice(character_list))

    random.shuffle(password)
    return ''.join(password)

def print_banner():
    print_color("----------------------------------","yellow")
    print_color("| D4RK-INJECTOR v1.0-Password Gen |","yellow")
    print_color("----------------------------------","yellow")
    print("Author: LocalHost.07")
    print("")

def print_color(text, color):
    print(termcolor.colored(text, color))
def main():
    print_banner()
    print_color("", "yellow")

    username = input("Enter username to login: ")
    password = input("Enter password to login: ")

    if username == "Admin" and password == "Admin":
        print("")
        print_color("Login successful!", "green")
        print("")

        length = int(input("Enter password length (min. 5): "))
        difficulty = input("Choose password difficulty (easy, medium, hard): ")

        password = generate_password(length, difficulty)
        print("")
        print_color(f"Generated Password: {password}", "yellow")
        print("")

    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
