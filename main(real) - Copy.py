from tkinter import *
from tkinter import ttk
from tkinter import messagebox,simpledialog
import dbconnect as db
from datetime import datetime
from PIL import ImageTk,Image #pip install pillow
from tkinter import filedialog
import os
import smtplib
import random
import pandas.io.sql as sql
import xlwt
from pymysql import*


win=Tk()
win.resizable(width=False,height=True)
win.state('zoomed')





color=['red','green','yellow','blue','pink','gold','brown']
def introlabelcolortick():
    fg=random.choice(color)
    sliderlabel.config(fg=fg)
    sliderlabel.after(2,introlabelcolortick)

    


def introlabeltick():
    global count,text
    if(count>=len(ss)):
        count=-1 ####count=0  ##    inside loop count+=1 when count=0
        text=' '
        sliderlabel.config(text=text)
    else:
        text=text+ss[count]
        sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(200,introlabeltick)

ss="BANK AUTOMATION"
count=0
text=' '

sliderlabel=Label(win,text=ss,relief='ridge',borderwidth='5',font=('chiller',30,'italic bold'),width='45')
sliderlabel.place(x=260,y=0)
introlabeltick()
introlabelcolortick()



def tick():
    
    time_string=time.strftime("%H-%M-%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text='Date:'+date_string +"\n"+'Time:'+time_string)
    clock.after(200,tick)
    clock=Label(win,font=('times',14,'italic bold'),relief='ridge',borderwidth='4',bg='red')
    clock.place(x=10,y=10)
    tick()

    
def login(prvfrm=None):
    if(prvfrm!=None):
        prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    

    bank_b=ImageTk.PhotoImage(Image.open("bank.jpg").resize((1300,500)))
    b_bank=Button(frm,image=bank_b)
    b_bank.image=bank_b
    b_bank.place(relwidth=1,relheight=1)

    newuser_b=ImageTk.PhotoImage(Image.open("signup.jpg").resize((90,40)))
    b_newuser=Button(frm,image=newuser_b,command=lambda:newuserscreen(frm))
    b_newuser.image=newuser_b
    b_newuser.place(x=1200,y=10)

    
    

    admin_b=ImageTk.PhotoImage(Image.open("admin.jpg").resize((90,40)))
    b_admin=Button(frm,image=admin_b,command=lambda:adminhomescreen(frm))
    b_admin.image=admin_b
    b_admin.place(x=1100,y=10)

    
    login_b=ImageTk.PhotoImage(Image.open("login.jpg").resize((90,40)))
    b_login=Button(frm,image=login_b,command=lambda:homescreen(frm))
    b_login.image=login_b
    b_login.place(x=1000,y=10)
    
    
    
    


def adminhomescreen(prvfrm):
    if(prvfrm!=None):
        prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue')
    user_lbl.place(x=400,y=100)
    
    pass_lbl=Label(frm,text='Password:',font=('',20,''),fg='blue')
    pass_lbl.place(x=400,y=150)

    usertype_lbl=Label(frm,text='UserType:',font=('',20,''),fg='blue')
    usertype_lbl.place(x=400,y=200)
    
    user_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    pass_entry=Entry(frm,show='*',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=150)
    
    type_dropdown=ttk.Combobox(frm,values=['User','Admin'],font=('',11,''))
    type_dropdown.current(0)
    type_dropdown.place(x=580,y=200)

    reset_b=ImageTk.PhotoImage(Image.open("reset.jpg").resize((110,50)))
    b_reset=Button(frm,image=reset_b,command=lambda:resethome(user_entry,pass_entry))
    b_reset.image=reset_b
    b_reset.place(x=650,y=400)

    

    forgotpassword_b=ImageTk.PhotoImage(Image.open("forgotpassword.jpg").resize((110,50)))
    b_forgotpassword=Button(frm,image=forgotpassword_b,command=lambda:forgotpassscreen(frm))
    b_forgotpassword.image=forgotpassword_b
    b_forgotpassword.place(x=500,y=400)

    admin_b=ImageTk.PhotoImage(Image.open("admin.jpg").resize((110,50)))
    b_admin=Button(frm,image=admin_b,command=lambda:admintype(frm,user_entry,pass_entry,type_dropdown))
    b_admin.image=admin_b
    b_admin.place(x=600,y=300)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:login(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)

    
def homescreen(prvfrm):
    if(prvfrm!=None):
        prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    
    
    
    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue')
    user_lbl.place(x=400,y=100)
    
    pass_lbl=Label(frm,text='Password:',font=('',20,''),fg='blue')
    pass_lbl.place(x=400,y=150)

    usertype_lbl=Label(frm,text='UserType:',font=('',20,''),fg='blue')
    usertype_lbl.place(x=400,y=200)
    
    user_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    pass_entry=Entry(frm,show='*',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=150)
    
    type_dropdown=ttk.Combobox(frm,values=['User','Admin'],font=('',11,''))
    type_dropdown.current(0)
    type_dropdown.place(x=580,y=200)
       

    login_b=ImageTk.PhotoImage(Image.open("login.jpg").resize((110,50)))
    b_login=Button(frm,image=login_b,command=lambda:validatehomescreen(frm,user_entry,pass_entry,type_dropdown))
    b_login.image=login_b
    b_login.place(x=600,y=300)
    


    reset_b=ImageTk.PhotoImage(Image.open("reset.jpg").resize((110,50)))
    b_reset=Button(frm,image=reset_b,command=lambda:resethome(user_entry,pass_entry))
    b_reset.image=reset_b
    b_reset.place(x=650,y=400)

    

    forgotpassword_b=ImageTk.PhotoImage(Image.open("forgotpassword.jpg").resize((110,50)))
    b_forgotpassword=Button(frm,image=forgotpassword_b,command=lambda:forgotpassscreen(frm))
    b_forgotpassword.image=forgotpassword_b
    b_forgotpassword.place(x=500,y=400)

    

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:login(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)

##    back_btn=Button(frm,text='Back',command=lambda:login (frm),width=10,font=('',12,''),bg='powder blue',bd=5)
##    back_btn.place(x=50,y=20)

    

    
    
def forgotpassscreen(prvfrm):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    user_lbl=Label(frm,text='username:',font=('',20,''),fg='blue')
    user_lbl.place(x=400,y=100)
    
    email_lbl=Label(frm,text='email:',font=('',20,''),fg='blue')
    email_lbl.place(x=400,y=150)
    
    mob_lbl=Label(frm,text='mobile:',font=('',20,''),fg='blue')
    mob_lbl.place(x=400,y=200)
    
    user_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    email_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    email_entry.place(x=580,y=150)
    
    mob_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    mob_entry.place(x=580,y=200)
    
    recvr_btn=Button(frm,text='Recover',command=lambda:recoverpass(frm,user_entry,email_entry,mob_entry),width=10,font=('',12,''),bg='powder blue',bd=5)
    recvr_btn.place(x=400,y=300)
    
    reset_btn=Button(frm,text='Reset',command=lambda:resetforgotpass(user_entry,email_entry,mob_entry),width=10,font=('',12,''),bg='powder blue',bd=5)
    reset_btn.place(x=550,y=300)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:homescreen(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)
    
    
    
def newuserscreen(prvfrm):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    user_lbl=Label(frm,text='UserName:',font=('',20,''),fg='blue')
    user_lbl.place(x=400,y=100)
    
    pass_lbl=Label(frm,text="Password:",font=('',20,''),fg='blue')
    pass_lbl.place(x=400,y=150)
    
    email_lbl=Label(frm,text='Email:',font=('',20,''),fg='blue')
    email_lbl.place(x=400,y=200)
    
    mob_lbl=Label(frm,text='Mobile:',font=('',20,''),fg='blue')
    mob_lbl.place(x=400,y=300)
    
    type_lbl=Label(frm,text='Account:',font=('',20,''),fg='blue')
    type_lbl.place(x=400,y=250)
    
    bal_lbl=Label(frm,text="Initial Bal:",font=('',20,''),fg='blue')
    bal_lbl.place(x=400,y=350)
    
    user_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    pass_entry=Entry(frm,show='*',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=150)
    
    email_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    email_entry.place(x=580,y=200)
    
    mob_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    mob_entry.place(x=580,y=300)
    
    type_dropdown=ttk.Combobox(frm,values=['Current','Saving'],font=('',11,''))
    type_dropdown.current(0)
    type_dropdown.place(x=580,y=250)
    
    bal_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    bal_entry.place(x=580,y=350)
    
    opn_btn=Button(frm,text='Open Account',command=lambda:validatenewuser(frm,user_entry,pass_entry,email_entry,type_dropdown,mob_entry,bal_entry),width=15,font=('',12,''),bg='powder blue',bd=5)
    opn_btn.place(x=480,y=450)


    reset_btn=Button(frm,text='Reset',command=lambda:resetnewuser(user_entry,pass_entry,mob_entry,email_entry,bal_entry),width=10,font=('',12,''),bg='powder blue',bd=5)
    reset_btn.place(x=650,y=450)
    
    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:homescreen(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)
    
def resethome(eu,ep):
    eu.delete(0,END)
    ep.delete(0,END)
    eu.focus()
def resetnewuser(eu,ep,em,ee,eb):
    eu.delete(0,END)
    ep.delete(0,END)
    em.delete(0,END)
    ee.delete(0,END)
    eb.delete(0,END)
    eu.focus()
def resetforgotpass(eu,em,ee):
    eu.delete(0,END)
    em.delete(0,END)
    ee.delete(0,END)
    eu.focus()
    
def validatehomescreen(frm,eu,ep,et):
    u=eu.get()
    p=ep.get()
    t=et.get()
    if(len(u)==0 or len(p)==0):
        messagebox.showwarning('Validaton failed',"username/password cant be empty")
        return
    else:
        con=db.getCon()
        cur=con.cursor()
        cur.execute("select * from ubank where username=%s and password=%s",(u,p))
        tup=cur.fetchone()
        if(tup!=None):
            if(t=='User'):
                messagebox.showinfo('Login Success',f"Welcome,{u}")
                welcomeuser(frm,u)            
            else:
                messagebox.showerror('Login Failed',"Invalid User type")
        else:
            messagebox.showerror('Login Failed',"Invalid Username/Password")
            
            
def validatenewuser(frm,eu,ep,ee,em,eb,et):
    u=eu.get()
    p=ep.get()
    e=ee.get()
    t=em.get()
    m=eb.get()
    b=et.get()
    if(len(u)==0 or len(p)==0 or len(e)==0 or len(m)==0 or len(b)==0 or len(t)==0):
        messagebox.showwarning('Validation failed',"fields cant be empty")
        return
    else:
        con=db.getCon()
        cur=con.cursor()
        cur.execute("select  max(accountno) from ubank")
        accountno=cur.fetchone()[0]
        accountno=accountno+1
        try:
            cur.execute("insert into ubank values(%s,%s,%s,%s,%s,%s,%s)",(u,p,e,t,m,b,accountno))
            con.commit()
            messagebox.showinfo('success',"account open with accountno:"+str(accountno))
            homescreen(frm)
            
        except Exception as e:
            messagebox.showwarning('username exits'+str(e))
            con.close()


            
def recoverpass(frm,a,b,c):
    u=a.get()
    e=b.get()
    m=c.get()
    con=db.getCon()
    cur=con.cursor()
    cur.execute("SELECT password FROM ubank where username=%s and email=%s and mobile=%s",(u,e,m))   
    tup=cur.fetchone()
    if(tup!=None):
          p=tup[0]
          messagebox.showinfo('password recovery',f"your password is:"+str(p))
          homescreen(frm)
          con.commit()
          con.close()
    else:
        messagebox.showinfo('password recovery',"invalid details")

def welcomeuser(prvfrm,u):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    if(os.path.exists(f'{u}.jpeg')):
        img=ImageTk.PhotoImage(Image.open(f'{u}.jpeg').resize((150,150)))
    else:
        img=ImageTk.PhotoImage(Image.open('default.jpeg').resize((150,150)))
        
    lbl_img=Label(frm,image=img)
    lbl_img.image=img
    lbl_img.place(x=10,y=30)

    updatepic_btn=Button(frm,text='change profile picture',command=lambda:changepic(frm,u))
    updatepic_btn.place(x=10,y=200)
    
    withdraw_btn=Button(frm,text='withdraw',command=lambda:withdraw(u),width=15,font=('',12,''),bg='powder blue',bd=5)
    withdraw_btn.place(x=600,y=50)

    deposit_btn=Button(frm,text='deposit',command=lambda:deposit(u),width=15,font=('',12,''),bg='powder blue',bd=5)
    deposit_btn.place(x=600,y=120)

    bal_btn=Button(frm,text='check bal',command=lambda:checkbal(u),width=15,font=('',12,''),bg='powder blue',bd=5)
    bal_btn.place(x=600,y=190)

    txn_btn=Button(frm,text='txn history',command=lambda:txnhistory(u),width=15,font=('',12,''),bg='powder blue',bd=5)
    txn_btn.place(x=600,y=260)

    email_btn=Button(frm,text='email',command=lambda:email(u),width=15,font=('',12,''),bg='powder blue',bd=5)
    email_btn.place(x=600,y=400)
  

    updatepass_btn=Button(frm,command=lambda:updatepass(u),text='update pass',width=15,font=('',12,''),bg='powder blue',bd=5)
    updatepass_btn.place(x=600,y=330)

    
    
    logout_btn=Button(frm,text='logout',command=lambda:logout(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    logout_btn.place(relx=.8,y=10)


    exit_btn=Button(frm,text='exit',command=lambda:Exit(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    exit_btn.place(relx=.8,y=50)

    wel_label=Label(frm,text=f'Welcome,{u}',font=('',12,''))
    wel_label.place(x=10,y=0)

def logout(frm):
    messagebox.showinfo('Logout',"you will be logged out!")
    homescreen(frm)

def logout1(frm):
    messagebox.showinfo('Logout',"you will be logged out!")
    adminhomescreen(frm)

def Exit(frm):
    res=messagebox.askyesnocancel('notifications',"Do You Want To Exit?")
    if(res==True):
        win.destroy()

def checkbal(u):
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal from ubank where username=%s",(u,))
    tup=cur.fetchone()    
    messagebox.showinfo('Check bal',f"Your Available Balance :{tup[0]}")
    con.close()
    
def withdraw(u):
    amt=simpledialog.askinteger('Withdraw','Enter Amount:')
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal,accountno from ubank where username=%s",(u,))
    tup=cur.fetchone()    
    avlbal=tup[0]
    accountno=tup[1]
    dt=datetime.now()
    if(avlbal>=amt):
        cur.execute("update ubank set bal=bal-%s where username=%s",(amt,u))
        con.commit()
        messagebox.showinfo('Withdraw',"Txn Done..")
        cur.execute("insert into txnhistory values(%s,%s,%s,%s,%s)",(accountno,dt,amt,'Debit',avlbal-amt))
        con.commit()
        con.close()
    else:
        messagebox.showinfo('Withdraw',"Insufficient Bal")


def deposit(u):
    amt=simpledialog.askinteger('Deposit','Enter Amount:')
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal,accountno from ubank where username=%s",(u,))
    tup=cur.fetchone()    
    avlbal=tup[0]
    accountno=tup[1]
    dt=datetime.now()
    if(amt >= 0):
        cur.execute("update ubank set bal=bal+%s where username=%s",(amt,u))
        con.commit()
        messagebox.showinfo('Deposit',"Txn Done..")
        cur.execute("insert into txnhistory values(%s,%s,%s,%s,%s)",(accountno,dt,amt,'Credit',avlbal+amt))
        con.commit()
        con.close()
    else:
        messagebox.showinfo('Deposit',"Invalid amount")


def updatepass(u):
    np=simpledialog.askstring('Update Password','Enter New Password:')
    cp=simpledialog.askstring('Update Password','Enter Confirm Password:')
    if(np==''):
        con=db.getCon()
        cur=con.cursor()
        cur.execute("update ubank set password=%s where username=%s",(np,u))
        con.commit()
        con.close()
        messagebox.showinfo('Update Password',"Password Changed Successfully")
    else:
       messagebox.showwarning('Update Password',"New and Confirm Passwords do not match") 

def txnhistory(u):
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select accountno from ubank where username=%s",(u,))
    accountno=cur.fetchone()[0]
    cur.execute("select txndate,amt,txntype,updatebal from txnhistory where accountno=%s",(accountno,))
    history=cur.fetchall()
    msg="\tDate\t\tAmount\tType\tUpdate bal\n"
    for row in history:
        msg=msg+'\t'+str(row[0])+'\t'+str(row[1])+'\t'+row[2]+'\t'+str(row[3])+'\n'
    messagebox.showinfo("Txn History",msg)

##def epassbook(u):
    
    

def changepic(frm,u):
    picpath=filedialog.askopenfilename()
    file1=open(picpath,'rb')
    data=file1.read()
    file2=open(f'{u}.jpeg','wb')
    file2.write(data)
    file2.close()
    file1.close()
    img=ImageTk.PhotoImage(Image.open(f'{u}.jpeg').resize((150,150)))
    lbl_img=Label(frm,image=img)
    lbl_img.image=img
    lbl_img.place(x=10,y=30)

def email(u):
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select email from ubank where username=%s",(u,))
    accountno1=cur.fetchone()[0]

    cur.execute("select accountno from ubank where email=%s",(accountno1,))
    accountno2=cur.fetchone()[0]

    cur.execute("select txndate,amt,txntype,updatebal from txnhistory where accountno=%s",(accountno2,))
    history=cur.fetchall()
    msg="\tDate\t\tAmount\tType\tUpdate bal\n"
    for row in history:
        msg=msg+'\t'+str(row[0])+'\t'+str(row[1])+'\t'+row[2]+'\t'+str(row[3])+'\n'
    messagebox.showinfo("Txn History",msg)

    for row in history:
        msg=msg+'\t'+str(row[0])+'\t'+str(row[1])+'\t'+row[2]+'\t'+str(row[3])+'\n'

    text=str("Account")+str(str(accountno2)+"================"+str((history)))
    sender_email='simranbhambri109@gmail.com'
    password="45064506"
    #send_to=p
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_email,password)

    s.sendmail(sender_email,accountno1,text)
    print("msg sent")
    s.quit()

###########################################################################################
def data():
    con=connect(user="root",password="Simran@18967",host="localhost",database="bank",port=3310)
##  df=sql.read_sql('select * from txnhistory',con)
    df=sql.read_sql('select * from ubank',con)
##  df=sql.read_sql('select * from admin',con)

    print(df)


    df.to_excel('ubank.xls')
    
def admintype(frm,ue,pe,te):
    u=ue.get()
    p=pe.get()
    t=te.get()
    if(len(u)==0 or len(p)==0):
        messagebox.showwarning('Validaton failed',"username/password cant be empty")
        return
    else:
        con=db.getCon()
        cur=con.cursor()
        cur.execute("select * from admin where username=%s and password=%s",(u,p))
        tup=cur.fetchone()
        if(tup!=None):
            if(t=='Admin'):
                messagebox.showinfo('Login Success',f"Welcome,{u}")
                adminuser(frm,u)            
            else:
                messagebox.showerror('Login Failed',"Invalid User type")
        else:
            messagebox.showerror('Login Failed',"Invalid Username/Password")


    

def adminuser(prvfrm,u):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    
    updatepass_btn=Button(frm,command=lambda:updatepass(u),text='update pass',width=15,font=('',12,''),bg='powder blue',bd=5)
    updatepass_btn.place(x=600,y=70)

    epass_btn=Button(frm,command=lambda:data(),text='pass book',width=15,font=('',12,''),bg='powder blue',bd=5)
    epass_btn.place(x=600,y=120)

    
    
    logout_btn=Button(frm,text='logout',command=lambda:logout1(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    logout_btn.place(relx=.8,y=10)

    wel_label=Label(frm,text=f'Welcome,{u}',font=('',12,''))
    wel_label.place(x=10,y=0)



    



login()
win.mainloop()

