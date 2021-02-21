# class Desktop:

# 	def dir_01(self):
# 		return "files in dir_01"

# 	def dir_02(self):
# 		return "files in dir_02"

# 	def dir_03(self):
# 		return "files in dir_03"


# desktop_directory = {"dir_01": Desktop().dir_01(), "dir_02": Desktop().dir_02(), "dir_03": Desktop().dir_03()}
from SystemCommand import help_response, \
                            AuthInSystem
from SystemOnOff import SystemWork


if __name__ == "__main__":

    with SystemWork():

        users_list_response = AuthInSystem().response_from_users_db()

        if ">>No users found" in users_list_response:
            user = AuthInSystem().user_create()
            if user == "quit":
                exit()
            user += "_:"
        else:
            print(users_list_response)
            user = input(">>Select an available user:")


        while True:

            request = input(user)

            if len(request) < 3:

                print(">>Unexpected request. try again or enter 'help'")
                continue

            elif request[0:3] == "cd ":

                try:
                    split_request = request.split(" ")

                    if len(split_request) == 2:

                        try:
                            response = desktop_directory[split_request[1]]
                            print("\n>>", response, "\n")

                        except:
                            print(">>Directory not found. try again or enter 'help'")

                    else:
                        print(">>Directory not found. try again or enter 'help'")

                except:
                    print(">>Directory not found. try again or enter 'help'")

            elif "help" in request:
                print(help_response())

            elif "quit" in request:
                break

            else:
                print(">>Unexpected request. try again or enter 'help'")
