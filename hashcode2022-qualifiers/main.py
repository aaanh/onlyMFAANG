import os

input_file = open("an_example_in.txt", "r")
output_file = open("an_example_out.txt", "w")

skills = {}
persons = []
projects = []

class Person():
    def __init__(self, name, is_busy=False):
        self.name = name
        self.skills = {}
        self.is_busy = is_busy

class Project():
    def __init__(self, project_name, num_of_day, score, best_before, num_of_roles):
        self.project_name = project_name
        self.num_of_day = num_of_day
        self.score = score
        self.best_before = best_before
        self.num_of_roles = num_of_roles
        self.skills_needed = []

def parse_file_oop(file):
    i = 0
    file = file.read().split("\n")
    line = file[i].split()
    num_of_contributor = line[0]
    num_of_projects = line[1]
    for _ in range(int(num_of_contributor)):
        i += 1
        line = file[i].split()
        curr_person = line[0]
        num_of_skills = int(line[1])
        person = Person(curr_person)
        persons.append(person)
        for _ in range(int(num_of_skills)):
            i += 1
            line = file[i].split()
            skill = line[0]
            level = int(line[1])
            person.skills[skill] = level
    print(num_of_projects)
    i += 1
    for _ in range(int(num_of_projects)):
        line = file[i].split()
        print(line)
        project_name = line[0]
        num_of_day = int(line[1])
        score = int(line[2])
        best_before = int(line[3])
        num_of_roles = int(line[4])
        project = Project(project_name, num_of_day, score, best_before, num_of_roles)
        projects.append(project)
        for _ in range(num_of_roles):
            i += 1
            line = file[i].split()
            line.append(False)
            project.skills_needed.append(line)
            print(project.skills_needed)
        i += 1

def main():
    parse_file_oop(input_file)
    

    return 10000

if __name__ == "__main__":
    main()