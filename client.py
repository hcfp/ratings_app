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
    data = response["list"]

    combined_names_data = []
    combined_names_data.append(data[0])
    del data[0]
    for item in data:
        is_unique = True
        for combined in combined_names_data:
            if combined["professor__code"] != item["professor__code"] and item["module__module__code"] == combined["module__module__code"] and item["module__module__name"] == combined["module__module__name"] and item["module__year"] == combined["module__year"]:
                combined["professor__code"] += " " + item["professor__code"]
                combined["professor__title"] += " " + item["professor__title"]
                combined["professor__first_name"] += " " + item["professor__first_name"]
                combined["professor__last_name"] += " " + item["professor__last_name"]
                is_unique = False
        if is_unique:
            combined_names_data.append(item)


    for item in combined_names_data:
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
    response = s.get("http://127.0.0.1/ratings/view").json()

def menu():
    while(True):
        print("1: Register")
        print("2: Login")
        print("3 : Logout")
        print("4 : List")
        print("Q: Quit")

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
        elif choice == "Q":
            print("Quiting...")
            break
        else:
            print("Pick a valid option")


if __name__ == '__main__':
    s = requests.Session()
    menu()
