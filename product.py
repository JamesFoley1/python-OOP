class Product:
    def __init__(self, price, item_name, weight, brand, status, tax=1, reason_for_return = "none"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.tax = tax
        self.reason_for_return = reason_for_return

    def sell(self):
        self.status = "sold"
        return self
    
    def addTax(self, tax):
        self.tax = (self.price * tax) + self.price
        return self
    
    def returnItems(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        return self
    
    def displayAll(self):
        print("Price: $"+str(self.price))
        print("Item: "+str(self.item_name))
        print("Weight: "+str(self.weight)+" lbs.")
        print("Brand: "+str(self.brand))
        print("Status: "+str(self.status))
        if self.tax != 1:
            print("Price with tax: $"+str(self.tax))
        if self.reason_for_return != "none":
            print("Reason for return: "+str(self.reason_for_return))
        return self

    
# product1 = Product( 1000, "laptop", 2.2, "Acer", "for sale")
# product1.displayAll()

# product2 = Product( 1000, "laptop", 2.2, "Acer", "for sale")
# product2.sell().addTax(.10).displayAll()

product3 = Product( 2000, "Office Desk", 65, "IKEA", "for sale")
product3.returnItems("defective")
product3.displayAll()
