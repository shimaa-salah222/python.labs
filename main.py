
import user 
logged_in = False

def main():
    print("Welcome to our App!")
while True:
    if not logged_in:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user.register()
        elif choice == "2":
            user.login()
            logged_in = True

        elif choice == "3":
                break
        else:
                print("Invalid option. Please choose a valid option.")
    else:
            print("\nProject Management Options:")
            print("1. Create a new project")
            print("2. List all projects")
            print("3. edit project")
            print("4. delete project")
            print("5. search project by date")
            print("6. Log out")
            choice = input("Choose an option: ")
            if choice == "1":
                user.create_project()
                
            elif choice == "2":
                user.view_projects()

            elif choice == "3":
                user.edit_project()

            elif choice == "4":
                user.delete_project()

            elif choice == "5":
                user.search_project_by_date()
                
            elif choice == "6":
                logged_in = False
            
            else:
                print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main() 