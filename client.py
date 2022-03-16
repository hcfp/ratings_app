import requests


def register():
    host = input("Host: ")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    print(host)
    response = s.post(f"http://{host}/ratings/register",
                      data={'username': username, 'password': password, 'email': email}).json()
    print(response)


def login(host):
    username = input("Username: ")
    password = input("Password: ")
    response = s.post(f"http://{host}/ratings/login",
                      data={'username': username, 'password': password}).json()
    if response["login-success"]:
        print("Logged in")
    else:
        print("Login failed")


def logout(host):
    response = s.post(f"http://{host}/ratings/logout").json()
    if response["logout-success"]:
        print("Logged out")
    else:
        print("Logout failed")


def list_all(host):
    response = s.get(f"http://{host}/ratings/list").json()["list"]
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


def view(host):
    response = s.get(f"http://{host}/ratings/view").json()["view"]
    for item in response:
        print(f'The Rating of {item["professor-title"]} {item["professor-first-name"]}. {item["professor-last-name"]} ({item["module-code"]}) is {"*" * item["average"]}')


def average(host, prof_code, module_code):
    data = {"professor-code": prof_code,
        "module-code": module_code}
    response = s.post(f"http://{host}/ratings/average", data=data).json()
    print(f'The rating of {response["professor-title"]} {response["professor-first-name"]}. {response["professor-last-name"]} ({prof_code}) in module {response["module-name"]} ({module_code}) is {"*" * response["average-score"]}')


def rate(host, prof_code, module_code, year, semester, score):
    data = {"professor-code": prof_code,
            "module-code": module_code,
            "year": year,
            "semester": semester,
            "score": score}
    response = s.post(f"http://{host}/ratings/rate", data=data).json()
    if response['rate-success']:
        print("Rating submitted")
    else:
        print("Error making rating")


def menu():
    host = ""
    while(True):
        command = input("> ")
        command_split = command.split()
        command_split_len = len(command_split)
        command_name = command_split[0]
        if command_name == "register" and command_split_len == 1:
            register()
        elif command_name == "login" and command_split_len == 2:
            host = command_split[1]
            login(host)
        elif command_name == "logout":
            logout(host)
        elif command_name == "list":
            list_all(host)
        elif command_name == "view":
            view(host)
        elif command_name == "average" and command_split_len == 3:
            average(host, command_split[1], command_split[2])
        elif command_name == "rate" and command_split_len == 6:
            rate(host, command_split[1], command_split[2],
                command_split[3], command_split[4], command_split[5])
        elif command_name == "quit":
            print("Quiting...")
            break
        else:
            print("Invalid command")

def instructions():
    BOLD = '\033[1m'
    END = '\033[0m'
    print(BOLD + "register" + END)
    print(BOLD + "login" + END + " host")
    print(BOLD + "logout" + END)
    print(BOLD + "list" + END)
    print(BOLD + "view" + END)
    print(BOLD + "average" + END + " professor_id module_code")
    print(BOLD + "rate" + END + " professor_id module_code year semester rating")


if __name__ == '__main__':
    s = requests.Session()
    instructions()
    menu()
