import user
import project

def main():
    print("Welcome to our App!")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user.register()
        elif choice == "2":
            user.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()