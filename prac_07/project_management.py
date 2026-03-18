"""
CP1404 Practical
Project Management program
"""

from project import Project
MENU ="""(L)oad projects  
(S)ave projects  
(D)isplay projects  
(F)ilter projects by date
(A)dd new project  
(U)pdate project
(Q)uit"""

def main():
    print(MENU)
    projects = []
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "D":
            load_project(projects)
            display_projects(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("good")
        choice = input(">>>").upper()


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i}. {project}")

    choice = int(input("Projects choice:"))



def load_project(projects):
    """load the file"""
    in_file = open("projects.txt", "r")
    in_file.readline()          # skip header
    for line in in_file:
        parts = line.strip().split("\t")
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion = float(parts[4])

        management = Project(name, start_date, priority, cost_estimate, completion)
        projects.append(management)

    in_file.close()


def display_projects(projects):
    """display projects list"""
    completed_projects = []
    incompleted_projects = []
    # separate the project
    for project in projects:
        if project.completion == 100:
            completed_projects.append(project)
        else:
            incompleted_projects.append(project)

    # sort by priority
    completed_projects.sort(key=lambda p: p.priority)
    incompleted_projects.sort(key=lambda p: p.priority)

    # display
    print("Incomplete projects: ")
    for project in incompleted_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")

main()