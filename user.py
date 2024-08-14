from datetime import datetime

users = []
projects = []

def register():
    print("Register a new user:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobile_phone = input("Enter your mobile phone (Egyptian format): ")


    if password != confirm_password:
        print("Passwords do not match. Please try again. confirm password")
        return
    
    # Validate mobile phone number
    if not mobile_phone.startswith("+20") or (len(mobile_phone) < 10 or len(mobile_phone)>14):
        print("Invalid mobile phone number. Please try again.")
        return

    # Check if email is already registered
    if any(user["email"] == email for user in users):
        print("Email already registered. Please try again.")
        return
    

    # Create a new user
    user = {"id": len(users) + 1, "first_name": first_name, "last_name": last_name, "email": email, "password": password}
    users.append(user)
    print("User registered successfully!")

    with open("user.txt", "a") as f:
        f.write(f"{email}:{password}:{first_name}:{last_name}:{mobile_phone}\n")

def login():
    print("Login:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")



    # Check if email is registered
    user = next((user for user in users if user["email"] == email), None)
    if user is None:
        print("Email not registered. Please try again.")
        return

    # Check if password is correct
    if user["password"] != password:
        print("Incorrect password. Please try again.")
        return

    print("Login successful! You are now logged in.")
   


#projects


def create_project():
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    
    while True:
        try:
            total_target = float(input("Enter the project total target (in EGP): "))
            if total_target <= 0:
                print("Total target must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid target. Please enter a valid number.")
    
    while True:
        start_date_str = input("Enter the start date (DD-MM-YYYY): ")
        try:
            start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    while True:
        end_date_str = input("Enter the end date (DD-MM-YYYY): ")
        try:
            end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
            if end_date < start_date:
                print("End date cannot be before start date. Please enter a valid date.")
                continue
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    project = {"title": title, "details": details, "total_target": total_target, "start_date": start_date, "end_date": end_date}
    projects.append(project)
    
    with open("project.txt", "a") as f:
        f.write(f"{title}:{details}:{total_target}:{start_date.strftime('%d-%m-%Y')}:{end_date.strftime('%d-%m-%Y')}\n")

def view_projects():
    if not projects:
        print("No projects found.")
        return

    projects.sort(key=lambda x: x["start_date"])
    
    for i, project in enumerate(projects):
        print(f"{i+1}. {project['title']} - Total target: {project['total_target']} EGP")


def edit_project():
    if not projects:
        print("No projects found.")
        return

    while True:
        view_projects()
        project_index = int(input("\nEnter the number of the project you want to edit or '0' to return to main menu: "))
        
        if project_index == 0:
            break
        elif 1 <= project_index <= len(projects):
            while True:
                print("\nOptions:")
                print("1. Edit title")
                print("2. Edit details")
                print("3. Edit total target")
                print("4. Edit start date")
                print("5. Edit end date")
                print("6. Back to main menu")
                choice = input("\nEnter your choice: ")
                
                if choice == '1':
                    title = input("\nEnter the new title: ")
                    projects[project_index-1]["title"] = title
                    break
                elif choice == '2':
                    details = input("\nEnter the new details: ")
                    projects[project_index-1]["details"] = details
                    break
                elif choice == '3':
                    while True:
                        try:
                            total_target = float(input("\nEnter the new total target (in EGP): "))
                            if total_target <= 0:
                                print("\nTotal target must be a positive number. Please try again.")
                                continue
                            break
                        except ValueError:
                            print("\nInvalid target. Please enter a valid number.")
                    projects[project_index-1]["total_target"] = total_target
                    break
                elif choice == '4':
                    while True:
                        start_date_str = input("\nEnter the new start date (DD-MM-YYYY): ")
                        try:
                            start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
                            break
                        except ValueError:
                            print("\nInvalid date format. Please use DD-MM-YYYY.")
                    projects[project_index-1]["start_date"] = start_date
                    break
                elif choice == '5':
                    while True:
                        end_date_str = input("\nEnter the new end date (DD-MM-YYYY): ")
                        try:
                            end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
                            if end_date < projects[project_index-1]["start_date"]:
                                print("\nEnd date cannot be before start date. Please enter a valid date.")
                                continue
                            break
                        except ValueError:
                            print("\nInvalid date format. Please use DD-MM-YYYY.")
                    projects[project_index-1]["end_date"] = end_date
                    break
                elif choice == '6':
                    break
                else:
                    print("\nInvalid option. Please choose a valid option.")
                    
def delete_project():
    if not projects:
        print("\nNo projects found.")
        return

    
    while True:
        try:
            choice = int(input("\nEnter the number of the project you want to delete (or 0 to cancel): "))
            if choice == 0:
                return
            if 0 < choice <= len(projects):
                del projects[choice-1]
                with open("project.txt", "w") as f:
                    for project in projects:
                        f.write(f"{project['title']}:{project['details']}:{project['total_target']}:{project['start_date'].strftime('%d-%m-%Y')}:{project['end_date'].strftime('%d-%m-%Y')}\n")
                print("\nProject deleted successfully.")
                return
            else:
                print("\nInvalid choice. Please enter a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        
def search_project_by_date():
    while True:
      search_start_date_str = input("\nEnter the start date (DD-MM-YYYY) or '0' to return to main menu: ")
      
      if search_start_date_str == '0':
          break
        
      try:
            search_start_date = datetime.strptime(search_start_date_str, "%d-%m-%Y")
            matching_projects = [project for project in projects if project["start_date"] >= search_start_date]
            if not matching_projects:
                print("\nNo projects found.")
                continue
            
            for i, project in enumerate(matching_projects):
                print(f"{i+1}. {project['title']} - Total target: {project['total_target']} EGP - Start Date: {project['start_date'].strftime('%d-%m-%Y')} - End Date: {project['end_date'].strftime('%d-%m-%Y')}")
            
            while True:
                choice = input("\nDo you want to continue searching for projects or return to main menu? (1/0): ")
                if choice == '0':
                    return
                elif choice == '1':
                    break
                else:
                    print("\nInvalid choice. Please enter 0 or 1.")
      except ValueError:
            print("\nInvalid date format. Please use DD-MM-YYYY.")

