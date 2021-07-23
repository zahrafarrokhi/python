class Menu:
    list = []

    def __init__(self, v_id, price, mojoodi):
        self.id = v_id
        self.price = price
        self.mojoodi = mojoodi


class Food(Menu):
    food_kinds = ['piza', 'pasta']

    def __init__(self, v_id, price, kind, mojoodi):
        super().__init__(v_id, price, mojoodi)
        if kind not in self.food_kinds:
            raise Exception('wrong food')
        self.kind = kind

    def __str__(self):
        return '{}{}{}'.format(self.id, self.price, self.kind)


class Member:
    def __init__(self,user_id,first_name, last_name,tel, address):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.address = address
        self.pastbuy = []
        self.cart_list = []

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def add_to_cart(self, kala_id):
        self.cart_list.append(kala_id)
        for i in Food.list:
            if i.id == kala_id:
                i.mojoodi -= 1


class Admin(Member):
    
    def __init__(self, user_id, first_name, last_name,tel, address):
        super(Admin, self).__init__(user_id,first_name, last_name,tel, address)
        self.kala_list = []

    def add_kala(self, **kwargs):
        kala = Food(**kwargs)
        self.kala_list.append(kala)
        kala.list.append(kala)
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


# run
person =Member(1,"Zahra","farrokhi","222","teh")
print(person.first_name,person.last_name)
# print(person.name,person.teh)  
# *******************
# login
# admin
log = login("admin", "admin")
# log = login("user","user")
log.check(input("Enter Login ID:"),input("Enter password:"))
       
# **********************
admin = Admin(2, 'zahra','farrokhi','555','teh')
admin.add_kala(**{'v_id': 1, 'price': 2500, 'kind': 'piza', 'mojoodi': 10})
person.add_to_cart(1)
print(admin.kala_list[0].mojoodi)

