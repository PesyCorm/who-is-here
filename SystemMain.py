# class Desktop:

# 	def dir_01(self):
# 		return "files in dir_01"

# 	def dir_02(self):
# 		return "files in dir_02"

# 	def dir_03(self):
# 		return "files in dir_03"


# desktop_directory = {"dir_01": Desktop().dir_01(), "dir_02": Desktop().dir_02(), "dir_03": Desktop().dir_03()}
from .SystemCommand import help_response
import re


def dir_db_request(request):

    if request == "users_list":
        with open("users.txt", "r") as users_list:
            if users_list.read() == "" or " ":
                return "No users found. Create new"
            else:
                return users_list.read()

class AuthInSystem:

    def user_create(self):

        while True:

            new_users_login = input("Enter login for new user: ")

            if new_users_login == "quit":
                pass

            try:
                assert len(list(new_users_login)) <= 20
                response_check_login = self.check_login(new_users_login)
                if response_check_login == 0:
                    continue
                elif response_check_login == 1:
                    break
            except:
                print("Login length must not exceed 20 characters\nTry again")


    def check_login(self, new_users_login):

        pattern = re.compile("[a-zA-Z0-9]")
        for word in new_users_login:

            if pattern.match(word):
                print("Login OK")
                return 1
            else:
                print("Login can include letters a-z, A-Z and numbers 0-9\nTry again")
                return 0


if __name__ == "__main__":

    users_list_response = dir_db_request("users_list")
    print(users_list_response)
    if "No users found" in users_list_response:
        AuthInSystem().user_create()
    else:
        user = input("Select an available user:")

while True:

    request = input("--")

    if request[0:2] == "cd ": #??????????????????????????????????

        try:
            split_request = request.split(" ")

            if len(split_request) == 2:

                try:
                    response = desktop_directory[split_request[1]]
                    print("\n>>", response, "\n")

                except:
                    print("directory not found. try again or enter 'help'")

            else:
                print("directory not found. try again or enter 'help'")

        except:
            print("directory not found. try again or enter 'help'")

    elif "help" in request:
        print(help_response())

    elif "quit" in request:
        break

    else:
        print("unexpected request. try again or enter 'help'")
