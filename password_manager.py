import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("Secure Password Manager")

    service = input("Service name: ")
    password = getpass.getpass("Enter password: ")

    hashed = hash_password(password)

    with open("vault.txt", "a") as file:
        file.write(f"{service}:{hashed}\n")

    print("Password stored securely (hashed).")

if __name__ == "__main__":
    main()
