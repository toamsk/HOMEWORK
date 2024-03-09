
class User:
    
    def __init__(self, first_name, last_name):
        self.firstn = first_name
        self.lastn = last_name
        
    def sayName(self):
        print("меня зовут:", self.firstn)
    
    def saySurname(self):
        print("моя фамилия:", self.lastn)
    
    def sayPerson(self):
        print("мои имя и фамилия:", self.firstn, self.lastn)