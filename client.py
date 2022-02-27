import requests
def register():
    """
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    """
    username = "user2"
    password = "password"
    email = "email@email.com"
    response = requests.post("http://127.0.0.1:8000/ratings/register", json = {'username' : username, 'password' : password, 'email' : email}).json()
    print(response)

def menu():
    print("1: Register")
    choice = input("Pick an option: ")
    if choice == 1:
        register()

if __name__ == '__main__':
    register()