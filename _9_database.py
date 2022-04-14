'''
pymysql package needs to be installed
--> sudo apt-get install python3-pip
--> sudo pip3 install pymysql
'''

import pymysq
db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
cur = db.cursor()
class MyDatabase:
    #def create(self):
        #db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        #self.cur.execute("Create database mca044")
        #print("Data base has been created")
    def display(self):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        cur.execute("Show databases")
        for db in cur:
            print(db)
    def create(self):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        cur.execute("Create table emp(name varchar(20),slno int(20),address varchar(20),empcode varchar(20),dob int(20),age int(20),mobile int(20),status varchar(20),designation varchar(20))")
        print("Table has been created")
    def showtable(self):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        print("The table created is : ")
        cur.execute("Describe table emp")
        cur.execute("Show tables")
        for self.tb in cur:
            print(self.tb)
    def insert(self):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        self.sqlform = "Insert into emp(name,slno,address,empcode,dob,age,mobile,status,designation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.employee = [("akash",101,"bangalore","i101",1303300,21,1721737,"single","manager"),("akash",102,"bangalore","i101",1333000,21,1722375,"single","manager"),("akash",103,"bangalore","i101",1303300,21,17217237,"single","manager"),("akash",104,"bangalore","i101",1344440,21,17271237,"single","manager"),("akash",105,"bangalore","i101",13044440,21,17571237,"single","manager"),("akash",106,"bangalore","i101",13066660,21,1721737,"single","manager")]
        cur.executemany(self.sqlform, self.employee)
        db.commit()
        print("Values have been inserted")
    def displaytable(self):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        print("Contents that are in the table are")
        cur.execute("Select * from emp")
        self.result = cur.fetchall()
        for self.row in self.result:
            print(self.row)
    def delete(self,slno):
        #self.db = pymysql.connect(host='172.16.34.105',user='mca044',passwd='mca044',database='mca044')
        #self.cur = self.db.cursor()
        self.sql = "Delete from emp where slno = '%s'"%(int(slno))
        cur.execute(self.sql)
        db.commit()
        print("Record has been deleted")
    def droptable(self):
        self.delt = "Drop table emp"
        cur.execute(self.delt)
        db.commit()
        print("table has been dropped")
    def describe(self):
        print("table structure of emp is : ")
        self.desc = "desc emp"
        cur.execute(self.desc)
        for self.de in cur:
            print(self.de)
data = MyDatabase()
while True:
    print("\n1.DISPLAY DATABASE \n2.CREATE TABLE \n3.DISPLAY TABLE AND STRUCTURE \n4.INSERT VALUES \n5.DISPLAY ALL TABLE CONTENTS \n6.DELETE A RECORD \n7.DROP THE TABLE \n8.TABLE STRUCTURE \n0.EXIT \n\n")
    ch = int(input("Enter your choice : "))
    if ch==1:
        print("------------------------------------------------------------------------------------")
        data.display()
        print("------------------------------------------------------------------------------------")
    elif ch==2:
        print("------------------------------------------------------------------------------------")
        data.create()
        print("------------------------------------------------------------------------------------")
    elif ch==3:
        print("------------------------------------------------------------------------------------")
        data.showtable()
        print("------------------------------------------------------------------------------------")
    elif ch==4:
        print("------------------------------------------------------------------------------------")
        data.insert()
        print("------------------------------------------------------------------------------------")
    elif ch==5:
        print("------------------------------------------------------------------------------------")
        data.displaytable()
        print("------------------------------------------------------------------------------------")
    elif ch==6:
        print("------------------------------------------------------------------------------------")
        sl = int(input("Enter the serial no. that to be deleted from DB : "))
        data.delete(sl)
        print("------------------------------------------------------------------------------------")
    elif ch==7:
        print("------------------------------------------------------------------------------------")
        data.droptable()
        print("------------------------------------------------------------------------------------")
    elif ch==8:
        print("------------------------------------------------------------------------------------")
        data.describe()
        print("------------------------------------------------------------------------------------")
    elif ch==0:
        exit()
    else:
        print("------------------------------------------------------------------------------------")
        print("That is a wrong choice")
        print("------------------------------------------------------------------------------------")
