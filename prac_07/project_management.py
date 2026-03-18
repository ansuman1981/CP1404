"""
CP1404 Practical
Project Management program
"""
import datetime
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
            display_projects(projects)
        elif choice == "U":
            update_project(projects)
        elif choice =="A":
            add_project(projects)
        elif choice =="F":
            filter_project(projects)
        else:
            print("good")
        choice = input(">>>").upper()

def filter_project(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    # covert input to date
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = []

    for project in projects:
        # convert input to date
        project_date = datetime.datetime.strptime(project["date"], "%d/%m/%Y").date()
        if project_date>= filter_date:
            filtered_projects.append(project)

    # sort by date
    filtered_projects.sort(key=lambda p: datetime.datetime.strptime(p.start_date, "%d/%m/%Y"))

    # display
    for project in filtered_projects:
        print(project)


def add_project(projects):
    print("lets add new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    # create Project object
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    # add to list
    projects.append(new_project)

def update_project(projects):
    # display all the projects with index
    for i, project in enumerate(projects):
        print(f"{i}. {project}")
    # user select the project
    choice = int(input("Projects choice:"))
    project = projects[choice]
    # print the project
    print(project)
    # update the completion
    new_completion = input("New percentage:")
    if new_completion != "":
        project.completion = int(new_completion)
    # update the priority
    new_priority = input("New priority:")
    if new_priority != "":
        project.priority = int(new_priority)


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