import json
# import requests


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
        # return ("%s %s" % (self.first_name,self.last_name))
    
    @classmethod
    def getAll(self):
        with open("member.json", "r") as read_file:
            json_list = json.load(read_file)
        result = []    
        for item in json_list.values():

            item = json.load(item)
            person = Member(item['first_name'], item['last_name'])
            result.append(person)
        return result
   

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



# person =Member(1,"Zahra","farrokhi","222","teh")
