class Customer:
    def __init__(self, name, unitsconsumed):
        self.name = name
        self.unitsconsumed = unitsconsumed

    def calculatebill(self, rate=0.1):
        self.rate = rate
        return self.unitsconsumed * self.rate

    def displaybill(self, bill):
        print(self.name, "- your electricity bill is:", bill)


class Residentialcustomer(Customer):
    def __init__(self, name, unitsconsumed, familymems):
        super().__init__(name, unitsconsumed)
        self.familymems = familymems

    def calculatebill(self, rate=0.08):
        discountmem = 0.02
        discountrate = rate - (self.familymems * discountmem)
        bill = super().calculatebill(discountrate)
        super().displaybill(bill)


class Commercialcustomer(Customer):
    def __init__(self, name, unitsconsumed, businesstype):
        super().__init__(name, unitsconsumed)
        self.businesstype = businesstype

    def calculatebill(self, rate=0.12):
        if self.businesstype == "small":
            dis = 0.1
        else:
            dis = 0
        if self.businesstype == "large":
            surcharge = 0.1
        else:
            surcharge = 0

        adjrate = rate * (1 - dis + surcharge)
        bill = super().calculatebill(adjrate)
        super().displaybill(bill)


res = Residentialcustomer("Arya", 200, 3)
res.calculatebill()

com = Commercialcustomer("Amal", 500, "large")
com.calculatebill()
