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
        else:
            print("good")
        choice = input(">>>").lower()


def load_project(projects):
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
    for project in projects:
        print(project)


main()