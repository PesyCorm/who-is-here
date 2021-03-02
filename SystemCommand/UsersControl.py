import re
import csv


class AuthInSystem:

    def response_from_users_db(self):

        with open("DB_dir/users.csv", "r") as users_list:
            reader = dict(csv.reader(users_list))
            counter = 0

            if len(reader) >= 2:

                for el in list(reader):

                    if "name" in el or "None" in el:
                        continue
                    counter += 1

                if counter > 0:
                    return reader
                return "<<No users found. Create new"

            else:
                return "<<No users found. Create new"

    def request_from_users_page(self, text):

        with open("DB_dir/users.csv", "r") as users_list:
            reader = dict(csv.reader(users_list))

            if "new user" in text:
                new_user_login = self.user_create()

    def check_availability_in_db(self):
        pass

    def password_verification(self):
        pass

    def activ_user(self):
        pass

    def user_create(self):

        while True:

            new_user_login = input("<<Enter login for new user: ")

            if new_user_login == "quit":
                return "quit"
            elif self.check_user_log_or_pass(new_user_login):
                break

        while True:

            new_user_password = input("<<Enter password for new user: ")

            if new_user_password == "quit":
                return "quit"
            elif self.check_user_log_or_pass(new_user_password):
                break

        self.add_user_to_db(new_user_login, new_user_password)

    def check_user_log_or_pass(self, new_user_login):

        try:
            assert len(list(new_user_login)) <= 20
            pattern = re.compile("[a-zA-Z0-9]")

            for word in new_user_login:

                if pattern.match(word):
                    return 1
                else:
                    print("Login can include letters a-z, A-Z and numbers 0-9. Try again")
                    return 0

        except:
            print("Login length must not exceed 20 characters. Try again")
            return 0

    def add_user_to_db(self, new_user_login, new_user_password):
        pass

    def rm_user_from_db(self):
        pass