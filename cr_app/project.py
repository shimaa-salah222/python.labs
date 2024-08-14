projects = []

def create_project():
    print("Create a new project:")
    title = input("Enter the title of the project: ")
    description = input("Enter the description of the project: ")
    funding_goal = float(input("Enter the funding goal: "))
    duration = int(input("Enter the duration of the project (in days): "))

    # Create a new project
    project = {"id": len(projects) + 1, "title": title, "description": description, "funding_goal": funding_goal, "duration": duration}
    projects.append(project)
    print("Project created successfully!")

def list_projects():
    print("List of projects:")
    for project in projects:
        print(f"{project['id']}. {project['title']} - {project['description']}")

if __name__ == "__main__":
    pass