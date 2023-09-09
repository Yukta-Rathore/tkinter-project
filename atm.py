from tkinter import *
import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="root",db="atm")
c=con.cursor()
c.execute("create table if not exists details(name varchar(500),password varchar(500)\
          ,balance float)")

def newuser():
    scr=Tk()
    scr.title("YUKTA")
    scr.geometry("3600x3600")
    scr.config(bg="white")
    def submit():
        nm=name.get()
        pw=passw.get()
        cpw=conpass.get()
        info=(nm,pw,0)
        if(pw==cpw and pw!="" and cpw!=""):
            query="Insert into details(name,password,balance) values(%s,%s,%s)"
            c.execute(query,info)
            con.commit()
            Label(scr,text="User registered!!              ",font=("Times",15,"bold")\
                  ,bg="White",fg="Red").place(x=500,y=600)
            con.close()
        elif(pw!="" and pw!=cpw and cpw!=""):
            Label(scr,text="Password do not match          ",font=("Times",15,"bold"),\
                  bg="White",fg="Red").place(x=500,y=600)
        else:
            con.rollback()
            Label(scr,text="Please fill all the information",font=("Times",15,"bold")\
                  ,bg="White",fg="Red").place(x=500,y=600)  

    Label(scr,text="Registration page",font=("Times",50,"bold"),bg="White",fg="Blue").pack()

    Label(scr,text="Name",font=("Times",20,"bold"),bg="White",fg="Black")\
          .place(x=500,y=250)
    name=Entry(scr)
    name.place(x=850,y=258)

    Label(scr,text="Password",font=("Times",20,"bold"),bg="White",fg="Black").\
           place(x=500,y=350)
    passw=Entry(scr,show="*")
    passw.place(x=850,y=358)

    Label(scr,text="Confirm Password",font=("Times",20,"bold"),bg="White",fg="Black")\
             .place(x=500,y=450)
    conpass=Entry(scr,show="*")
    conpass.place(x=850,y=458)

    Button(scr,text=" Submit ",font=("Time",15,"bold"),bg="Red",\
       fg="White",command=submit).place(x=500,y=550)
    Button(scr,text="  Exit  ",font=("Time",15,"bold"),bg="Red",\
       fg="White",command=scr.destroy).place(x=870,y=550)

def registereduser():
    r=Tk()
    r.title("YUKTA")
    r.geometry("3600x3600")
    r.config(bg="white")

    def submit():
        if(name.get!="" and passw.get()!=""):
            c.execute("Select * from details")
            detail=c.fetchall()
            flag=0
            for i in detail:
                n=i[0]
                p=i[1]
                if(n==name.get() and p==passw.get()):
                    flag=1
                    break
                    
            if(flag==0):
                Label(r,text="User name or password did not match",font=("Times",15,"bold"),\
                  bg="White",fg="Red").place(x=500,y=600)
            elif(flag==1):
                def deposit():
                        dep=Tk()
                        dep.title("YUKTA")
                        dep.geometry("3600x3600")
                        dep.config(bg="white")
                        

                        def bal():
                            if(depositm.get()!="" and float(depositm.get())>0):
                                c.execute("Select balance from details where name=(%s) AND \
password=(%s)",(name.get(),passw.get()))
                                b=c.fetchone()[0]
                                b=b+float(depositm.get())
                                c.execute('update details set balance=(%s) where name=(%s)\
AND password=(%s)',(b, name.get(),passw.get()))
                                con.commit()
                                Label(dep,text="Amount deposited              ",\
                                font=("Times",20,"bold"),bg="White",fg="Red")\
                                .place(x=640,y=450)
                                con.close()
                            elif(float(depositm.get())<0):
                                Label(dep,text="Please enter valid amount   ",\
                                      font=("Times",20,"bold"),bg="White",fg="Red")\
                                      .place(x=640,y=450)  

                            else:
                                Label(dep,text="Please enter the deposit        ",\
                                      font=("Times",15,"bold"),bg="White",fg="Red")\
                                      .place(x=640,y=450)  

                        Label(dep,text="Enter amount to deposit",\
                              font=("Times",50,"bold"),bg="White",fg="Blue").pack()
                        depositm=Entry(dep)
                        depositm.place(x=680,y=250)
                        Button(dep,text="  Deposit  ",font=("Time",20,"bold")\
                               ,bg="Red",fg="White",command=bal).place(x=670,y=350)
                def withdraw():
                    withd=Tk()
                    withd.title("YUKTA")
                    withd.geometry("3600x3600")
                    withd.config(bg="white")
                    def wd():
                        if(w.get()!=""):
                            c.execute("Select balance from details where name=(%s) AND \
password=(%s)",(name.get(),passw.get()))
                            b=c.fetchone()[0]
                            if(float(w.get())<=b and float(w.get())>0):
                                b=b-float(w.get())
                                c.execute('Update details SET balance=(%s) where \
name=(%s) AND password=(%s)',(b, name.get(),passw.get()))
                                con.commit()
                                con.close()
                                Label(withd,text="Amount withdrawn           \
                                        ",font=("Times",20,"bold"),bg="White",fg="Red").\
                                        place(x=640,y=450)
                            elif(float(w.get())>b):
                                Label(withd,text="Insufficient balance                     \
             ",font=("Times",20,"bold"),bg="White",fg="Red").place(x=640,y=450)
                            elif(float(w.get())<0):
                                Label(withd,text="Invalid amount entered                     \
             ",font=("Times",20,"bold"),bg="White",fg="Red").place(x=640,y=450)
                        else:
                            Label(withd,text="Please enter the amount to be withdrawn     ",\
                                      font=("Times",20,"bold"),bg="White",fg="Red")\
                                      .place(x=640,y=450)  

                    Label(withd,text="Enter amount to withdraw",\
                              font=("Times",50,"bold"),bg="White",fg="Blue").pack()
                    w=Entry(withd)
                    w.place(x=680,y=250)
                    Button(withd,text="  Withdraw  ",font=("Time",20,"bold")\
                           ,bg="Red",fg="White",command=wd).place(x=670,y=350)
                        
                def check():
                    ch=Tk()
                    ch.title("YUKTA")
                    ch.geometry("400x100")
                    ch.config(bg="white")
                    
                    c.execute("Select balance from details where name=(%s) AND \
password=(%s)",(name.get(),passw.get()))
                    b=c.fetchone()[0]
                    con.close()
                    Label(ch,text="Current Balance is "+str(b),\
                              font=("Times",20,"bold"),bg="White",fg="Red").pack()

                def cp():
                    q=Tk()
                    q.title("YUKTA")
                    q.geometry("3600x3600")
                    q.config(bg="white")

                    def change():
                        if(np.get()!="" and cnp.get()!="" and np.get()==cnp.get()):
                            c.execute("Select password from details where name=(%s) AND \
password=(%s)",(name.get(),passw.get()))
                            op=c.fetchone()[0]
                            if(op==np.get()):
                                Label(q,text="Please select a new password           ",\
                                  font=("Times",20,"bold"),bg="White",fg="Red")\
                                  .place(x=500,y=580)
                                con.close()
                            else:
                                c.execute("Update details set password=(%s) where name=(%s) AND \
password=(%s)",(np.get(),name.get(),passw.get()))
                                con.commit()
                                Label(q,text="Password changed                             ",\
                                      font=("Times",20,"bold"),bg="White",fg="Red")\
                                      .place(x=500,y=580)
                                con.close()
                        elif(np.get()!=cnp.get() and np.get()!="" and cnp.get()!=""):
                            Label(q,text="Password do not match          ",\
                                  font=("Times",20,"bold"),bg="White",fg="Red")\
                                  .place(x=500,y=580)
                        else:
                            Label(q,text="Please fill all the information",\
                                  font=("Times",20,"bold"),bg="White",fg="Red")\
                                  .place(x=500,y=580)
            

                    Label(q,text="Change password",font=("Times",50,"bold"),bg="White"\
                          ,fg="Blue").pack()

                    Label(q,text="New Password",font=("Times",20,"bold"),bg="White"\
                          ,fg="Black").place(x=500,y=250)
                    np=Entry(q,show="*")
                    np.place(x=850,y=258)

                    Label(q,text="Confirm Password",font=("Times",20,"bold"),bg="White"\
                          ,fg="Black").place(x=500,y=350)
                    cnp=Entry(q,show="*")
                    cnp.place(x=850,y=358)

                    Button(q,text=" Submit ",font=("Time",15,"bold"),bg="Red",\
                           fg="White",command=change).place(x=500,y=500)
                    Button(q,text="  Exit  ",font=("Time",15,"bold"),bg="Red",\
                           fg="White",command=q.destroy).place(x=880,y=500)

                root=Tk()
                root.title("YUKTA")
                root.geometry("3600x3600")
                root.config(bg="white")
                Label(root,text="Please select one option!!",font=("Times",50,"bold")\
                      ,bg="White",fg="Blue").pack()

                Button(root,text="      Deposit      ",font=("Time",20,"bold"),\
                           bg="Dark Blue",fg="White",command=deposit).place(x=660,y=150)
                Button(root,text="    Withdraw     ",font=("Time",20,"bold"),\
                           bg="Dark Blue",fg="White",command=withdraw).place(x=660,y=250)
                Button(root,text="    Check balance   ",font=("Time",20,"bold")\
                           ,bg="Dark Blue",fg="White",command=check).place(x=640,y=350)
                Button(root,text="  Change password  ",font=("Time",20,"bold")\
                           ,bg="Dark Blue",fg="White",command=cp).place(x=632,y=450)
                Button(root,text="         Exit        ",font=("Time",20,"bold")\
                           ,bg="Red",fg="White",command=root.destroy).place(x=665,y=550)
                    
        else:
            Label(r,text="Please fill all the information",font=("Times",15,"bold")\
                  ,bg="White",fg="Red").place(x=500,y=600)  

    Label(r,text="Login page",font=("Times",50,"bold"),bg="White",fg="Blue").pack()

    Label(r,text="Name",font=("Times",20,"bold"),bg="White",fg="Black")\
          .place(x=500,y=250)
    name=Entry(r)
    name.place(x=850,y=258)

    Label(r,text="Password",font=("Times",20,"bold"),bg="White",fg="Black").\
           place(x=500,y=350)
    passw=Entry(r,show="*")
    passw.place(x=850,y=358)

    Button(r,text="  Enter   ",font=("Time",15,"bold"),bg="Red",\
       fg="White",command=submit).place(x=500,y=550)
    Button(r,text="  Cancel  ",font=("Time",15,"bold"),bg="Red",\
       fg="White",command=r.destroy).place(x=870,y=550)
    

scr=Tk()
scr.title("YUKTA")
scr.geometry("3600x3600")
scr.config(bg="white")
scr.iconbitmap(r"C:\Users\user\Downloads\download.ico")

Label(scr,text="Bank Of Yukta",font=("Times",50,"bold"),bg="White",fg="Blue").pack()

imagei=PhotoImage(file=r"C:\Users\user\Downloads\images.gif")
Label(scr,image=imagei).place(x=670,y=150,height=150,width=260)

Button(scr,text="New User",font=("Time",20,"bold"),bg="Dark Blue",\
       fg="White",command=newuser).place(x=700,y=350)

Button(scr,text="Registered User",font=("Time",20,"bold"),bg="Dark Blue",\
       fg="White",command=registereduser).place(x=660,y=450)
