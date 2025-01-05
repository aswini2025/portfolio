

##PRINTING WELCOME MESSAGE

print("""
        ================================
           Welcome to Hospital
        ================================
""")
##Establishing connection and creating database along with required tables
import random
import mysql.connector as ms
pd=str(input("Enter Database Password:"))
cn=ms.connect(host="localhost",user="root",passwd="prince",database='hospital')
cur=cn.cursor()
#creating database for hospital
cur.execute("create database if not exists prince_hospital")
cur.execute("use prince_hospital")
cur.execute("create table if not exists patients\
                 (pid int(10) primary key,\
                 name varchar(30) not null,\
                 mobile varchar(10),\
                 age int(3) not null,\
                 city varchar(50) not null,\
                 doc_rec varchar(30))")
cur.execute("create table if not exists doctors\
                (docid int primary key,name varchar(30),\
                department varchar(40),\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                fees int(10),\
                salary int(10))")
cur.execute("create table if not exists nurses\
                (nurseid int primary key,name varchar(30),\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                salary int(10))")
cur.execute("create table if not exists workers\
                 (workerid int primary key,name varchar(30),\
                 age int(2),\
                 city varchar(30),\
                 mobile varchar(15),\
                 salary int(10))")
#login or signup option for users
#creating table for storing the username and password of the new user
cur.execute("create table if not exists users\
                 (username varchar(30) primary key,\
                  password varchar(30) default'000')")



def sign_up():
    print("""

            ============================================
            !!!!!!!Please enter new user details!!!!!!!!
            ============================================
                                                """)
    u=input("Enter New User Name:")
    p=input("Enter password (Combination of Letters, Digits etc.):")
    
    #ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
    cur.execute("insert into users values('{}','{}')".format(u,p))
    cn.commit()
    print("""
        ========================================================
         !!!!!!!!Congratulations!!! New User Created...!!!!!!!!
        ========================================================
                                            """)

def login():
    
    #Login with username and password

            print("""
                ==========================================================
                !!!!!!!!  {{Loginwith username and password }}  !!!!!!!!!!
                ===========================================================
                                                    """)
            un=input("Username!!:")
            ps=input("Password!!:")
            #pid=0
            cur.execute("select password from users where username='{}'".format(un))
            rec=cur.fetchall()
            for i in rec:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        #Menu for Administrative Tasks
                        print("""
                            1.Admin Tasks
                            2.Patient (Admit and Discharge)
                            3.Sign Out
                                                          
                                                        """)
                        #prompt message for the task from user
                        a=int(input("Enter your choice:"))
                        #Admin tasks
                        if a==1:
                            print("""
                                1. Show Details
                                2. Add new member
                                3. Delete existing member
                                4. Exit
                                                         """)
                            b=int(input("Enter your choice:"))
                            #Showing details of doctors, nurses and workers
                            if b==1:
                                print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers
                                                     """)
                                
                                #Prompt Message for users to show details
                                c=int(input("ENTER YOUR CHOICE:"))
                                #See the details of doctors 
                                if c==1:
                                    cur.execute("select * from doctors")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        b=0
                                        v=list(i)
                                        k=["DOCTORID","NAME","DEPARTEMNT","AGE","CITY","MOBILE","FEES","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                #See the details of nurses    
                                elif c==2:
                                    cur.execute("select * from nurses")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NURSEID","NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                #See the details of workers
                                elif c==3:
                                    cur.execute("select * from workers")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["WORKERID","NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                            #Add new member into hosptial team
                            elif b==2:
                                print("""

                                    1. Doctor
                                    2. Nurse
                                    3. Worker
                                                                                """)
                                c=int(input("Enter your choice:"))
                                #New doctor details
                                if c==1:
                                  #Prompt messages for doctor details
                                  cur.execute('select * from doctors')
                                  rec=cur.fetchall()
                                  l=[]
                                  for i in rec:
                                    v=list(i)
                                    l.append(v[0])
                                  num=random.randint(10001,99999)
                                  if num in l:
                                    num=random.randint(10001,99999)
                                    docid=num
                                  else:
                                    docid=num
                                  name=input("Enter name of doctor:")
                                  dep=input("Enter department:")
                                  age=input("Enter age:")
                                  city=input("Enter city doctor belongs to:")
                                  mno=input("Enter 10 digit mobile no.:")
                                  fees=input("Enter fees:")
                                  sal=input("Enter Salary of doctor:")
                                  #Insert values into doctors table
                                  cur.execute("insert into doctors values({},'{}','{}','{}','{}','{}','{}','{}')".format(docid,name,dep,age,city,mno,fees,sal))
                                  cn.commit()
                                  print("New doctor details has been added successfully. ")
                                #New nurse details
                                elif c==2:
                                  #Prompt message for nurse details
                                  cur.execute('select * from nurses')
                                  rec=cur.fetchall()
                                  l=[]
                                  for i in rec:
                                    v=list(i)
                                    l.append(v[0])
                                  num=random.randint(100001,999999)
                                  if num in l:
                                    num=random.randint(100001,999999)
                                    nurseid=num
                                  else:
                                    nurseid=num
                                  name=input("Enter name of nurse:")
                                  age=input("Enter age:")
                                  city=input("Enter city nurse belongs to:")
                                  mno=input("Enter mobile no.:")
                                  sal=int(input("Enter salary:"))
                                  #Insert value into nurses table
                                  cur.execute("insert into nurses values({},'{}','{}','{}','{}','{}')".format(nurseid,name,age,city,mno,str(sal)))
                                  cn.commit()
                                  print("New nurse details has been added successfully.")
                                #New worker details
                                elif c==3:
                              #Prompt message for worker details
                                  cur.execute('select * from workers')
                                  rec=cur.fetchall()
                                  l=[]
                                  for i in rec:
                                    v=list(i)
                                    l.append(v[0])
                                  num=random.randint(1000001,9999999)
                                  if num in l:
                                    num=random.randint(1000001,9999999)
                                    workerid=num
                                  else:
                                    workerid=num
                                  name=input("Enter name of worker:")
                                  age=input("Enter Age:")
                                  city=input("Enter city:")
                                  mno=input("Enter mobile no:")
                                  ms=input("Enter Salary:")
                                  #Insert worker details into doctors table
                                  cur.execute("insert into workers values({},'{}','{}','{}','{}','{}')".format(workerid,name,age,city,mno,ms))
                                  cn.commit()
                                  print("SUCCESSFULLY ADDED")
                            #Menu for delete data
                            elif b==3:
                               print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers
                                                                                """)
                               c=int(input("Enter your choice:"))
                               #deleting doctor's details
                               if c==1:
                                   name=input("Enter doctor name to delete:")
                                   cur.execute("select * from doctors where name='{}'".format(name))
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Do you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from doctors where name='{}'".format(name))
                                       cn.commit()
                                       print("Doctor has been deleted successfully")
                                   else:
                                       print("Error in deletion....")
                                   
                                  
                               #deleting nurse details
                               elif c==2:
                                   name=input("Enter name of nurse:")
                                   cur.execute("select * nurses where name='{}'".format(name))
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Do you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from nurses where name='{}'".format(name))
                                       mysql.commit()
                                       print("Nurse has been deleted successfully.")
                                   else:
                                       print("Error in deletion")
                               #deleting worker details
                               elif c==3:
                                   name=input("Enter name of worker:")
                                   cur.execute("select * from workers where name='{}'".format(name))
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Do you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from workers where name='{}'".format(name))
                                       cn.commit()
                                       print("Worker has been deleted.")
                                   else:
                                       print("Error in deletion.")
                            elif b==4:
                                print("Thank you! See you again! Have nice Day!")
                                break
                           
                        #entering the patient details table
                        elif a==2:
                            
                            print("""
                                    1. Show patient record
                                    2. Admit new patient
                                    3. Discharge Patient
                                    4. Exit
                                                                      """)
                            b=int(input("ENTER YOUR CHOICE:"))
                            #showing the existing details of patients
                            #See the details of patient
                            if b==1:
                                cur.execute("select * from patients")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                    v=list(i)
                                    k=["PID","NAME","MOBILE NO","AGE","CITY","DOCTOR RECOMMENDED"]
                                    d=dict(zip(k,v))
                                    for i in d:
                                        print(i,":",d[i])
                            #Admit a new patient
                            elif b==2:
                                cur.execute('select * from patients')
                                rec=cur.fetchall()
                                l=[]
                                for i in rec:
                                    v=list(i)
                                    l.append(v[0])
                                num=random.randint(1001,9999)
                                if num in l:
                                    num=random.randint(1001,9999)
                                    pid=num
                                else:
                                    pid=num
                                print(pid)
                                #pid=pid+1
                                name=input("Enter name of patient: ")
                                mn=input("Enter Mobile no.: ")
                                age=input("Enter age: ")
                                city=input("Enter City: ")
                                cur.execute("select name from doctors")
                                rec=cur.fetchall()
                                print(rec)
                                print(pid)
                                
                                dr=str(input("Enter doctorname to be recommended:"))
                                cur.execute ("insert into patients values('{}','{}','{}','{}','{}','{}')".format(pid,name,mn,age,city,dr))
                                cn.commit()            
                                
                                print("""
                                ====================================
                                !!!!!!!New patient admitted!!!!!!
                                ====================================
                                                """)
                            #discharge a patient
                            elif b==3:
                                name=input("Enter the name of patient to discharge:")
                                cur.execute("select * from patients where name='{}'".format(name))
                                rec=cur.fetchall()
                                print(rec)
                                bill=input("Has the patient paid the bill (y/n):")
                                if bill=="y":
                                    cur.execute("delete from patients where name like'%"+name+"%'")
                                    cn.commit()
                                    print('Patient record deleted successfully')
                                elif bill=="n":
                                    print("Please pay your pending bill amount to discharge patient.")
                                else:
                                    print("Bill payment status is unknown....")
                            #if user wants to exit
                            elif b==4:
                                break
                        ###SIGN OUT
                        elif a==3:
                            break
def change_pass():
    cur.execute("select username from users")
    rec=cur.fetchall()
    for i in rec:
        v=list(i)
        k=["USERNAME"]
        d=dict(zip(k,v))
    print(d)
    u=input("Enter username to change password from above:")
    if u in d.values():
        pd=input("Enter New Password:")
        pd1=input("Renter New Password again:")
        if pd==pd1:
          cur.execute("update users set password='{}' where username='{}'".format(pd1,u))
          cn.commit()
          print("Password Changed Successfully.")
        else:
          print("Password did not match...")
    else:
        print("Username not found")
            
#Main Menu
r=0
while r!=4:
    print("""
                    1. Sign Up (New User)
                    2. Log In
                    3. Change Password
                    4. Exit
                                                        """)

    r=int(input("Enter your choice:"))    
    #New User Registration
    if r==1:
        sign_up()
    elif r==2:
        login()                 
    elif r==3:
        change_pass()
    elif r==4:
      print("Thank you.Have a nice day!")
      break

