class Smartphone:
    
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def sayBrand(self):
           print("бренд:", self.brand)
    
    def sayModel(self):
           print("модель:", self.model)
    
    def sayNumber(self):
            print("номер телефона:", self.number)
