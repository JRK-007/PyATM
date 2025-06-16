################## IMPORTED MODULES #################################
from tkinter import *
from tkinter import messagebox
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import os
import csv
from PIL import Image,ImageTk
import time
import pandas as pd
from datetime import date
import random
from tkcalendar import Calendar
from time import strftime
from fpdf import FPDF
import mysql.connector 
import webbrowser
############################################################ BANKING SCREEN USING CLASS ############################################################

################## CURRENT BALANCE #################################


current_balance=0.00

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ################## INITIALIZING PAGES IN CONTAINER #################################
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, MinistatementPage, BalancePage, InfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

################## START PAGE #################################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('PAYSRM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\abc.PNG'))

        heading=tk.Label(self,text='PAYSRM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        password_label=tk.Label(self,text=(f'Welcome {user_display_name} to PAYSRM Banking'),font=('BatmanForeverAlternate',17),bg='#3d3d5c',fg='white').pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Enter',font=('orbitron',15),command=next_page,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Exit','Do you want to Quit?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='Quit',font=('orbitron',15),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('orbitron',15),fg='white',bg='#33334d',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Exit','Do you want to use another account?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Use another account',font=('orbitron',15),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ################## BOTTOM FRAME #################################
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')

        visa_photo= tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\visa.PNG')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        mastercard_photo= tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\mastercard.PNG')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        american_express_photo= tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\american_express.PNG')
        american_express_label=tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image=american_express_photo

        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()

        credits=tk.Label(bottom_frame,text='PAYSRM Bank',font=('orbitron',15)).pack()



################## MENU PAGE #################################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAY SRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Main Menu',font=('orbitron',20),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)
        slection_label=tk.Label(self,text='Please make a selection',font=('orbitron',20),fg='white',bg='#3d3d5c')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='Withdraw',font=('orbitron',15),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=20,padx=100)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='Deposit',font=('orbitron',15),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=20)
        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='Balance',font=('orbitron',15),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=394)

        def mini():
            controller.show_frame('MinistatementPage')

        mini_button=tk.Button(button_frame,text='Mini Statement',font=('orbitron',15),command=mini,relief='raised',borderwidth=3,width=30,height=4)
        mini_button.grid(row=1,column=1,pady=5,padx=394)
            
        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='Personal Info',font=('orbitron',15),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.grid(row=2,column=0,pady=20)

        def exit():
            controller.show_frame('StartPage')


        exit_button=tk.Button(button_frame,text='Exit',font=('orbitron',15),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=2,column=1,pady=5)

################## WITHDRAW PAGE #################################
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAYSRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Choose the amount you want to withdraw',font=('orbitron',15),fg='white',bg='#3d3d5c')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            global val
            val=amount
            if amount>current_balance:
                messagebox.showwarning('WARNING','Not sufficient funds!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                messagebox.showinfo('TRANSACTION','Done Successfully!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                controller.show_frame('MenuPage')
                mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
                mycursor=mydb.cursor()
                mycursor.execute("use paysrm")
                mycursor.execute(f"update paysrm set balance ={current_balance} where accid = {username1} ")
                acc={username1}
                mydb.commit()
                prtpdfw()

                try:
                    f=open("{}.csv".format(acc),'r',newline="\n")
                    f.close()
                    f=open("{}.csv".format(acc),'a',newline="\n")
                    col=["date","withdrawls","deposits","balance"]
                    today = date.today()
                    dt = today.strftime("%d/%m/%Y")
                    withdrawls= amount
                    deposits= "-"
                    balance= current_balance
                    tr=[dt,withdrawls,deposits,balance]
                    file=csv.writer(f)
                    file.writerow(tr)
                    f.close()
                    
                        
                except:
                    f=open("{}.csv".format(acc),'w',newline="\n")
                    col=["date","withdrawls","deposits","balance"]
                    today = date.today()
                    dt = today.strftime("%d/%m/%Y")
                    withdrawls= amount
                    deposits= "-"
                    balance= current_balance
                    tr=[dt,withdrawls,deposits,balance]
                        
                    file=csv.writer(f)
                    file.writerow(col)
                    file.writerow(tr)
                    f.close()
                    

                controller.show_frame('MenuPage')



        twenty_button=tk.Button(button_frame,text='₹20000',font=('orbitron',12),command=lambda:withdraw(20000),relief='raised',borderwidth=3,width=30,height=4)
        twenty_button.grid(row=0,column=0,pady=5)

        fourty_button=tk.Button(button_frame,text='₹40000',font=('orbitron',12),command=lambda:withdraw(40000),relief='raised',borderwidth=3,width=30,height=4)
        fourty_button.grid(row=1,column=0,pady=5)

        sixty_button=tk.Button(button_frame,text='₹60000',font=('orbitron',12),command=lambda:withdraw(60000),relief='raised',borderwidth=3,width=30,height=4)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button=tk.Button(button_frame,text='₹80000',font=('orbitron',12),command=lambda:withdraw(80000),relief='raised',borderwidth=3,width=30,height=4)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button=tk.Button(button_frame,text='₹100000',font=('orbitron',12),command=lambda:withdraw(100000),relief='raised',borderwidth=3,width=30,height=4)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=794)

        two_hundred_button=tk.Button(button_frame,text='₹200000',font=('orbitron',12),command=lambda:withdraw(200000),relief='raised',borderwidth=3,width=30,height=4)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button=tk.Button(button_frame,text='₹300000',font=('orbitron',12),command=lambda:withdraw(300000),relief='raised',borderwidth=3,width=30,height=4)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('orbitron',12),textvariable=cash,width=28,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='Other amount in rupees',font=('orbitron',13),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#33334d',bg='#33334d',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            global val
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('WARNING','Not sufficient funds!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('WARNING','Invalid Input!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION','Done Successfully!')
                    controller.show_frame('MenuPage')
                    mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
                    mycursor=mydb.cursor()
                    mycursor.execute("use paysrm")
                    mycursor.execute(f"update paysrm set balance ={current_balance} where accid = {username1} ")
                    acc={username1}
                    mydb.commit()
                    prtpdfw()
                    try:
                        f=open("{}.csv".format(acc),'r',newline="\n")
                        f.close()
                        f=open("{}.csv".format(acc),'a',newline="\n")
                        col=["date","withdrawls","deposits","balance"]
                        today = date.today()
                        dt = today.strftime("%d/%m/%Y")
                        withdrawls=val
                        deposits= "-"
                        balance= current_balance
                        tr=[dt,withdrawls,deposits,balance]
                        file=csv.writer(f)
                        file.writerow(tr)
                        f.close()
                        
                        
                    except:
                        f=open("{}.csv".format(acc),'w',newline="\n")
                        col=["date","withdrawls","deposits","balance"]
                        today = date.today()
                        dt = today.strftime("%d/%m/%Y")
                        withdrawls=val
                        deposits= "-"
                        balance= current_balance
                        tr=[dt,withdrawls,deposits,balance]
                        
                        file=csv.writer(f)
                        file.writerow(col)
                        file.writerow(tr)
                        f.close()
                        
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)
        
        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Back',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

    
       

################## DEPOSIT PAGE #################################
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAYSRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        enter_amount_label=tk.Label(self,text='Enter the amount you want to deposit',font=('orbitron',20),bg='#3d3d5c',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('orbitron',15),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            global val
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('WARNING','Improper Amount Entered!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITION','Done Successfully!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Goodluck#04*")
                    mycursor=mydb.cursor()
                    mycursor.execute("use paysrm")
                    mycursor.execute(f"update paysrm set balance ={current_balance} where accid = {username1} ")
                    acc={username1}
                    mydb.commit()
                    prtpdfd()

                    try:
                        f=open("{}.csv".format(acc),'r',newline="\n")
                        f.close()
                        f=open("{}.csv".format(acc),'a',newline="\n")
                        col=["date","withdrawls","deposits","balance"]
                        today = date.today()
                        dt = today.strftime("%d/%m/%Y")
                        withdrawls="-"
                        deposits= val
                        balance= current_balance
                        tr=[dt,withdrawls,deposits,balance]
                        file=csv.writer(f)
                        file.writerow(tr)
                        f.close()
                        
                        
                    except:
                        f=open("{}.csv".format(acc),'w',newline="\n")
                        col=["date","withdrawls","deposits","balance"]
                        today = date.today()
                        dt = today.strftime("%d/%m/%Y")
                        withdrawls="-"
                        deposits= val
                        balance= current_balance
                        tr=[dt,withdrawls,deposits,balance]
                        
                        file=csv.writer(f)
                        file.writerow(col)
                        file.writerow(tr)
                        f.close()
                        

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('orbitron',15),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)

        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Back',font=('orbitron',12),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

################## MINI STATEMENT PAGE #################################
class MinistatementPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAYSRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        today=date.today()

        from_label = tk.Label(self, text='From', font=('orbitron',13),fg='white', bg='#3d3d5c', anchor='w')
        from_label.pack()
        
        cal1= Calendar(self, selectmode = 'day',year = today.year, month = today.month,day = today.day)
        cal1.pack(pady = 25)


        
        to_label = tk.Label(self, text='To', font=('orbitron',13),fg='white', bg='#3d3d5c', anchor='w')
        to_label.pack()

        cal2= Calendar(self, selectmode = 'day',year = today.year, month = today.month,day = today.day)
        cal2.pack(pady = 20)


        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def caldate():
            global fromdate
            global todate
            fromdate=cal1.get_date()
            todate=cal2.get_date()

            tran()

        def ok():
            controller.show_frame('MenuPage')

        ok_button=tk.Button(button_frame,command=caldate,text='Okay',font=('orbitron',15),relief='raised',borderwidth=3,width=23,height=6)
        ok_button.pack(side=RIGHT,pady=5,padx=5)
            
        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Back',font=('orbitron',15),relief='raised',borderwidth=3,width=23,height=6)
        menu_button.pack(side=LEFT,padx=5,pady=5)


     
        
################## BALANCE PAGE #################################
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAYSRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Balance', font=('orbitron',13),fg='white', bg='#3d3d5c', anchor='w')
        balance_label.pack()

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('orbitron',16),fg='white', bg='#33334d', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Back',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Exit',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Current Balance: ₹'+str(self.controller.shared_data['Balance'].get()))

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='PAYSRM ATM',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Personal Info',font=('orbitron',15),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both')

        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Goodluck#04*")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists paysrm")
        mycursor.execute("use paysrm")


        name_info = tk.Label(upperframe, text=f'Name : {user_display_name}', font=('orbitron',16),fg='white', bg='#33334d')
        name_info.pack(pady=5)

        accid_info = tk.Label(upperframe, text=f'Account No. : {username1}', font=('orbitron',16),fg='white', bg='#33334d')
        accid_info.pack(pady=5)


        def changepass():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Change Password',command=change,font=('orbitron',15),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=30,padx=20)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Back',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)


################## CLASS  DEFINE FUNCTION #################################
def abcd():

        app = SampleApp()
        app.mainloop()


############################################################ REGISTER/LOGIN ############################################################


def password_not_recognised():
  messagebox.showwarning('WARNING',('Invalid Password!'))

def password_not_match():
    messagebox.showwarning('WARNING',('Password Does Not Match!'))

def password_ch_suc():
    messagebox.showwarning('WARNING',('Password Changed Sucessfully!'))



################## ABOUT SCREEN #################################
def about():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("About")
    screen3.state("zoomed")
    screen3.configure(bg='lightblue')
    screen3.iconphoto(False,tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\abc.PNG'))
    Label(screen3,bg='lightblue', text = "Created and Developed by Pal\n 12 CS Project \n Tkinter python with Mysql database \n Database paysrm \n Table paysrm",font = ("orbitron", 10,'bold')).pack()
    webbrowser.open("https://sites.google.com/view/srmbankings/home")
################## CHANGE PASSWORD VERIFY ##################################

def pass_verify():
    global oldpass
    global npass1
    global npass2
    mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
    mycursor=mydb.cursor()
    mycursor.execute("use paysrm")
    mycursor.execute("select accid from paysrm ")
    accid=mycursor.fetchall()
    accid={username1}
    mycursor.execute(f"select password from paysrm where accid= {username1}")
    values=mycursor.fetchall()
    opass=oldpass.get()
    npass1=newpass1.get()
    npass2=newpass2.get()

    for i in accid:
        accid=int(i)
    print(accid)

    for i in values:
        for j in i:
            values=str(j)
            
    if str(values)==str(opass):
        if npass1==npass2:
            mycursor.execute("update paysrm set password='{}' where accid={}".format(npass1,accid))
            mydb.commit()
            password_ch_suc()
            screen4.destroy()

        else:
            password_not_match()
    else:
        password_not_recognised()
        
    
##################CHANGE PASSWORD SCREEN###########################

def change():
    global screen4
    global name
    global oldpass
    global newpass1
    global newpass2
    
    global oldpass_entry
    global newpass_entry1
    global newpass_entry2
    
    screen4 = Tk()
    screen4 = Toplevel(screen4)
    screen4.title("Change Password")
    screen4.state("zoomed")
    screen4.configure(bg='#33334d')
    oldpass = StringVar(screen4)
    newpass1 = StringVar(screen4)
    newpass2 = StringVar(screen4)
    
    Label(screen4,fg="white",bg='#33334d', text = "Change Password",font = ("arial", 25,'bold')).pack()
    Label(screen4, text = "",fg="white",bg='#33334d').pack()
    Label(screen4, text = "Old Password",font = ("orbitron", 20),fg="white",bg='#33334d').pack()
    oldpass_entry = Entry(screen4,font = ("orbitron",20), textvariable = oldpass)
    oldpass_entry.pack()

    Label(screen4, text = "",bg='#33334d').pack()
    Label(screen4, text = "New Password",font = ("orbitron", 20),fg="white",bg='#33334d').pack()
    newpass_entry1 = Entry(screen4,font = ("orbitron",20), textvariable = newpass1)
    newpass_entry1.pack()

    Label(screen4, text = "",bg='#33334d').pack()
    Label(screen4, text = "Renter your New Password",font = ("orbitron", 20),fg="white",bg='#33334d').pack()
    newpass_entry2 = Entry(screen4,font = ("orbitron",20), textvariable = newpass2)
    newpass_entry2.pack()

    button_frame=tk.Frame(screen4,bg='#33334d')
    button_frame.pack(fill='both')

    def chps():
            controller.show_frame('MenuPage')

    chps_button=tk.Button(button_frame,text='Change Password',command=pass_verify,font=('orbitron',20),relief='raised',borderwidth=3,width=23,height=4)
    chps_button.pack(pady=30,padx=20)

################## TRANSACTIONS #################################
def tran():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
    mycursor=mydb.cursor()
    mycursor.execute("use paysrm")
    mycursor.execute("select accid from paysrm")
    acc=mycursor.fetchall()
    acc=acc[0][0]
    acc={username1}
    for i in acc:
        acc=i
    
    mycursor.execute(f"select name from paysrm where accid= {username1} ")
    Name=mycursor.fetchall()
    Name=Name[0][0]

          
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size =15)

    today = date.today()
    dte = today.strftime("%d/%m/%Y")
    tim=time.strftime('%I:%M %p')
    pdf.cell(200, 10, txt = "SRM banks",ln = 1, align = 'C')


    pdf.cell(200,10, txt = "MINI STATEMENT",ln = 2, align = 'C')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')

    pdf.cell(20 ,10, txt = "Name :                            {}".format(Name),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Account number :            {}".format(acc),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "------------------------------------------------------------------------------------------------------",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "DATE          WITHDRAWL          DEPOSIT          BALANCE",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "------------------------------------------------------------------------------------------------------",ln=2, align = 'L')
    f=open('{}.csv'.format({username1}),"r",newline='\n')
    s=csv.reader(f)
    
    for i in s:
        if i[0] in pd.date_range(start=fromdate,end=todate):
            q=''
            for j in i:
                q=q+str(j)+'                '
            pdf.cell(20 ,10, txt = q,ln=2, align = 'L')

    f.close()
            
    pdf.output("MINISTATEMENT.pdf")  
    os.system("MINISTATEMENT.pdf")

##################PRINT PDF-DEPOSIT###############################################
def prtpdfd():
     global screen5
     screen5 = Tk()
     screen5.title("Print reciept")
     screen5.geometry("380x90+750+230")
     screen5.configure(bg='#33334d')
     button_frame=tk.Frame(screen5,bg='#33334d')
     button_frame.pack(fill='both')
     prtpdfd_button=tk.Button(button_frame,text='Print pdf',command=crpdfd,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
     prtpdfd_button.pack(pady=30,padx=20)
     

####################CREATING PDF-(DEPOSIT)########################################
def crpdfd():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
    mycursor=mydb.cursor()
    mycursor.execute("use paysrm")
    mycursor.execute("select accid from paysrm")
    acc=mycursor.fetchall()
    acc=acc[0][0]
    acc={username1}
    for i in acc:
        acc=i
    
    mycursor.execute(f"select name from paysrm where accid= {username1} ")
    Name=mycursor.fetchall()
    Name=Name[0][0]
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size =15)

    today = date.today()
    dte = today.strftime("%d/%m/%Y")
    tim=time.strftime('%I:%M %p')
    pdf.cell(200, 10, txt = "SRM banks",ln = 1, align = 'C')
    amt=val


    pdf.cell(200,10, txt = "Deposit reciept",ln = 2, align = 'C')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')

    pdf.cell(20 ,10, txt = "Name :                            {}".format(Name),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Account number :            {}".format(acc),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Amount :                          {}".format(amt),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Date :                              {}".format(dte),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Time :                              {}".format(tim),ln=2, align = 'L')



    pdf.output("GFG.pdf")  
    os.system("GFG.pdf")


##################PRINT PDF-WITHDRAW###############################################
def prtpdfw():
     global screen5
     screen5 = Tk()
     screen5.title("Print reciept")
     screen5.geometry("380x90+750+230")
     screen5.configure(bg='#33334d')
     button_frame=tk.Frame(screen5,bg='#33334d')
     button_frame.pack(fill='both')
     prtpdfw_button=tk.Button(button_frame,text='Print pdf',command=crpdfw,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
     prtpdfw_button.pack(pady=30,padx=20)
     

####################CREATING PDF-WITHDRAW########################################
def crpdfw():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
    mycursor=mydb.cursor()
    mycursor.execute("use paysrm")
    mycursor.execute("select accid from paysrm")
    acc=mycursor.fetchall()
    acc=acc[0][0]
    acc={username1}
    for i in acc:
        acc=i
    
    mycursor.execute(f"select name from paysrm where accid= {username1} ")
    Name=mycursor.fetchall()
    Name=Name[0][0]
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size =15)

    today = date.today()
    dte = today.strftime("%d/%m/%Y")
    tim=time.strftime('%I:%M %p')
    pdf.cell(200, 10, txt = "SRM banks",ln = 1, align = 'C')
    amt=val


    pdf.cell(200,10, txt = "Withdraw reciept",ln = 2, align = 'C')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "                 ",ln=2, align = 'L')

    pdf.cell(20 ,10, txt = "Name :                            {}".format(Name),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Account number :            {}".format(acc),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Amount :                          {}".format(amt),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Date :                              {}".format(dte),ln=2, align = 'L')
    pdf.cell(20 ,10, txt = "Time :                              {}".format(tim),ln=2, align = 'L')



    pdf.output("GFG.pdf")  
    os.system("GFG.pdf")



    
   

################## WARNING_SCREEN #################################
def user_not_found():
  messagebox.showwarning('WARNING',('No AccountID Found !'))

################## REGISTER USER SCREEN #################################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get()

  ################## MYSQL DATABASE ##################
  global mycursor
  mydb=mysql.connector.connect(host="localhost",user="root",password="Goodluck#04*")
  mycursor=mydb.cursor()
  mycursor.execute("create database if not exists paysrm")
  mycursor.execute("use paysrm")
  mycursor.execute("create table if not exists paysrm(accid int(10) primary key,name varchar(30),password char(20),balance char(30))")
  mydb.commit()

  mycursor.execute('select accid from paysrm')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if username_info in b:
    messagebox.showwarning('WARNING',('AccountID already exists!'))

    password_entry.delete(0,END)
    name_entry.delete(0,END)
  elif name_info=='' :
        messagebox.showwarning('WARNING',('No Name Given!'))
        password_entry.delete(0,END)
  elif password_info=='' :
        messagebox.showwarning('WARNING',('No Password Given!'))
  else:
        balance_inti='0.00'
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        screen1.destroy()
        mycursor.execute("insert into paysrm values('"+username_info+"','"+name_info+"','"+password_info+"','"+balance_inti+"')")
        mydb.commit()
        messagebox.showinfo('Registration',('Done Successfully!'))


################## LOGIN VERIFY SCREEN #################################
def login_verify():
    global current_balance
    global username1
    global name_display
    global user_display_name

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    mydb = mysql.connector.connect(host="localhost", user="root", password="Goodluck#04*")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS paysrm")
    mycursor.execute("USE paysrm")

    mycursor.execute("SELECT accid FROM paysrm")
    values = mycursor.fetchall()
    user_acc = [i[0] for i in values]

    if username1.isalpha():
        messagebox.showwarning('WARNING', 'Wrong Input!')
    elif username1.strip() == '':
        messagebox.showwarning('WARNING', 'No Account ID Given!')
    elif username1.isalnum() and username1.isdigit():
        if int(username1) in user_acc:
            mycursor.execute("SELECT password FROM paysrm WHERE accid = %s", (username1,))
            values = mycursor.fetchall()
            user_pass = [i[0] for i in values]

            if not user_pass:
                user_not_found()
                return

            user_pass_1 = str(user_pass[0])

            if password1 == '':
                messagebox.showwarning('WARNING', 'No Password Given!')
            elif password1 == user_pass_1:
                # Get user display name
                mycursor.execute("SELECT name FROM paysrm WHERE accid = %s", (username1,))
                values = mycursor.fetchall()
                user_name = [i[0] for i in values]
                user_display_name = str(user_name[0])

                # Get user balance
                mycursor.execute("SELECT balance FROM paysrm WHERE accid = %s", (username1,))
                values = mycursor.fetchall()
                user_balance = [i[0] for i in values]

                if not user_balance:
                    user_not_found()
                    return

                current_balance = float(user_balance[0])

                # Launch main GUI
                screen2.destroy()
                screen.destroy()
                abcd()
            else:
                password_not_recognised()
        else:
            user_not_found()
    else:
        user_not_found()


################## REGISTER DISPLAY SCREEN #################################
def register():
  global screen1
  global password_entry
  global username_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.state("zoomed")
  screen1.configure(bg='lightblue')
  screen1.iconphoto(False,tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\abc.PNG'))

  photo = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\login_person.PNG")
  label = Label(screen1,image=photo,bg='lightblue')
  label.image = photo
  label.pack(pady=5)

  global username
  global password
  global name

  global username_entry
  global password_entry
  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()

  Label(screen1, text = "Please enter details below to register",bg='lightblue',font = ("orbitron", 25)).pack()

  Label(screen1, text = "",bg='lightblue').pack()
  Label(screen1, text = "Name",font = ("orbitron", 25),bg='lightblue').pack()
  name_entry = Entry(screen1,font = ("orbitron",25), textvariable = name)
  name_entry.pack()

  Label(screen1, text = "Account No.",font = ("orbitron", 25),bg='lightblue').pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("orbitron", 25),bg='lightblue').pack()
  #username_entry = Entry(screen1, textvariable = username)
  #username_entry.pack()

  Label(screen1, text = "Pin",font = ("orbitron", 25),bg='lightblue').pack()
  password_entry =  Entry(screen1,font = ("orbitron",25), textvariable = password)
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  Label(screen1, text = "",bg='lightblue').pack()

  img1 = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\register_final.PNG")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen1,command = register_user,image=photoimage1,bg='lightblue',activebackground='lightblue',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

################## LOGIN DISPLAY SCREEN #################################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.state("zoomed")
  screen2.configure(bg='lightblue')
  screen2.iconphoto(False,tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\abc.PNG'))

  photo = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\login_person.PNG")
  label = Label(screen2,image=photo,bg='lightblue')
  label.image = photo
  label.pack(pady=5)

  Label(screen2, text = "Please enter details below to login",bg='lightblue',font = ("orbitron", 30)).pack()
  Label(screen2, text = "",bg='lightblue').pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  
  password_verify = StringVar()


  global username_entry1
  global password_entry1

  Label(screen2, text = "Account No.",bg='lightblue',font = ("orbitron", 25)).pack()
  username_entry1 = Entry(screen2,font = ("orbitron",25) ,textvariable = username_verify)
  username_entry1.pack()

  Label(screen2, text = "",bg='lightblue').pack()
  Label(screen2, text = "Pin",bg='lightblue',font = ("orbitron", 25)).pack()
  password_entry1 = Entry(screen2,font = ("orbitron",25), textvariable = password_verify)
  password_entry1.config(fg='black',show='●')
  password_entry1.pack()
  Label(screen2, text = "",bg='lightblue').pack()

  img1 = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\login_final.PNG")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen2,command = login_verify,image=photoimage1,bg='lightblue',activebackground='lightblue',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

################## REGISTER/LOGIN SCREEN #################################
def main_screen():
  global screen
  screen = Tk()
  screen.state("zoomed")
  screen.title("PAYSRM")
  screen.configure(bg='lightblue')
  screen.iconphoto(False,tk.PhotoImage(file='F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\abc.PNG'))


  Label(text = "PAY SRM",fg='white', bg = "grey", width = "300", height = "2", font = ("orbitron", 9,'bold')).pack()
  Label(text = "",bg='lightblue').pack()

  img = ImageTk.PhotoImage(Image.open("F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\bankk.PNG"))
  panel = Label(screen, image = img,bg='lightblue')
  panel.pack()

  photo1 = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\login_final.PNG")
  photoimage1 = photo1.subsample(2, 2)
  Button(command = login,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage1).pack(pady=5)

  Label(text = "",bg='lightblue',).pack()

  photo2 = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\register_final.PNG")
  photoimage2 = photo2.subsample(2, 2)
  Button(command = register,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage2).pack(pady=5)

  Label(text = "",bg='lightblue').pack()

  photo3 = PhotoImage(file="F:\\COURSES AND CODES\\PYTHON PROJECTS SOURCE CODE\\ATM-GROUP PROJECT\\IMAGES\\about.PNG")
  photoimage3 = photo3.subsample(2, 2)
  Button(command = about,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage3).pack(pady=5)
  Label(text="",bg="lightblue").pack()
  screen.mainloop()

main_screen()


