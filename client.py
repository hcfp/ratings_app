import requests
import json
import sys


def register(host):
    username = "user5"
    password = "password123"
    email = "email@email.com"
    host = "127.0.0.1"
    #host = input("Host: ")
    # username = input("Username: )
    #password = input("Password: ")
    #email = input("Email: ")
    response = s.post(f"http://{host}:8000/ratings/register",
                      data={'username': username, 'password': password, 'email': email}).json()
    print(response)


def login(host, username, password):
    username = "user5"
    password = "password123"
    host = "127.0.0.1"
    response = s.post(f"http://{host}:8000/ratings/login",
                      data={'username': username, 'password': password}).json()
    if response["login-success"]:
        print("Logged in")
    else:
        print("Login failed")


def logout():
    response = s.post(f"http://{global_host}:8000/ratings/logout").json()
    if response["logout-success"]:
        print("Logged out")
    else:
        print("Logout failed")


def list_all():
    response = s.get(f"http://{global_host}:8000/ratings/list").json()["list"]
    for item in response:
        print("\nModule information")
        print(f'Code: {item["module_instance__module__code"]} Name: { item["module_instance__module__name"]} Year: 20{item["module_instance__year"]} Semester: {item["module_instance__semester"]}')
        print("Taught by")
        codes = item["professor__code"].split()
        titles = item["professor__title"].split()
        first_names = item["professor__first_name"].split()
        last_names = item["professor__last_name"].split()

        for i in range(len(codes)):
            print(
                f'({codes[i]}) {titles[i]} {first_names[i]}. {last_names[i]}')
        print("-" * 70)


def view():
    response = s.get(f"http://{global_host}:8000/ratings/view").json()["view"]
    for item in response:
        print(f'The Rating of {item["professor-title"]} {item["professor-first-name"]}. {item["professor-last-name"]} ({item["module-code"]}) is {"*" * item["average"]}')


def average(prof_code, module_code):
    prof_code = "VS1"
    module_code = "CD1"
    data = {"professor-code": prof_code,
        "module-code": module_code}
    response = s.post(f"http://{global_host}:8000/ratings/average", data=data).json()
    print(f'The rating of {response["professor-title"]} {response["professor-first-name"]}. {response["professor-last-name"]} ({prof_code}) in module {response["module-name"]} ({module_code}) is {"*" * response["average-score"]}')


def rate(prof_code, module_code, year, semester, score):
    prof_code = "VS1"
    module_code = "CD1"
    year = "17"
    semester = "1"
    score = 5
    data = {"professor-code": prof_code,
            "module-code": module_code,
            "year": year,
            "semester": semester,
            "score": score}
    response = s.post(f"http://{global_host}:8000/ratings/rate", data=data).json()
    if response['rate-success']:
        print("Rating submitted")
    else:
        print("Error making rating")


def menu():
    while(True):
        command = input("> ")
        command_split = command.split()
        command_split_len = len(command_split)
        command_name = command_split[0]
        if command_name == "register" and command_split_len == 2:
            global_host = command_split[1]
            register(command_split[1])
        elif command_name == "login" and command_split_len == 4:
            global_host = command_split[1]
            login(command_split[1], command_split[2], command_split[3])
        elif command_name == "logout":
            logout()
        elif command_name == "list":
            list_all()
        elif command_name == "view":
            view()
        elif command_name == "average" and command_split_len == 3:
            average(command_split[1], command_split[2])
        elif command_name == "rate" and command_split_len == 6:
            rate(command_split[1], command_split[2],
                command_split[3], command_split[4], command_split[5])
        elif command_name == "quit":
            print("Quiting...")
            break
        else:
            print("Invalid command")


if __name__ == '__main__':
    global_host = "127.0.0.1"
    s = requests.Session()
    menu()
