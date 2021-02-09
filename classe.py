class User:

    def __init__(self):
        self.username = "Delphine" # public property by default
        self.__password= "secret" # private property

    def say_hello(self):
        print("Salut à tous")

    def display_password(self):
        print(self.__password)

class Editor:
    def write_article(self):
        print("article ecrit")


class Admin(User, Editor):# class Admin inherited from User, can use multiple heritage
    def test_method(self):
        self.write_article()


my_user = User() # instantiate class User for use property user
my_user.say_hello()
print(my_user.username)
my_user.display_password()

