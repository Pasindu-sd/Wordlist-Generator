import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choices(characters, k=length))

def generate_wordlist(length, count, filename="generated_wordlist.txt"):
    with open(filename, "w") as file:
        for _ in range(count):
            password = generate_random_password(length)
            file.write(password + "\n")
    print(f"\n Wordlist saved as '{filename}'")
    print(f"Total passwords generated: {count}")
    print(f" Password length: {length} characters")

def main():
    print(" RandWordlistGen - Random Password Wordlist Generator ")
    try:
        length = int(input(" Enter password length (e.g., 8): "))
        count = int(input(" How many passwords to generate (e.g., 1000): "))
        filename = input(" Output filename (default = generated_wordlist.txt): ").strip()
        if filename == "":
            filename = "generated_wordlist.txt"
        generate_wordlist(length, count, filename)
    except ValueError:
        print(" Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
