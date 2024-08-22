from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()==''or usernameEntry.get()==''or passwordEntry=='' or confirmEntry=='':
        messagebox.showerror('Error','All Fields Are Requires')

    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')

    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Condtions')
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='Root@123',database='userdata')
            mycursor=conn.cursor()
        except pymysql.Error as e:
            print(f"Error connecting to MySQL: {e}")
            messagebox.showerror('Error', 'Unable to connect to the database.')
            # Exit the function or handle the error appropriately
            return
        try:
            query='create database if not exists userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table if not exists data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)

        except pymysql.Error as e:
            #print(f"Error executing query:{e}")
            # Log the error or show an error message in a GUI application
            #return
            mycursor.execute('use userdata')

        query='insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Registration is successful')
        clear()
        signup_window()
        import signin2


def login_page():
    signup_window.destroy()
    import signin2
    

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='White',fg='firebrick1')
heading.grid(row=0,column=0,padx=9,pady=9)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='grey3')
emailLabel.grid(row=1,column=0,sticky='W',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='grey3',bg='grey99')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='grey3')
usernameLabel.grid(row=3,column=0,sticky='W',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='grey3',bg='grey99')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='grey3')
passwordLabel.grid(row=5,column=0,sticky='W',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='grey3',bg='grey99')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='grey3')
confirmLabel.grid(row=7,column=0,sticky='W',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='grey3',bg='grey99')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termscondition=Checkbutton(frame,text='I agree to the terms & conditions',font=('Microsoft Yahei UI Light',9,'bold')
                           ,fg='grey3',bg='white',activebackground='white',activeforeground='grey3',
                           cursor='hand2',variable=check)
              
termscondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',15,'bold'),bd=0,bg='skyblue',
                    fg='grey3',activebackground='dodgerblue1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)


alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white', fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',
                    fg='blue',bd=0,cursor='hand2',activebackground='white',
                    activeforeground='blue',command=login_page)

loginButton.place(x=160,y=402)


signup_window.mainloop()
