class Product:
    _price = 50000

    @property
    def getting_price(self):
        return self._price
    
    @getting_price.setter
    def setting_price(self, new_price):
        self._price = new_price
    
    @getting_price.deleter
    def deleting_price(self):
        print("Deleting the Price...")


get_price = Product()
print(get_price.getting_price)
user_price = int(input("New Price: "))
get_price.setting_price = user_price
print(get_price.setting_price)
del get_price.deleting_price
