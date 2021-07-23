from models import Member


# login
class login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):
        # print (self.id)
        if self.id == id and self.pas == pas:
            print ("Login success!")
        else:
            print ("Login error!")
# login
# admin
# log = login("admin", "admin")
# # log = login("user","user")
# log.check(input("Enter Login ID:"),input("Enter password:"))
       

class register:
    pass

class showAll:
    def showAll():

        db = Member.getAll()
        return db 
   

    




