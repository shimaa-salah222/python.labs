projects = []

def create_project():
    print("Create a project:")
    title = input("Enter the title of the project: ")
    details = input("Enter the details of the project: ")
    target = float(input("Enter the target amount (in EGP): "))
    start_date = input("Enter the start date of the campaign (in YYYY-MM-DD): ")
    end_date = input("Enter the end date of the campaign (in YYYY-MM-DD): ")

    # Validate dates
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if start_date > end_date:
            print("Invalid dates. Start date must be before end date. Please try again.")
            return
        if end_date > datetime.now().date():
            print("Invalid dates. End date must be in the future. Please try again.")
            return
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Create a new project
    project = {"title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date}
    projects.append(project)
    print("Project created successfully!")

def view_projects():
    if len(projects) == 0:
        print("No projects found.")
        return
    for i, project in enumerate(projects, 1):
        print(f"Project {i}: {project['title']}")
