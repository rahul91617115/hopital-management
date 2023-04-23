import mysql.connector#create table staff(D_ID int(90) PRIMARY KEY,D_NAME char(90),DEPARTMENT varchar(90),DESIGNATION varchar(90),SALARY int(90),SHIFT varchar(6))
def nstaff_display(database):#TO DISPLAY THE ALL THE VALUES IN THE TABLE  debugged
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysql', database=database)

        print("successfully connected ")
        cr = mydb.cursor()
        print("1.display details of all staffs\n2.display details of single staff")
        ch=int(input("enter your choice:-"))
        if ch==1:
            try:


                query = "select * from  staff"
                cr.execute(query)
                m = cr.fetchall()
                for i in m:
                    print(i)
            except Exception as e:
                print(e)
                nstaff_display(database)
                
        elif ch==2:
            try:
                id=int(input("enter the ID of the staff who's detail u want to display:-"))
                q3="select * from staff where ID="+id
                cr.execute(q3)
                x=cr.fetchone()
                for i in x:
                    print(i)
            except Exceptionas as e:
                print(e)
                staff_display()
        elif ch==3:
            pass
        else:
            print("you probably made a wrong choice(enter number 1 or 2 next time")
            nstaff_display()
    except Exception as e:
        print(e)
        nstaff_display(database)
def nstaff_delete(database):#TO SELECT SPECIFIC SELECTION OF ROWS    debugged
    try:

        mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysql', database='database')

        print("successfully connected ")
        cr = mydb.cursor()
        print("THIS ACTION WILL PERMENANTLY DELETE THE TABLE\nADMINISTRATIVE PERMISSION REQUIRED FOR THIS ACTION")
        print("ARE YOU SURE YOU WANT TO CONTINUE(Y/N)")
        if ch=='y' or ch=='Y':
            try:
                cr.execute("drop table medstaff")
                mydb.commit()
                print("SUCCESSFULLY DELETED ")
            except Exception as e:
                print(e)
        
            
        else:
            print("you are probably not the administrator")
    except Exception as e:
        print(e)
        mydb.rollback()
        nstaff_delete()


def nmedstaff_updation(database): # TO UPDATE THE TABLE    debugged
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysql', database=database)

        print("successfully connected ")
        cr = mydb.cursor()
        print("1.Add Values\n2.update single value\n3.Delete one row")
        ch = int(input("enter your choice"))
        if ch == 1:
            try:

                i = int(input("enter the number of rows you want to add"))
                q = 0
                while q < i:#create table medstaff(ID)
                    try:
                        n = int(input("enter the ID"))
                        name = input("enter the staff name ")
                        dep = input("enter the department")
                        des = input("enter the designation")
                        salary = int(input("enter the salary"))
                        swifty = input("enter the shift(day/night)")

                        query = "insert into medstaff values({},'{}','{}','{}',{},'{}')".format(n, name, dep, des, salary,swifty)  # to be debugged from here
                        cr.execute(query)
                        mydb.commit()
                        q = q + 1
                        print("TABLE SUCCESSFULLY UPDATED")
                    except Exception as e:
                        print(e)
                        print("thank you")



            except Exception as e:
                print(e)
        elif ch == 2:

            print("do you want to update 1.salary or 2.any other atribute")
            u = input("enter your choice(1/2):")
            if u == 1:
                try:
                    d = int(input("enter the Id of the staff who's attribute you want to edit"))
                    nm = input("enter the column name which you want to edit")
                    val = int(input("enter the new value "))
                    query = "update  staff set {}={} where ID={}".format(nm, val, d)
                    cr.execute(query)
                    mydb.commit()
                except Exception as e:
                    print(e)

            if u == 2:
                d = int(input("enter the Id of the staff who's salary you want to edit"))
                val = int(input("enter the new salary"))
                query = "update  staff set salary={} where ID={}".format(val, d)
                cr.execute(query)
                mydb.commit()

        elif ch==3:
            
            print("THIS ACTION WILL PERMENANTLY DELETE A ROW:-")
            v = input("do you want to continue?(y/n):-")
            if v == 'y':
                try:
                    id = int(input("enter the ID of the staff you want to delete:-"))
                    qu = "delete from staff where ID={}".format(id)
                    cr.execute(qu)
                    print("successfully deleted the row")
                except Exception as e:
                    print(e)
            else:
                print('not here oh dear')
                nmedstaff_updation(database)
    except Exception as e:
        print(e)
        nmedstaff_updation(database)


# this program consists of nstaff_display() nstaff_delete() and nmedstaff_updation()
#need a main pgm 
