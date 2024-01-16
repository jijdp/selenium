

class LoginPage:

    def __init__(self, secret):
        self.secret = secret

    def login(self, username, password):
        return username + " --- " + password
    
    def loginWithSecret(self, username, password):
        return username + " ----- " + password + self.secret
    
l = LoginPage("$$$$$$")
print(l.login("admin", "password"))

print(l.loginWithSecret("supervisor", "superpass"))