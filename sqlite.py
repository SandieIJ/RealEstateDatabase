import sqlite3
from real_estate import Seller, Agent, Buyer, Office, House, Sold, Summary
from datetime import date, datetime


#for testing change value to ":memory" in order to start up from scratch
conn =sqlite3.connect(':memory:')

#cursor will alow us to execute sql commands
c = conn.cursor()

#journaling using write ahead logging
c.execute("PRAGMA journal_mode=wal")

#the limit of logs before files in the wal are written onto disk
c.execute("PRAGMA journal_size_limit=100")

c.execute("""CREATE TABLE sellers(
    id integer PRIMARY KEY AUTOINCREMENT, 
    name text,
    email text,
    contact integer
)""")

conn.commit()

c.execute("""CREATE TABLE agents(
    id integer PRIMARY KEY AUTOINCREMENT, 
    first text,
    last text,
    email text,
    contact integer
)""")

conn.commit()

c.execute("""CREATE TABLE buyers(
    id integer PRIMARY KEY AUTOINCREMENT, 
    name text,
    email text,
    contact integer
)""")

conn.commit()

c.execute("""CREATE TABLE offices(
    id integer PRIMARY KEY AUTOINCREMENT, 
    operationzip integer
)""")

conn.commit()

c.execute("""CREATE TABLE houses(
    id integer PRIMARY KEY AUTOINCREMENT, 
    listingdate date,
    beds integer,
    baths integer,
    listingprice integer, 
    status text,
    housezipcode integer
)""")

conn.commit()

c.execute("""CREATE TABLE soldhouses(
    id integer PRIMARY KEY AUTOINCREMENT,
    sellingagentid integer NOT NULL REFERENCES agents(id),
    houseid integer NOT NULL REFERENCES houses(id),
    sellerid integer NOT NULL REFERENCES seller(id),
    buyerid integer NOT NULL REFERENCES buyer(id),
    saledate date,
    saleprice integer,
    commission decimal(10,2)
)""")

conn.commit()

c.execute("""CREATE TABLE salesummary(
    houseid integer NOT NULL REFERENCES houses(id),
    saleid integer NOT NULL REFERENCES soldhouses(id),
    officeid integer NOT NULL REFERENCES offices(id),
    agentid integer NOT NULL REFERENCES agents(id),
    salelistingdate date NOT NULL REFERENCES houses(listingdate),
    datesold date NOT NULL REFERENCES soldhouses(saleprice), 
    housezip integer NOT NULL REFERENCES houses(housezipcode) ,
    housesaleprice integer NOT NULL REFERENCES soldhouses(saleprice)
)""")

conn.commit()

c.execute("""CREATE TABLE wages(
    agentid integer NOT NULL REFERENCES agents(id), 
    saleid integer NOT NULL REFERENCES soldhouses(id),
    house_saleprice integer NOT NULL REFERENCES soldhouses(saleprice),
    house_commission decimal (12,2) NOT NULL REFERENCES soldhouses(commission)
)""")

conn.commit()

sell1 = Seller(1, 'Jane Doe', 'janedoe@gmail.com', 2348760912)
sell2 = Seller(2, 'John Doe', 'johndoe@gmail.com', 1458736087)
sell3 = Seller(3, 'James Doe', 'jamesdoe@gmail.com', 6091096320)
sell4 = Seller(4, 'Jasmin Doe', 'jasmindoe@gmail.com', 2133042960)
sell5 = Seller(5, 'Janet Doe', 'janetdoe@gmail.com', 9876091917)
sell6 = Seller(6, 'Joel Doe', 'joeldoe@gmail.com', 8766187200)
sell7 = Seller(7, 'Jesus Doe', 'jesusdoe@gmail.com', 6406971802)

c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell1.sellerid, sell1.name, sell1.email, sell1.contact))
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell2.sellerid, sell2.name, sell2.email, sell2.contact)) 
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell3.sellerid, sell3.name, sell3.email, sell3.contact)) 
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell4.sellerid, sell4.name, sell4.email, sell4.contact)) 
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell5.sellerid, sell5.name, sell5.email, sell5.contact))
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell6.sellerid, sell6.name, sell6.email, sell6.contact)) 
c.execute("INSERT INTO sellers VALUES (?, ?, ?, ?)", (sell7.sellerid, sell7.name, sell7.email, sell7.contact))

conn.commit()

ag1 = Agent(1001, 'Sam', 'Smith', 9873108613)
ag2 = Agent(1002, 'Tanya', 'Fowler', 8502470679)
ag3 = Agent(1003, 'Carey', 'Johnson', 8502298201)
ag4 = Agent(1004, 'Mike', 'Okunwu', 2136060331)
ag5 = Agent(1005, 'Sheila', 'August', 3307650003)
ag6 = Agent(1006, 'Smiley', 'Montana', 6508618983)
ag7 = Agent(1007, 'Zheng', 'Montoya', 4153104443)

c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag1.agentid, ag1.first, ag1.last, ag1.contact, ag1.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag2.agentid, ag2.first, ag2.last, ag2.contact, ag2.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag3.agentid, ag3.first, ag3.last, ag3.contact, ag3.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag4.agentid, ag4.first, ag4.last, ag4.contact, ag4.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag5.agentid, ag5.first, ag5.last, ag5.contact, ag5.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag6.agentid, ag6.first, ag6.last, ag6.contact, ag6.staffemail))
c.execute("INSERT INTO agents VALUES(?, ?, ?, ?, ?)", (ag7.agentid, ag7.first, ag7.last, ag7.contact, ag7.staffemail))

conn.commit()

buy1 = Buyer(2001, 'Carol Garcia', 'carlog@gmail.com', 2098762201)
buy2 = Buyer(2002, 'Mike Scott', 'mikescott@email.com', 9107629033)
buy3 = Buyer(2003, 'Chanel Iman', 'chanel@email.com', 2237293007)
buy4 = Buyer(2004, 'Colin Cowe', 'cowcolin@gmail.com', 5708821010)
buy5 = Buyer(2005, 'Jimmy Butler', 'jimmybut@email.com', 4809090212)
buy6 = Buyer(2006, 'Alex Caruso', 'alexcaruso@email.com', 6650298133)
buy7 = Buyer(2007, 'Jenny Chu', 'jchu@email.com', 3138774020)

c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy1.buyerid, buy1.name, buy1.email, buy1.contact))
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy2.buyerid, buy2.name, buy2.email, buy2.contact)) 
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy3.buyerid, buy3.name, buy3.email, buy3.contact)) 
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy4.buyerid, buy4.name, buy4.email, buy4.contact)) 
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy5.buyerid, buy5.name, buy5.email, buy5.contact))
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy6.buyerid, buy6.name, buy6.email, buy6.contact)) 
c.execute("INSERT INTO buyers VALUES (?, ?, ?, ?)", (buy7.buyerid, buy7.name, buy7.email, buy7.contact))

conn.commit()

of1 = Office(3001, 94108)
of2 = Office(3002, 94607)
of3 = Office(3003, 90210)

c.execute("INSERT INTO offices VALUES(?,?)", (of1.officeid, of1.operationzipcode))
c.execute("INSERT INTO offices VALUES(?,?)", (of2.officeid, of2.operationzipcode))
c.execute("INSERT INTO offices VALUES(?,?)", (of3.officeid, of3.operationzipcode))

conn.commit()


hou1 = House(4001, 2018-12-12, 2, 1, 540000, 'ACTIVE', 94111)
hou2 = House(4002, 2019-1-1, 3, 4, 900000, 'ACTIVE', 94108)
hou3 = House(4003, 2018-11-11, 10, 8, 2300000, 'SOLD', 90210)
hou4 = House(4004, 2019-1-17, 1, 1, 150000, 'ACTIVE', 94607)
hou5 = House(4005, 2018-2-14, 2, 2, 770000, 'SOLD', 90210)
hou6 = House(4006, 2018-9-24, 4, 2, 220000, 'ACTIVE', 94108)
hou7 = House(4007, 2018-6-21, 0, 1, 94000, 'SOLD', 94607)
hou8 = House(4008, 2018-3-12, 2, 1, 400000, 'SOLD', 90210)
hou9 = House(4009, 2019-1-1, 3, 4, 900000, 'ACTIVE', 94108)
hou10 = House(4010, 2018-11-11, 1, 1, 54000, 'SOLD', 94108)
hou11 = House(4011, 2019-3-17, 3, 2, 350000, 'ACTIVE', 94111)
hou12 = House(4012, 2019-2-14, 5, 3, 667000, 'SOLD', 94111)
hou13 = House(4013, 2018-10-18, 4, 2, 220000, 'ACTIVE', 94607)
hou14 = House(4014, 2018-8-10, 4, 4, 946000, 'SOLD', 90210)

c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou1.houseid, hou1.listingdate, hou1.beds, hou1.baths, hou1.listingprice, hou1.status, hou1.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou2.houseid, hou2.listingdate, hou2.beds, hou2.baths, hou2.listingprice, hou2.status, hou2.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou3.houseid, hou3.listingdate, hou3.beds, hou3.baths, hou3.listingprice, hou3.status, hou3.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou4.houseid, hou4.listingdate, hou4.beds, hou4.baths, hou4.listingprice, hou4.status, hou4.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou5.houseid, hou5.listingdate, hou5.beds, hou5.baths, hou5.listingprice, hou5.status, hou5.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou6.houseid, hou6.listingdate, hou6.beds, hou6.baths, hou6.listingprice, hou6.status, hou6.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou7.houseid, hou7.listingdate, hou7.beds, hou7.baths, hou7.listingprice, hou7.status, hou7.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou8.houseid, hou8.listingdate, hou8.beds, hou8.baths, hou8.listingprice, hou8.status, hou8.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou9.houseid, hou9.listingdate, hou9.beds, hou9.baths, hou9.listingprice, hou9.status, hou9.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou10.houseid, hou10.listingdate, hou10.beds, hou10.baths, hou10.listingprice, hou10.status, hou10.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou11.houseid, hou11.listingdate, hou11.beds, hou11.baths, hou11.listingprice, hou11.status, hou11.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou12.houseid, hou12.listingdate, hou12.beds, hou12.baths, hou12.listingprice, hou12.status, hou12.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou13.houseid, hou13.listingdate, hou13.beds, hou13.baths, hou13.listingprice, hou13.status, hou13.housezipcode))
c.execute("INSERT INTO houses VALUES(?, ?, ?, ?, ?, ?, ?)", (hou14.houseid, hou14.listingdate, hou14.beds, hou14.baths, hou13.listingprice, hou14.status, hou14.housezipcode))

conn.commit

sol1 = Sold(5001, 1002, 4003, 2, 2001, 2019-1-11, 23240000)
sol2 = Sold(5002, 1004, 4007, 5, 2007, 2018-8-14, 97000)
sol3 = Sold(5003, 1004, 4008, 7, 2002, 2018-10-12, 390000)
sol4 = Sold(5004, 1006, 4005, 1, 2005, 2018-12-10, 75000)
sol5 = Sold(5005, 1003, 4010, 6, 2004, 2018-12-14, 55000)
sol6 = Sold(5006, 1001, 4012, 4, 2003, 2019-3-17, 662000)
sol7 = Sold(5007, 1001, 4014, 2, 2006, 2019-1-10, 950000)


c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol1.saleid, sol1.agentid, sol1.houseid, sol1.sellerid, sol1.buyerid, sol1.saledate, sol1.saleprice, sol1.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol2.saleid, sol2.agentid, sol2.houseid, sol2.sellerid, sol2.buyerid, sol2.saledate, sol2.saleprice, sol2.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol3.saleid, sol3.agentid, sol3.houseid, sol3.sellerid, sol3.buyerid, sol3.saledate, sol3.saleprice, sol3.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol4.saleid, sol4.agentid, sol4.houseid, sol4.sellerid, sol4.buyerid, sol4.saledate, sol4.saleprice, sol4.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol5.saleid, sol5.agentid, sol5.houseid, sol5.sellerid, sol5.buyerid, sol5.saledate, sol5.saleprice, sol5.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol6.saleid, sol6.agentid, sol6.houseid, sol6.sellerid, sol6.buyerid, sol6.saledate, sol6.saleprice, sol6.commission))
c.execute("INSERT INTO soldhouses VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sol7.saleid, sol7.agentid, sol7.houseid, sol7.sellerid, sol7.buyerid, sol7.saledate, sol7.saleprice, sol7.commission))

conn.commit

sum1 = Summary(4003, 5001, 3001, 1002, 2018-11-11, 2019-1-11, 90210, 23240000)
sum2 = Summary(4007, 5002, 3003, 1004, 2018-6-21, 2018-8-14, 94607, 97000)
sum3 = Summary(4008, 5003, 3002, 1004, 2018-3-12, 2018-10-12, 90210, 390000)
sum4 = Summary(4005, 5004, 3002, 1006, 2018-2-14, 2018-12-10, 90210, 75000)
sum5 = Summary(4010, 5005, 3001, 1003, 2018-11-11, 2018-12-14, 94108, 55000)
sum6 = Summary(4012, 5006, 3003, 1001, 2019-2-14, 2019-3-17, 94111, 662000)
sum7 = Summary(4014, 5007, 3003, 1001, 2018-8-10, 2019-1-10, 90210, 950000)

c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum1.houseid, sum1.saleid, sum1.officeid, sum1.agentid, sum1.listingdate, sum1.saledate, sum1.housezipcode, sum1.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum2.houseid, sum2.saleid, sum2.officeid, sum2.agentid, sum2.listingdate, sum2.saledate, sum2.housezipcode, sum2.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum3.houseid, sum3.saleid, sum3.officeid, sum3.agentid, sum3.listingdate, sum3.saledate, sum3.housezipcode, sum3.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum4.houseid, sum4.saleid, sum4.officeid, sum4.agentid, sum4.listingdate, sum4.saledate, sum4.housezipcode, sum4.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum5.houseid, sum5.saleid, sum5.officeid, sum5.agentid, sum5.listingdate, sum5.saledate, sum5.housezipcode, sum5.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum6.houseid, sum6.saleid, sum6.officeid, sum6.agentid, sum6.listingdate, sum6.saledate, sum6.housezipcode, sum6.saleprice))
c.execute("INSERT INTO salesummary VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (sum7.houseid, sum7.saleid, sum7.officeid, sum7.agentid, sum7.listingdate, sum7.saledate, sum7.housezipcode, sum7.saleprice))


#c.execute("SELECT * FROM salesummary")
#print(c.fetchall())

#Find the average price of the sales for a particular month
#Write the day input in the form YYYY-MM
def avgsaleprice(day):
    c.execute("SELECT AVG(saleprice) FROM soldhouses WHERE saledate LIKE 'day%'")
    return c.fetchall()

#find the top 5 agents by number of sales
def topagents():
    c.execute("SELECT agents.id, agents.first, agents.last, agents.contact, COUNT(soldhouses.saleprice) AS NumberofSales FROM soldhouses, agents WHERE agents.id = soldhouses.sellingagentid GROUP BY agents.id ORDER BY NumberofSales DESC LIMIT 5")
    return c.fetchall()

#Find the commission of each agent & store it in the table.
#This function takes in the values for every entry that will be inserted in the soldhouses table hence the sol prefix
def wages(solx):
    c.execute("INSERT INTO wages VALUES (?, ?, ?, ?)", (solx.sellingagentid, solx.id, solx.saleprice, solx.commission))
    return c.fetchall()

#this function finds the top 5 offices with the most sales for that month
def topoffices():
    c.execute("SELECT offices.id, COUNT(salesummary.housesaleprice) AS NumberofHouseSales FROM salesummary, offices WHERE offices.id = salesummary.officeid GROUP BY office.id ORDER BY NumberofHouseSales DESC LIMIT 5")
    return c.fetchall()

def topzipcodes():
    c.execute("SELECT salesummary.houseszipcode, AVG(soldhouses.saleprice) AS AverageSales FROM soldhouses, salesummary WHERE soldhouses.id = salesummary.saleid GROUP BY salesummary.houseszipcode ORDER BY AverageSales DESC LIMIT 5")
    return c.fetchall()


#closes the database connection
conn.close()

