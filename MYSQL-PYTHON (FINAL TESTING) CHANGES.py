# aaa=input("Enter the name of Database : ")
aaa = "shop"
from tabulate import tabulate

import mysql.connector
# mydb=mysql.connector.connect(host="localhost", user="root", passwd=" ")
# cur=mydb.cursor()

# cur.execute("Create database {}".format(aaa))




mydb=mysql.connector.connect(host="localhost", user="root", passwd="vardhman")
cur=mydb.cursor()
if mydb.is_connected():
    print("Connected Successfully !!")

cur.execute("create database if not exists shop")



cur.execute("show databases")
for i in cur:
    print(i)


# cur.execute("use database {}".format(aaa))
cur.execute("use shop")


# cur.execute('create table SHOP(ItemNo integer(3), ItemName varchar(30), Quantity integer(5), Price integer(5))')

cur.execute("show tables")
for i in cur:
    print(i)



# ***** FUNCTIONS ***** #

def additem():
    while True:
        print("\nContents in table SHOP")
        a=cur.execute("select Itemno, Itemname, Quantity from Shop")
        cur.execute(a)
        print(tabulate(cur, headers=['Itno', 'Itnm', 'Qty'],tablefmt='psql'))
        # cur.execute("\nSelect Itemno,Itemname from shop ")
        # f=cur.fetchall()
        # for i in f:
        #     print(i)
    
        print("\nADDING RECORDS ...")
        itno=int(input("\nEnter Item Number - "))
        itnm=input("Enter Item Name - ")
        qty=int(input("Enter Quantity - ")) 
        pr=int(input("Enter price - Rs. "))
        cur.execute("insert into shop values( {},'{}',{},{})".format(itno,itnm,qty,pr))
        mydb.commit()
        print("\nRecord Added Successfully !!!")

        abc=input("\nDo you want to Add more Records ? (y/n) - ")
        if abc=='n':
            break

def updateitem():

    print("\nContents in table SHOP")
    a=cur.execute("select Itemno, Itemname from Shop")
    cur.execute(a)
    print(tabulate(cur, headers=['ItemNo','   ItemName   ',], tablefmt='grid'))
    # cur.execute("\nSelect Itemno,Itemname from shop ")
    # f=cur.fetchall()
    # for i in f:
    #     print(i)

    try:
        print("\nUPDATING RECORDS ...")
        print('''\nWhat do you want to Update ? - 
        1. Item Name
        2. Quantity of an Item
        3. Price of an Item''')


        while True:
            
                ch=int(input("\nEnter your Choice - "))
                if ch==1:
                    print("\nUPDATING ITEM NAME...")
                    itemno=int(input("\nEnter Item Number - "))
                    itemnm=input("Enter Updated Item Name - ")
                    cur.execute("update shop set itemname = '{}' where itemno = {}".format(itemnm,itemno))
                    mydb.commit()
                    print("\nRecord Updated Successfully !!!")
            
            
                elif ch==2:
                    print("\nUPDATING QUANTITY...")
                    itemno=int(input("\nEnter Item Number - "))
                    qty=int(input("Enter Updated Quantity - "))
                    cur.execute("update shop set Quantity = {} where itemno = {}".format(qty,itemno))
                    mydb.commit()
                    print("\nRecord Updated Successfully !!!")

                elif ch==3:
                    print("\nUPDATING PRICE...")
                    itemno=int(input("\nEnter Item Number - "))
                    pr=int(input("Enter Updated Price - "))
                    cur.execute("update shop set Price = {} where itemno = {}".format(pr,itemno))
                    mydb.commit()
                    print("\nRecord Updated Successfully !!!")
                
                else:
                    print("Please Enter a Valid Input")
                    break

    except:
        print("Enter Valid Input")

def delitem():
    
    while True:

        print("\nContents in table SHOP")
        a=cur.execute("select * from Shop")
        cur.execute(a)
        print(tabulate(cur, headers=['ItemNo','ItemName','Quantity','Price'],tablefmt='grid'))
        # cur.execute("Select Itemno,Itemname from shop ")
        # f=cur.fetchall()
        # for i in f:
        #     print(i)


        ch=input("\nDo you want to continue to delete a Record ? (y/n) - ")
        if ch == 'y':
            itemno=int(input("\nEnter Item Number - "))
            cur.execute("delete from shop where itemno = {} ".format(itemno))
            mydb.commit()
            print("\nRecord Deleted Successfully !!!")
        
        else:
            print("Thanks!!!")
            break

def inventory():
    print('\n')
    print("Inventory :-\n")
    a=cur.execute("select * from Shop")
    cur.execute(a)
    print(tabulate(cur, headers=['ItemNo','ItemName','Quantity','Price'],tablefmt='grid'))
    
        


# *************************************************************************** #

def stock():
    
    print("\n*** INVENTORY MANAGEMENT ***")
    
    # while True:

    print('''
    1.ADD
    2.UPDATE
    3.DELETE
    4.SHOW INVENTORY''')
            
    ch=int(input("\nEnter your Choice -- "))

    if ch==1 :
        additem()

    elif ch==2:
        updateitem()

    elif ch==3:
        delitem()
        
    elif ch==4:
        inventory()

    else:
        print("\nPlease Enter a Valid Input")
        
    
        

    
def adddata():
    
        name=input("Enter the name of the buyer : ")
        no=int(input("Enter the phone number of the buyer : "))
        y=int(input("Enter number of products : "))
        cur.execute("create table {}(cname varchar (25), cno integer, item varchar(25), itpr integer, itqty integer)".format(name))
        # cur.execute("create table {}( pname varchar(25), pno integer, itname varchar(25), itpr integer, itqu integer)".format(name))
        i=0
        while(i<y):
            
            
            na=input("\nEnter the name of the item : ")
            pr=int(input("Enter the price of the item : "))
            quan=int(input("Enter the quantity of the item : "))
            cur.execute("insert into `{}` values ( '{}',{},'{}',{},{})".format(name,name,no,na,pr,quan))
        
            i=i+1
            cur.execute("Select Quantity from shop where ItemName='{}'".format(na))
            myrecords=cur.fetchall()
            x=myrecords[0][0]
            cur.execute("update shop set Quantity = {} where itemName = '{}'".format(x-1,na))
            mydb.commit()
             
        print("Records Added!!")

    
def deldata():
        name=input("Enter Name of Customer : ")
        no=int(input("Enter the phone number of the buyer : "))
        cur.execute("delete from `{}` where cno={}".format(name,no))
        mydb.commit()
        print("Record deleted!!")
    
    
def fetchdata():
        na=input("Enter Name of Buyer : ")
        no=int(input("Enter the phone number of the person : "))
        cur.execute("Show Tables")
        myrecords=cur.fetchall()
        i=0
        x=myrecords
        if x!=None:
            a=cur.execute("Select * from {}".format(na))
            abc=cur.fetchall()
            cur.execute(a,abc)
            print(tabulate(cur, headers=['cname','cno','item','itpr','itqty'],tablefmt='grid'))
            # print(abc)
        else:
            print("Table doesn't Exists!!")
        
        
        

# *************************************************************************** #

def billing():
    
    print("*** BILLING ***")

    #while True:
        
    print ('''
        1. Add record
        2. Delete record
        3. Display records
        4. Exiting''')
                
                
    choice=int (input ("Enter your choice: "))
    if choice == 1:
            adddata()
            
    elif choice== 2:
        deldata()
                
    elif choice== 3:
        fetchdata()
                
    elif choice == 4:
        print ("Exiting")
        
    else:
        print("wrong input")

# ******************************************************************************* #

while True:
    
    print('''
    1. Inventory
    2. Billing ''')
    
    ch=int(input("\nEnter your Choice -- "))

    if ch==1 :
        stock()

    elif ch==2:
        billing()

    else:
        print("\nPlease Enter a Valid Input")
        
    aa=input("\n\nDo you want to Continue ? (y/n) - ")
    if aa=='n':
        print("\nEXITING PROGRAM ...")
        break