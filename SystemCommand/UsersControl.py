import re
import csv


class AuthInSystem:

    def response_from_users_db(self):

        with open("DB_dir/users.csv", "r") as users_list:
            reader = dict(csv.reader(users_list))
            if len(reader) >= 2:
                return reader
            else:
                return ">>No users found. Create new"

    def password_verification(self):
        pass

    def request_from_users_page(self):
        pass

    def user_create(self):

        while True:

            new_users_login = input(">>Enter login for new user: ")

            if new_users_login == "quit":
                return "quit"

            try:
                assert len(list(new_users_login)) <= 20
                response_check_login = self.check_login(new_users_login)
                if response_check_login == 0:
                    continue
                elif response_check_login == 1:

                    return new_users_login
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