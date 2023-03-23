    
import mysql.connector as ms
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl


mycon=ms.connect(host='localhost', user='root', passwd='1234567890')
if mycon.is_connected():
    print('Connected Successfully')

    
command=mycon.cursor()     
command.execute('Create database if not exists Hotel')
command.execute('Use Hotel')

command.execute('Create table if not exists Hotel_Visitors(ID int primary key,\
               Name char(30), Mobile_no bigint, ID_Proof char(20), ID_no int,\
               Nationality char(30), City char(20))')

command.execute('Create table if not exists Room_Details(R_no int primary key,\
               R_type char(40), Charges int, Vacancy char(8) default "Vacant")')

command.execute('Create table if not exists Booking(BID char(8) primary key,ID int, R_no int , Enroll_Date date)')

command.execute('Alter table Booking add foreign key(ID) references Hotel_Visitors(ID),add foreign key(R_no) references Room_Details(R_no)')

command.execute('Create table if not exists Billing(BID int primary key,\
               ID int, R_no int, Enroll_Date date, DisEnroll_Date date,Stay int,Amount int, GST char(10), Net_Amount int)')

command.execute('Alter table Billing add foreign key(ID) references Hotel_Visitors(ID),\
                add foreign key(R_no) references Room_Details(R_no)')


while True:
    command.execute('Select * from Room_Details')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        command.execute('Insert into Room_Details values(1001,"Single bed+NonAC",1500,"Vacant"),\
                                                        (1002,"Single bed+NonAC",1500,"Vacant"),\
                                                        (1003,"Single bed+NonAC",1500,"Vacant"),\
                                                        (1004,"Single bed+NonAC",1500,"Vacant"),\
                                                        (1005,"Double bed+NonAC",2300,"Vacant"),\
                                                        (1006,"Double bed+NonAC",2300,"Vacant"),\
                                                        (1007,"Double bed+NonAC",2300,"Vacant"),\
                                                        (2001,"Single bed+AC",1700,"Vacant"),\
                                                        (2002,"Single bed+AC",1700,"Vacant"),\
                                                        (2003,"Single bed+AC",1700,"Vacant"),\
                                                        (2004,"Single bed+AC",1700,"Vacant"),\
                                                        (2005,"Double bed+AC",2500,"Vacant"),\
                                                        (2006,"Double bed+AC",2500,"Vacant"),\
                                                        (2007,"Double bed+AC",2500,"Vacant"),\
                                                        (3001,"Confrence Hall",5000,"Vacant"),\
                                                        (3002,"Confrence Hall",5000,"Vacant"),\
                                                        (3003,"Confrence Hall",5000,"Vacant")')
        mycon.commit()
    else:
        break



def ShowVisitors():
    print()
    print('----------------------------------------------------------')
    print("Visitor's Details Are as Follows ")
    print('__________________________________________________________')
    print()
    command.execute('select * from Hotel_Visitors')
    Details=command.fetchall()
    c=command.rowcount
    if c==0:
        print('Sorry, but no Visitor yet! ☺☺')
    else:
        df=pd.DataFrame(Details, columns=['Visitor ID', 'Visitor Name', 'Mobile No', 'ID Proof', 'ID No', 'Nationality', 'City'])
        print(df.to_string(index=False))
    print('**********************************************************')

def AddVisitors():
    print()
    print('**********************************************************')
    print('Adding Visitors...')
    print('__________________________________________________________')
    print()
    ID=int(input("Visitor's ID -->"))
    while True:
        command.execute('Select * from Hotel_Visitors where ID={}'.format(ID,))
        command.fetchall()
        c=command.rowcount
        if c>=1:
            print("Visitor ID ",str(ID),' already exists...')
            ID=int(input('Please Enter VIsitor ID -->'))
        else:
            break
    Name=input('Please Enter Your Name-->')
    Mobile_no=int(input('Enter your Mobile No. -->'))
    print()
    print('Identification type are :')
    print('     1. Aadhar Card')
    print('     2. Passport')
    print('     3. PAN Card')
    print('     4. Driving Licence')
    ID_Proof=int(input('Please press 1 to select Aadhar Card\
                        Please press 2 to select Passport\
                        Please press 3 to select PAN Card\
                        Please press 4 to select Driving License'))
    while True:
        idtype=''
        if ID_Proof<=0 or ID_Proof>=5:            
            print('Sorry, But enter a valid option -->')
            ID_Proof=int(input('Again choose any Identification type :'))
        else:       
            if ID_Proof==1:
                idtype='Aadhar Card'
            elif ID_Proof==2:
                idtype='Passport'
            elif ID_Proof==3:
                idtype='PAN Card'
            elif ID_Proof==4:
                idtype='Driving Licence'
            break
    ID_no=int(input('Please Enter your ID Number -->'))    
    print()
    print('Which type of nationality do you have :')
    print('     1. Indian')
    print('     2. Foreigner')
    Nationality=int(input('Please press 1 to select Nationality as Indian\
                        Please press 2 to select Nationality as Foreigner'))
    while True:
        ntype=''
        if Nationality<=0 or Nationality>=3:
            print('Sorry ☺☺, But Please enter a Valid Option!')
            Nationality=int(input('Again choose the correct option -->'))
        else:
            if Nationality==1:
                ntype='Indian'
            elif Nationality==2:
                ntype='Foreigner'
            break
    City=input('Please Enter your Belonging City Name -->') 
    print()

    command.execute('Insert into Hotel_Visitors values({}, "{}", {}, "{}", {}, "{}", "{}")'.format(ID, Name, Mobile_no, idtype, ID_no, ntype, City))
    mycon.commit()
    print()
    print('__________________________________________________________')
    print()
    print('Guest Add Successfully...')
    print()
    print('**********************************************************')
    
def UpdateVisitorDetails():
    command.execute('Select * from Hotel_Visitors')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Guest is Available to Update.')
        print()
        print('**********************************************************')
    else:
        print()
        print('**********************************************************')
        ShowVisitors()
        print('__________________________________________________________')
        print()
        print('Updating Guest Details...')
        print('__________________________________________________________')
        print()   
        print('Enter Update Field Type : ')
        print('     1. By Guest ID')

        UpdateVisitor=int(input('Select type to update Guest Details -->'))
        while True:
            if UpdateVisitor<=0 or UpdateVisitor>=2:
                print('Invalid input, Please select valid input...')
                UpdateVisitor=int(input('Again select type to update Guest Details -->'))
            
            else:
                if UpdateVisitor==1:
                    ID=int(input('Enter Guest ID of the Guest for update -->'))
                    while True:
                        command.execute('Select * from Hotel_Visitors where ID={}'.format(ID,))
                        command.fetchall()
                        c=command.rowcount
                        if c==0:
                            print('Guest ID ',str(ID),' is not found...')
                            ID=int(input('Again Enter Guest ID -->'))
                        else:
                            break
                    Name=input('Guest Name-->')
                    Mobile_no=int(input('Mobile No. -->'))
                    print()
                    print('Identification type are :')
                    print('     1. Aadhar Card')
                    print('     2. Passport')
                    print('     3. PAN Card')
                    print('     4. Driving Licence')
                    ID_Proof=int(input('Choose any Identification type :'))
                    while True:
                        idtype=''
                        if ID_Proof<=0 or ID_Proof>=5:            
                            print('Invalid input, Please select valid input...')
                            ID_Proof=int(input('Again choose any Identification type :'))
                        else:       
                            if ID_Proof==1:
                                idtype='Aadhar Card'
                            elif ID_Proof==2:
                                idtype='Passport'
                            elif ID_Proof==3:
                                idtype='PAN Card'
                            elif ID_Proof==4:
                                idtype='Driving Licence'
                            break
                    ID_no=int(input('ID Number -->'))    
                    print()
                    print('Which type of nationality do you have :')
                    print('     1. Indian')
                    print('     2. Foreigner')
                    Nationality=int(input('Choose nationality type -->'))
                    while True:
                        ntype=''
                        if Nationality<=0 or Nationality>=3:
                            print('Invalid input, Please select valid input...')
                            Nationality=int(input('Again choose nationality type -->'))
                        else:
                            if Nationality==1:
                                ntype='Indian'
                            elif Nationality==2:
                                ntype='Foreigner'
                            break
                    City=input('City Name -->') 
                    print()
                    
                    command.execute('Update Hotel_Visitors set Name="{}", Mobile_no={}, ID_Proof="{}", ID_no={}, Nationality="{}", City="{}" where ID={}'.format(Name, Mobile_no, idtype, ID_no, ntype, City, ID))
                    mycon.commit()
                    print()
                    print('__________________________________________________________')
                    print()
                    print('Guest Details Update Successfully...')
                    print()
                    print('**********************************************************')
                break
                    
            

def RemoveVisitor():
    command.execute('Select * from Hotel_Visitors')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Guest is Available to Delete.')
        print()
        print('**********************************************************')
    else:
        print()
        print('**********************************************************')
        ShowVisitors()
        print('__________________________________________________________')
        print()
        print('Deleting Guest Details...')
        print('__________________________________________________________')
        print()   
        print('Enter Delete Field Type : ')
        print('     1. By Guest ID')
        RemoveVisitor=int(input('Select type to delete Guest deatils -->'))
        while True:
            if RemoveVisitor<=0 or RemoveVisitor>=2:
                print('Invalid input, Please select valid input...')
                RemoveVisitor=int(input('Again select type to delete Guest Details -->'))
            
            else:
                if RemoveVisitor==1:
                    ID=int(input('Enter Guest ID of the Guest for delete -->'))
                    while True:
                        command.execute('Select * from Hotel_Visitors where ID={}'.format(ID,))
                        command.fetchall()
                        cnt=command.rowcount
                        if cnt==0:
                            print('Guest ID ',str(ID),' is not found...')
                            ID=int(input('Again Enter Guest ID -->'))
                        else:
                            command.execute('Delete from Hotel_Visitors where ID={}'.format(ID,))
                            mycon.commit()
                            print()
                            print('__________________________________________________________')
                            print()
                            print('Guest Details Deleted Successfully...')
                            print()
                            print('**********************************************************') 
                            break
                                                   
                
                
    #Function : 5 - Search for Guest
def SearchVisitor():
    command.execute('Select * from Hotel_Visitors')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Guest is Available to Search.')
        print()
        print('**********************************************************')
    else:
        print()
        print('**********************************************************')
        print('Searching for Guest...')
        print('__________________________________________________________')
        print()   
        print('Enter Search Field Type : ')
        print('     1. By Guest ID')
        SearchVisitor=int(input('Select type to search Guest deatils -->'))
        while True:
            if SearchVisitor<=0 or SearchVisitor>=2:
                print('Invalid input, Please select valid input...')
                SearchVisitor=int(input('Again select type to Guest Details -->'))
            
            else:
                if SearchVisitor==1:
                    ID=int(input('Enter Guest ID to search the Guest -->'))
                    command.execute('Select * from Hotel_Visitors where ID={}'.format(ID,))
                    command.fetchall()
                    cnt=command.rowcount
                    if cnt>=1:
                        print()
                        print('Guest Detail is : ')
                        print()
                        print('__________________________________________________________')
                        print()
                        command.execute('Select * from Hotel_Visitors where ID={}'.format(ID,))
                        gdetail=command.fetchall()
                        df=pd.DataFrame(gdetail, columns=['Visitor ID', 'Visitor Name', 'Mobile No', 'ID Proof', 'ID No', 'Nationality', 'City'])
                        print(df.to_string(index=False))
                        print()
                        print('**********************************************************')
                    else:
                        print()
                        print('__________________________________________________________')
                        print()
                        print('Guest No. ',str(ID), ' is not found...' )
                        print()
                        print('**********************************************************') 
                    break
                        
                                    
    #Function : 6 - Summary of Guest
def SummaryOfVisitors():
    print()
    print('**********************************************************')
    print('Summary of Guests...')
    print('__________________________________________________________')
    print()
    command.execute('Select * from Hotel_Visitors')
    command.fetchall()
    Total_no_of_guest=command.rowcount
    print(' >>> Total No. of Guest in our Hotel  :  ', Total_no_of_guest)
    print()
    print(' >>> No. of Guest Nationality wise :- ')
    command.execute('Select * from Hotel_Visitors where Nationality="Indian"')
    command.fetchall()
    No_of_Indian=command.rowcount
    print('          Indian  :  ', No_of_Indian)
    command.execute('Select * from Hotel_Visitors where Nationality="Foreigner"')
    command.fetchall()
    No_of_Foreigner=command.rowcount
    print('          Foreigner  :  ', No_of_Foreigner)
    print()
    print(' >>> No. of Guest City wise :- ')
    command.execute('Select City, count(*) as "No. of Guest" from Hotel_Visitors group by City')
    Total_guest_by_City=command.fetchall()
    dfnoofcities=pd.DataFrame(Total_guest_by_City, columns=['City', 'No. of Guest'])
    print(dfnoofcities.to_string(index=False))
    print()
    print('**********************************************************')


##Functions of Room Menu

    #Function : 1 - Show Rooms
def ShowRoom():
    print()
    print('**********************************************************')
    print('Room Details are : ')
    print('__________________________________________________________')
    print()
    command.execute('select * from Room_Details')
    rdetails=command.fetchall()
    if cnt==0:
        print('No Guest Records Available.')
    else:
        df=pd.DataFrame(rdetails, columns=['Room No', 'Room Type', 'Charges', 'Vacancy'])
        print(df.to_string(index=False))
    print('**********************************************************')

    #Function : 2 - Adding New Room
def AddRoom():
    print()
    print('**********************************************************')
    print('Adding Room...')
    print('__________________________________________________________')
    print()
    R_no=int(input('Room No -->'))
    while True:
        command.execute('Select * from Room_Details where R_no={}'.format(R_no,))
        command.fetchall()
        cnt=command.rowcount
        if cnt>=1:
            print('Room No. ',str(R_no),' is already exist...')
            R_no=int(input('Again Enter Room No. -->'))
        else:
            break
    print()
    print('Room types are :')
    print('     1. Single Room (Charges(per day) = Rs. 1500)')
    print('     2. Double Room (Charges(per day) = Rs. 2500)')
    print('     3. Family Room (Charges(per day) = Rs. 3000)')
    print('     4. Duplex Room (Charges(per day) = Rs. 5500)')
    print('     5. Conference Room (Charges(per day) = Rs. 8500)')
    print('     6. Inter-Connecting Room (Charges(per day) = Rs. 6000)')
    print()
    R_type=int(input('Choose any Room type :'))
    while True:
        if R_type<=0 or R_type>=7:
            print('Invalid input, Please select valid input...')
            R_type=int(input('Again choose any Room type :'))
        else:
            rtype=''
            Charges=0
            if R_type==1:
                rtype='Single Room'
                Charges=1500
            elif R_type==2:
                rtype='Double Room'
                Charges=2500
            elif R_type==3:
                rtype='Family Room'
                Charges=3000
            elif R_type==4:
                rtype='Duplex Room'
                Charges=5500
            elif R_type==5:
                rtype='Conference Room'
                Charges=8500
            elif R_type==6:
                rtype='Inter-Connecting Room'
                Charges=6000
           
                
            command.execute('Insert into Room_Details values({}, "{}", {}, "Vacant")'.format(R_no, rtype, Charges))
            mycon.commit()
            print()
            print('__________________________________________________________')
            print()
            print('Room Add Successfully...')
            print()
            print('**********************************************************')
        break

    #Function : 3 - Update Room Details
def UpdateRoomDetails():
    command.ecute('Select * from Room_Details')
    command.fetchallxe()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Room is Available to Update.')
        print()
        print('**********************************************************')
    else:
        print()
        print('**********************************************************')
        print('Updating Room Details...')
        print('__________________________________________________________')
        print()
        R_no=int(input('Enter Room No to Update Room Details -->'))
        while True:
            command.execute('Select * from Room_Details where R_no={}'.format(R_no,))
            command.fetchall()
            cnt=command.rowcount
            if cnt==0:
                print('Room No. ',str(R_no),' is not exist...')
                R_no=int(input('Again Enter Room No. -->'))
            else:
                break
        print()
        print('Room types are :')
        print('     1. Single Room (Charges(per day) = Rs. 1500)')
        print('     2. Double Room (Charges(per day) = Rs. 2500)')
        print('     3. Family Room (Charges(per day) = Rs. 3000)')
        print('     4. Duplex Room (Charges(per day) = Rs. 5500)')
        print('     5. Conference Room (Charges(per day) = Rs. 8500)')
        print('     6. Inter-Connecting Room (Charges(per day) = Rs. 6000)')
        print()
        R_type=int(input('Choose any Room type :'))
        while True:
            if R_type<=0 or R_type>=7:
                print('Invalid input, Please select valid input...')
                R_type=int(input('Again choose any Room type :'))
            else:
                rtype=''
                Charges=0
                if R_type==1:
                    rtype='Single Room'
                    Charges=1500
                elif R_type==2:
                    rtype='Double Room'
                    Charges=2500
                elif R_type==3:
                    rtype='Family Room'
                    Charges=3000
                elif R_type==4:
                    rtype='Duplex Room'
                    Charges=5500
                elif R_type==5:
                    rtype='Conference Room'
                    Charges=8500
                elif R_type==6:
                    rtype='Inter-Connecting Room'
                    Charges=6000
                break
                    
        command.execute('Update Room_Details set R_type="{}", Charges={} where R_no={}'.format(rtype, Charges, R_no))
        mycon.commit()
        print()
        print('__________________________________________________________')
        print()
        print('Room Details Updating Successfully...')
        print()
        print('**********************************************************')

    #Function : 4 - Removing Room
def RemoveRoom():
    command.execute('Select * from Room_Details')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Room is Available to Delete.')
        print()
        print('**********************************************************')
    else:
        print()
        print('**********************************************************')
        ShowRoom()
        print('__________________________________________________________')
        print()
        print('Deleting Room Details...')
        print('__________________________________________________________')
        print()   
        R_no=int(input('Enter Room No for delete the room -->'))
        while True:
            command.execute('Select * from Room_Details where R_no={}'.format(R_no,))
            command.fetchall()
            cnt=command.rowcount
            if cnt==0:
                print('Room No. ',str(R_no),' is not found...')
                R_no=int(input('Again Enter Room No -->'))
            else:
                command.execute('Delete from Room_Details where R_no={}'.format(R_no,))
                mycon.commit()
                print()
                print('__________________________________________________________')
                print()
                print('Room Details Deleted Successfully...')
                print()
                print('**********************************************************') 
                break
                
    #Function : 5 - Search for Room
def SearchRoom():
    command.execute('Select * from Room_Details')
    command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print()
        print('No Room is Available to Delete.')
        print()
        print('**********************************************************')
    else:
        print()
        R_no=int(input('Enter Room No for search the room -->'))
        command.execute('Select * from Room_Details where R_no={}'.format(R_no,))
        command.fetchall()
        cnt=command.rowcount
        if cnt==0:
            print()
            print('__________________________________________________________')
            print()
            print('Room No. ',str(R_no), ' is not found...' )
            print()
            print('**********************************************************') 
        else:
            print()
            print('Room Detail is : ')
            print()
            print('__________________________________________________________')
            print()
            command.execute('Select * from Room_Details where R_no={}'.format(R_no,))
            rdetail=command.fetchall()
            df=pd.DataFrame(rdetail, columns=['Room No', 'Room Type', 'Charges', 'Vacancy'])
            print(df.to_string(index=False))
            print()
            print('**********************************************************')
        
        
    #Function : 6 - Summary of Guest
def SummaryOfRoom():
    print()
    print('**********************************************************')
    print('Summary of Rooms...')
    print('__________________________________________________________')
    print()
    command.execute('Select * from Room_Details')
    command.fetchall()
    Total_no_of_guest=command.rowcount
    print(' >>> Total No. of Room in our Hotel  :  ', Total_no_of_guest)
    print()
    
    print(' >>> No. of Room type wise :- ')
    command.execute('Select * from Room_Details where R_type="Single Room"')
    command.fetchall()
    Total_no_of_single=command.rowcount
    print('          Single Room            :  ', Total_no_of_single)
    command.execute('Select * from Room_Details where R_type="Double Room"')
    command.fetchall()
    Total_no_of_double=command.rowcount
    print('          Double Room            :  ', Total_no_of_double)
    command.execute('Select * from Room_Details where R_type="Family Room"')
    command.fetchall()
    Total_no_of_Family=command.rowcount
    print('          Family Room            :  ', Total_no_of_Family)
    command.execute('Select * from Room_Details where R_type="Duplex Room"')
    command.fetchall()
    Total_no_of_duplex=command.rowcount
    print('          Duplex Room            :  ', Total_no_of_duplex)
    command.execute('Select * from Room_Details where R_type="Conference Room"')
    command.fetchall()
    Total_no_of_conference=command.rowcount
    print('          Conference Room        :  ', Total_no_of_conference)
    command.execute('Select * from Room_Details where R_type="Inter-Connecting Room"')
    command.fetchall()
    Total_no_of_interconnecting=command.rowcount
    print('          Inter-Connecting Room  :  ', Total_no_of_interconnecting)
    print()
    
    print(' >>> No. of Room Vacancy wise :- ')
    command.execute('Select * from Room_Details where Vacancy="Vacant"')
    command.fetchall()
    Total_no_of_vacant=command.rowcount
    print('          Vacant Room  :  ', Total_no_of_vacant)
    command.execute('Select * from Room_Details where Vacancy="Booked"')
    command.fetchall()
    Total_no_of_book=command.rowcount
    print('          Booked Room  :  ', Total_no_of_book)
    print()
    print('**********************************************************')


##Functions of Booking Menu

    #Function : 1 - Show Current Booking Details
def ShowCurrentBooking():
    print()
    print('**********************************************************')
    print('Current Booking Details are : ')
    print('__________________________________________________________')
    print()
    command.execute('select * from Booking')
    booking_details=command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print('No Bookings are Available.')
    else:
        df=pd.DataFrame(booking_details, columns=['Booking ID', 'Guest ID', 'Room No', 'Check in Date'])
        print(df.to_string(index=False))
    print('**********************************************************')

    #Function : 2 - Show Previous Booking Details
def ShowBilling_Details():
    print()
    print('**********************************************************')
    print('Billing Details are : ')
    print('__________________________________________________________')
    print()
    command.execute('select * from Billing')
    billing_details=command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print('No Previous Bookings are Available.')
    else:
        df=pd.DataFrame(billing_details, columns=['Booking ID', 'Guest ID', 'Room No', 'Enroll_Date', 'DisEnroll_Date','Stay',  'Amount', 'GST',  'NetAmount'])
        print(df.to_string(index=False))
    print('**********************************************************')
    
    #Function : 3 - Booking of a Room
def BookingRoom():
    print()
    print('**********************************************************')
    print('Booking of Room...')
    print('__________________________________________________________')
    print()
    BID=int(input('Booking ID > '))
    while True:
        command.execute('Select * from Booking where BID={}'.format(BID))
        command.fetchall()
        cnt=command.rowcount
        if cnt>=1:
            print('Booking ID ',BID, ' already exist...')
            BID=int(input('Again Enter Booking ID >'))
        else:
            break   
    print()
    print('**********************************************************')
    print('Availability of Rooms...')
    print('__________________________________________________________')
    print()
    command.execute('Select R_no, R_type from Room_Details where Vacancy like "%Vacant%" order by R_no')
    data=command.fetchall()
    cnt=command.rowcount
    if cnt==0:
        print()
        print('**********************************************************')
        print('No Rooms are Available... ')
        print('__________________________________________________________')
        print()
    else:
        print()
        print('**************************************************')
        print('Available Rooms are :-')
        print('**************************************************')
        print()
        df=pd.DataFrame(data, columns=['Room No.', 'Room Type'])
        print(df.to_string(index=False))
        print()
    
    R_no=int(input('Enter R_no > '))
    while True:
        command.execute('Select * from Room_Details where R_no={}'.format(R_no))
        command.fetchall()
        cnt=command.rowcount
        if cnt==0:
            print('Room No. ',str(R_no), ' not exist...')
            R_no=int(input('Again enter Room No > '))
        else:
            command.execute('Select * from Room_Details where Vacancy like "%Booked%" and R_no={}'.format(R_no))
            command.fetchall()
            cnt=command.rowcount
            if cnt>=1:
                print('Room No. ', str(R_no), ' is already Booked.')
                R_no=int(input('Again enter Room No > '))
            else:
                break
        
    ID=int(input('Guest ID > '))
    while True:
        command.execute('Select * from Hotel_Visitors where ID={}'.format(ID))
        command.fetchall()
        cnt=command.rowcount
        if cnt==0:
            print('Guest ID ',ID, ' not exist...')
            ID=int(input('Again Enter Guest ID >'))
        else:
            break
    Enroll_Date=input('Check in Date (YYYY-MM-DD) > ')
    
    command.execute('Insert into Booking(BID, ID, R_no, Enroll_Date) values("{}", {}, {}, "{}")'.format(BID, ID, R_no, Enroll_Date))
    mycon.commit()
    command.execute('Insert into Billing(BID, ID, R_no, Enroll_Date) values("{}", {}, {}, "{}")'.format(BID, ID, R_no, Enroll_Date))
    mycon.commit()
    
    command.execute('Update Room_Details set Vacancy="Booked" where R_no={}'.format(R_no))
    mycon.commit()
    
    command.execute('Select Name from Hotel_Visitors where ID={}'.format(ID))
    data=command.fetchone()
    for Name in data:
        Name=Name
    print('Room No. ',R_no, ' booked successfully for Guest ', Name, '...')
    print()
    print('**********************************************************')
        
    #Function : 4 - Generate Bill
def BillGenerate():
    print()
    print('**********************************************************')
    print('Generating Bill...')
    print('__________________________________________________________')
    print()
    BID=int(input('Booking ID > '))
    while True:
        command.execute('Select * from Booking where BID={}'.format(BID))
        command.fetchall()
        cnt=command.rowcount
        if cnt==0:
            print('Booking ID ',BID, ' not exist...')
            BID=int(input('Again Enter Booking ID >'))
        else:
            break   
        
    print()
    print('__________________________________________________________')
    command.execute('Select BID, ID, R_no, Enroll_Date from Booking where BID={}'.format(BID))
    data=command.fetchall()
    df=pd.DataFrame(data, columns=['Booking ID', 'Guest ID', 'Room No.', 'Enroll_Date'])
    print(df.to_string(index=False))
    print('__________________________________________________________')
    
    DisEnroll_Date=input('Check out Date (YYYY-MM-DD) > ')
    command.execute('Update Billing set DisEnroll_Date="{}" where BID={}'.format(DisEnroll_Date, BID))
    mycon.commit()
    while True:
        command.execute('Select DateDiff(DisEnroll_Date, Enroll_Date) from Billing where BID={}'.format(BID))
        data=command.fetchone()
        for a in data:
            Stay=a
        if Stay<0:
            print("Invalid Check out date, it can't be less than check in date...")
            DisEnroll_Date=input('Again Check out Date (YYYY-MM-DD) > ')
            command.execute('Update Previous_Booking set DisEnroll_Date="{}" where BID={}'.format(DisEnroll_Date, BID))
            mycon.commit()
        if Stay>=0:
            Stay=Stay+1
            break
    
    command.execute('Select Room_Details.Charges from Room_Details, Booking where Room_Details.R_no=Booking.R_no and BID={}'.format(BID))
    data=command.fetchone()
    for x in data:
        Charges=x
    
    Amount=Stay*Charges
    GST=Amount*(12/100)
    Net_Amount=Amount+GST
    
    command.execute('Update Billing set Stay={}, Amount={}, GST={},Net_Amount={} where BID={}'.format(Stay, Amount, GST,Net_Amount, BID))
    mycon.commit()
    command.execute('Update Room_Details set Vacancy="Vacant" where (Select R_no from Booking where BID={})'.format(BID))
    mycon.commit()
    command.execute('Delete from Booking where BID={}'.format(BID))
    mycon.commit()
    
    command.execute('Select R_no from Billing where BID={}'.format(BID))
    data=command.fetchone()
    for a in data:
        R_no=a
    
    command.execute('Select R_Type from Room_Details where R_no={}'.format(R_no))
    data=command.fetchone()
    for a in data:
        R_Type=a
    
    command.execute('Select ID from Billing where BID={}'.format(BID))
    data=command.fetchone()
    for a in data:
        ID=a
    
    command.execute('Select Name from Hotel_Visitors where ID="{}"'.format(ID))
    data=command.fetchone()
    for a in data:
        Name=a

    command.execute('Select Enroll_Date from Billing where BID={}'.format(BID))
    data=command.fetchone()
    for a in data:
        Enroll_Date=a

    command.execute('Select DisEnroll_Date from Billing where BID={}'.format(BID))
    data=command.fetchone()
    for a in data:
        DisEnroll_Date=a
    
    print()
    print()
    print('*'*50)
    print('                   HOTEL MAHARAJA')
    print('            (Opp. Bikaner Railway Station)')
    print('_'*50)
    print('_'*50)
    print()
    print()
    print('                 Billing Receipt :-')
    print('              _______________________')
    print()
    print('          Booking ID           :           ', BID)
    print('          Room No              :           ', R_no)
    print('          Room Type            :           ', R_Type)
    print('          Guest ID             :           ', ID)
    print('          Guest Name           :           ', Name)
    print('          Check in Date        :           ', Enroll_Date)
    print('          Check out Date       :           ', DisEnroll_Date)
    print('          No. of Stay          :           ', Stay)
    print('          Charges (per Room)   :           ', Charges)
    print('          Amount               :           ', Amount)
    print('          GST (@ 12 %)         :           ', GST)
    print()
    print('                                 Net Amount          :        Rs. ', Net_Amount)
    print()
    print('          ___________________________________________')
    print()
    print('                Thanks for Stay in our Hotel &')
    print('              Enjoy the Feeling of "MAHARAJAS" !')
    print('          ___________________________________________')    
    print()
    print()
    print('**********************************************************')
    print()
    
## FUNCTIONS OF REPORT MENU

    #Function - 1 : On the basis of vacancy
def Report_VacancyBasis():
    print()
    print('**********************************************************')
    print('Report of the Hotel Maharaja')
    print('__________________________________________________________')
    print()
    command.execute('Select IsVacant from Room_Info where IsVacant like "%Booked%"')
    command.fetchall()
    BookedRoom=command.rowcount
    command.execute('Select IsVacant from Room_Info where IsVacant like "%vacant%"')
    command.fetchall()
    VacantRoom=command.rowcount
    
    x=[BookedRoom, VacantRoom]
    y=np.arange(2)
    pl.bar(y,x, color=['g', 'orange'], width=0.5)
    pl.xticks(y, ['Booked', 'Vacant'])
    pl.title('Report of Hotel on the Basis of Vacancies of Room')
    pl.xlabel('Types of Vacancy')
    pl.ylabel('No. of Rooms')
    pl.show()
    
    print('Total No. of Room ',BookedRoom+VacantRoom, 'out of which : ' )
    print(' >>> Booked     :     ', BookedRoom)
    print(' >>> Vacant     :     ', VacantRoom)
    print('**********************************************************')
    
    #Function - 2 : On the basis of frequency of booking
def Report_FrequencyOfBooking():
    print()
    print('**********************************************************')
    print('Report of the Hotel Maharaja')
    print('__________________________________________________________')
    print()
    Year=int(input('Enter Year --> '))
    while True:
        command.execute('Select * from Previous_Booking where Year(Enroll_Date)={}'.format(Year,))
        command.fetchall()
        cnt=command.rowcount
        if cnt<=0:
            print('Bookings of Year ', str(Year), ' not available...')
            Year=int(input('Again enter Year --> '))
        else:
            command.execute('Select * from Previous_Booking where Year(Enroll_Date)={}'.format(Year,))
            command.fetchall()
            cnt=command.rowcount
            if cnt==0:
                print('__________________________________________________________')
                print()
                print('No. Records are Available...')
                print('__________________________________________________________') 
                break
            else:
                li=[]
                clrs=['m', 'olive', 'r', 'tan', 'g', 'burlywood', 'b', 'gold', 'y', 'c', 'k', 'b']
                month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                count=0
                for a in range(1, 13):
                    command.execute('Select count(Enroll_Date) from Previous_Booking where Month(Enroll_Date)={} and Year(Enroll_Date)={}'.format(a, Year))
                    data=command.fetchone()[0]
                    if data==None:
                        count=0
                        li.append(count)
                    else:
                        count=int(data)
                        li.append(count)
                df=pd.DataFrame(li, index=month, columns=['No. of Bookings'])
                print()
                pl.bar(month, df['No. of Bookings'], color=clrs)
                pl.xlabel('Months')
                pl.ylabel('Total No. of Room Bookings (acc. to months) ')
                pl.title('Report of Hotel on the Basis of Frequency of Room Bookings')
                pl.show()
                
                command.execute('Select count(Enroll_Date) from Previous_Booking where Year(Enroll_Date)={}'.format(Year,))
                data=command.fetchone()[0]
                TBooking=int(data)
                print('Total Booking in Year ', Year, ' is : ', TBooking)
                break
                print('**********************************************************')    
        
    #Function - 3 : On the basis of Income from booking
def Report_IncomeFromBooking():
    print()
    print('**********************************************************')
    print('Report of the Hotel Maharaja')
    print('__________________________________________________________')
    print()
    Year=int(input('Enter Year --> '))
    while True:
        command.execute('Select * from Previous_Booking where Year(Enroll_Date)={}'.format(Year,))
        command.fetchall()
        cnt=command.rowcount
        if cnt<=0:
            print('Bookings of Year ', str(Year), ' not available...')
            Year=int(input('Again enter Year --> '))
        else:
            command.execute('Select * from Previous_Booking where Year(DisEnroll_Date)={}'.format(Year,))
            command.fetchall()
            cnt=command.rowcount
            if cnt==0:
                print('__________________________________________________________')
                print()
                print('No. Records are Available...')
                print('__________________________________________________________') 
                break
            else:
                li=[]
                clrs=['m', 'olive', 'r', 'tan', 'g', 'burlywood', 'b', 'gold', 'y', 'c', 'k', 'b']
                month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                count=0
                for a in range(1, 13):
                    command.execute('Select sum(Net_Amount) from Previous_Booking where Month(Enroll_Date)={} and Year(Enroll_Date)={}'.format(a, Year))
                    data=command.fetchone()[0]
                    if data==None:
                        count=0
                        li.append(count)
                    else:
                        count=int(data)
                        li.append(count)
                df=pd.DataFrame(li, index=month, columns=['Total Income'])
                print()
                pl.bar(month, df['Total Income'], color=clrs)
                pl.xlabel('Months')
                pl.ylabel('Total Income (acc. to months) ')
                pl.title('Report of Hotel on the Basis of Income from Bookings')
                pl.show()
                
                command.execute('Select sum(Net_Amount) from Previous_Booking where Year(Enroll_Date)={}'.format(Year,))
                data=command.fetchone()[0]
                TIncome=int(data)
                print('Total Income in Year ', Year, ' is : Rs. ', TIncome)
                break
                print('**********************************************************')
                    
    
'''DIFFERENT SUB-MENUS OF THE HOTEL MANAGEMENT SYSTEM'''

## Menu : 1 - Guest Details
def GuestMenu():
    while True:
            print('Guest Details :-')
            print()
            print('          1. Show Guests')
            print('          2. Add Guest')
            print('          3. Update Guest Details')
            print('          4. Remove Guest')
            print('          5. Search for Guest')
            print('          6. Summary of the Guest')
            print('          7. Back to Main Menu(<<)')
            print()
            gwant=int(input('    Enter any option from above -->'))
            
            if gwant==1:
                ShowVisitors()
            elif gwant==2:
                AddVisitors()
            elif gwant==3:
                UpdateVisitorDetails()
            elif gwant==4:
                RemoveVisitor()
            elif gwant==5:
                SearchVisitor()
            elif gwant==6:
                SummaryOfVisitors()
            elif gwant==7:
                break
            else:
                print()
                print('Invalid input, Please select valid input...')
                print()

## Menu : 2 - Room Details
def RoomMenu():
    while True:
            print('Room Details :-')
            print()
            print('          1. Show Rooms')
            print('          2. Add Room')
            print('          3. Update Room Details')
            print('          4. Remove Room')
            print('          5. Search for Room')
            print('          6. Summary of the Rooms')
            print('          7. Back to Main Menu(<<)')
            rwant=int(input('    Enter any option from above -->'))
            
            if rwant==1:
                ShowRoom()
            elif rwant==2:
                AddRoom()
            elif rwant==3:
                UpdateRoomDetails()
            elif rwant==4:
                RemoveRoom()
            elif rwant==5:
                SearchRoom()
            elif rwant==6:
                SummaryOfRoom()
            elif rwant==7:
                break
            else:
                print()
                print('Invalid input, Please select valid input...')
                print()

## Menu : 3 - Booking of Rooms
def BookingMenu():
    while True:
            print('Booking Details :-')
            print()
            print('          1. Show Current Booking Details')
            print('          2. Show Previous Booking Details')
            print('          3. Booking of a Room')
            print('          4. Generate Bill')
            print('          5. Back to Main Menu(<<)')
            print()
            bwant=int(input('    Enter any option from above -->'))
            
            if bwant==1:
                ShowCurrentBooking()
            elif bwant==2:
                ShowBilling_Details()
            elif bwant==3:
                BookingRoom()

            elif bwant==4:
                BillGenerate()
            elif bwant==5:
                break
            else:
                print()
                print('Invalid input, Please select valid input...')
                print()
    
    
    
## Menu : 4 - Report Menu
def Reports():
    while True:
        print()  
        print('Report Of The Hotel  :-')
        print()
        print('          1. On the Basis of Vacancies of Rooms')
        print('          2. On the Basis of Frequency of Booking')
        print('          3. On the Basis of Income from Booking')
        print('          4. Back to Main Menu(<<)')
        print()
        reportmenu=int(input('    Enter any option from above -->'))
        
        if reportmenu==1:
            Report_VacancyBasis()
        elif reportmenu==2:
            Report_FrequencyOfBooking()
        elif reportmenu==3:
            Report_IncomeFromBooking()
        elif reportmenu==4:
            break
        else:
            print('Invalid input, Please select valid input...')

    
'''MAIN MENU OF THE HOTEL'''

#Here, we are creating main menu or front page of our hotel management software
def MainMenu():
    while True:
        print()
        print()
        print()
        print('*'*50)
        print('                   HOTEL MAHARAJA')
        print('            (Opp. Bikaner Railway Station)')
        print('*'*50)
        print()
        print()
        print('     Welcome To Our Room Reservation System:-')
        print()
        print('          1. Guest Details')
        print('          2. Room Details')
        print('          3. Booking of Rooms')
        print('          4. Reports of Hotel')
        print('          5. Exit')
        MenuCmd=int(input('    Enter What you want -->'))
        
        if MenuCmd==1:
            GuestMenu()
        elif MenuCmd==2:
            RoomMenu()
        elif MenuCmd==3:
            BookingMenu()
        elif MenuCmd==4:
            Reports()
        elif MenuCmd==5:
            print('Exiting...')
            break
        else:
            print()
            print('Invalid input, Please select valid input...')
            print()
MainMenu()
