class Snack:
    snack_dict = {'biskuit': 6000, 'chips': 8000, 'oreo':10000, "tango": 12000, 'cokelat': 15000}
    stock_dict = {'biskuit': 5, 'chips': 4, 'oreo': 7, "tango": 6, 'cokelat': 1}
    money = [2000, 5000, 10000, 20000, 50000]

    def __init__(self, snack_name, payment, total_item):
        self.name = snack_name
        self.price = payment
        self.total = total_item
    
    def show(self):
        for key, value in Snack.stock_dict.items():
            if key == self.name and value > 0:
                for key, value in Snack.snack_dict.items():
                    if self.price in Snack.money:
                        changes = self.price - value
                        if key == self.name:
                            # break
                            print(f"You buy a {self.name} with {self.price}\nChanges: {changes}")
            elif key == self.name and value < 0:
                print(f"{self.name} is empty")
                
                                
        if not self.price in Snack.money:
            print("Vending Machine cannot accept these type of money")
           

buy_snack = Snack("biskuit", 20000, 1)
buy_snack.show()
