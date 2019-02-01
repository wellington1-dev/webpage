class User:
    def_init_(self, name, email):
        self.name = name 
        self.email = email
        self.logged = True
    def login(self):
        self.logged=True
        print(self.name + "is logged in.")
        return self
    def logout(self):
        self.logged = False
        print(self.name + " is logged in")
        return self
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}.")
        return self
new_user = User("Anna","anna@anna.com")
print(new_user.email)
    