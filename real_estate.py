class Seller:

    def __init__(self,sellerid, name, email, contact):
        self.sellerid = sellerid
        self.name = name
        self.email = email
        self.contact = contact

    def __repr__(self):
        return "Seller('{}','{}','{}', '{}')".format(self.sellerid, self.name, self.email, self.contact)

class Agent:

    def __init__(self, agentid, first, last, contact):
        self.agentid = agentid
        self.first = first
        self.last = last
        self.contact = contact

    @property
    def staffemail(self):
        return "{}.{}@realestatemail.com".format(self.first, self.last) 

    def __repr__(self):
        return "Agent('{}','{}','{}','{}', '{}')".format(self.agentid, self.first, self.last, self.contact, self.staffemail)

class Buyer:

    def __init__(self,buyerid, name, email, contact):
        self.buyerid = buyerid
        self.name = name
        self.email = email
        self.contact = contact
    
    def __repr__(self):
        return "Buyer('{}','{}','{}', '{}')".format(self.buyerid, self.name, self.email, self.contact)

class Office:

    def __init__(self, officeid, operationzipcode):
        self.officeid = officeid
        self.operationzipcode = operationzipcode
    
    def __repr__(self):
        return "Office('{}','{}')".format(self.officeid, self.operationzipcode)

class House:

    def __init__(self, houseid, listingdate, beds, baths, listingprice, status, housezipcode):
        self.houseid = houseid
        self.listingdate = listingdate
        self.beds = beds
        self.baths = baths
        self.listingprice = listingprice
        self.status = status
        self.housezipcode = housezipcode

    def __repr__(self):
        return "House('{}','{}','{}','{}','{}','{}')".format(self.houseid, self.listingdate, self.beds, self.baths, self.listingprice, self.status)

class Sold:

    def __init__(self, saleid, agentid, houseid, sellerid, buyerid, saledate, saleprice):
        self.saleid = saleid
        self.agentid = agentid
        self.houseid = houseid
        self.sellerid = sellerid
        self.buyerid = buyerid
        self.saledate = saledate
        self.saleprice = saleprice
    
    @property
    def commission(self):
        if self.saleprice < 100000:
            return 0.1*self.saleprice
        elif self.saleprice < 200000:
            return 0.075*self.saleprice
        elif self.saleprice < 500000:
            return 0.06*self.saleprice
        elif self.saleprice < 1000000:
            return 0.05*self.saleprice
        else:
            return 0.04*self.saleprice
    
    def __repr__(self):
        return "Sold('{}','{}','{}','{}', '{}','{}','{}', '{}')".format(self.saleid, self.agentid, self.houseid, self.sellerid, self.buyerid, self.saledate, self.saleprice, self.commission)

class Summary:

    def __init__(self, houseid, saleid, officeid, agentid, listingdate, saledate, housezipcode, saleprice):
        self.houseid = houseid
        self.saleid = saleid
        self.officeid = officeid
        self.agentid = agentid
        self.listingdate = listingdate
        self.saledate = saledate
        self.housezipcode = housezipcode
        self.saleprice = saleprice
    
    def __repr__(self):
        return "Summary('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.houseid, self.saleid, self.officeid, self.agentid, self.listingdate, self.saledate, self.housezipcode, self.saleprice)
