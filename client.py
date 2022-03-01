import requests
import json
import sys


def register():
    """
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    """
    username = "user4"
    password = "password123"
    email = "email@email.com"
    response = s.post("http://127.0.0.1:8000/ratings/register",
                        data={'username': username, 'password': password, 'email': email}).json()
    print(response)


def login():
    """
    username = input("Username: ")
    password = input("Password: ")
    """
    username = "user4"
    password = "password123"
    response = s.post("http://127.0.0.1:8000/ratings/login",
                        data={'username': username, 'password': password})
    print(response.json())


def logout():
    response = s.post("http://127.0.0.1:8000/ratings/logout")
    print(response.json())


def list_all():
    response = s.get("http://127.0.0.1:8000/ratings/list").json()
    response = response["list"]
    for item in response:
        print("\nModule information")
        print(f'Code: {item["module__module__code"]} Name: { item["module__module__name"]} Year: 20{item["module__year"]} Semester: {item["module__semester"]}')
        print("Taught by")
        codes = item["professor__code"].split()
        titles = item["professor__title"].split()
        first_names = item["professor__first_name"].split()
        last_names = item["professor__last_name"].split()

        for i in range(len(codes)):
            print(f'({codes[i]}) {titles[i]} {first_names[i]}. {last_names[i]}')
        print("-" * 70)

def view():
    response = s.get("http://127.0.0.1:8000/ratings/view").json()["view"]
    print(f'The Rating of {response["professor-title"]} {response["professor-first-name"]}. {response["professor-last-name"]} ({response["module-code"]}) is {"*" * response["average"]}')

def average():
    prof_code = "VS1"
    module_code = "CD1"
    #prof_code = input("Professor code")
    #module_code = input("Module code")

    response = s.post("http://127.0.0.1:8000/ratings/average", data = {"professor-code": prof_code, "module-code": module_code}).json()
    print(f'The rating of {response["professor-title"]} {response["professor-first-name"]}. {response["professor-last-name"]} ({prof_code}) in module {response["module-name"]} ({module_code}) is {"*" * response["average-score"]}')

def menu():
    while(True):
        print("1 - Register")
        print("2 - Login")
        print("3 - Logout")
        print("4 - List")
        print("5 - View")
        print("6 - Average")
        print("7 - Rate")
        print("Q - Quit")

        choice = input("Pick an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            list_all()
        elif choice == "5":
            view()
        elif choice == "6":
            average()
        elif choice == "Q":
            print("Quiting...")
            break
        else:
            print("Pick a valid option")


if __name__ == '__main__':
    s = requests.Session()
    menu()
