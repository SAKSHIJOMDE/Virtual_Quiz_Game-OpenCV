from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def forget_pass():
    def change_password():
        if user_entry.get()==''or newpass_entry.get()==''or confpass_entry.get()=='':
            messagebox.showerror('Error','All Fileds Are Required',parent=window)

        elif newpass_entry.get()!=confpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching',parent=window)
        
        else:
            conn=pymysql.connect(host='localhost',user='root',password='Root@123',database='userdata')
            mycursor=conn.cursor()

            query='Select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()

            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)

            else:
                query='Update data set password=%'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showerror('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()

    window=Toplevel()
    window.title('Change Password')

    bgPic= ImageTk.PhotoImage(file='images/background.jpg')
    bglabel=Label(window,image=bgPic)
    bglabel.grid()
   
    headind_label=Label(window,text='RESET PASSWORD',font=('Microsoft Yahei UI Light','18','bold'),bg='white',fg='magenta2')
    headind_label.place(x=490, y=50)
    
    #Username
    userLabel=Label(window,text='Username',font=('Microsoft Yahei UI Light','12','bold'),bg='white',fg='orchid1')
    userLabel.place(x=480, y=100)

    user_entry=Entry(window,width=25,fg='magenta2',font=('Microsoft Yahei UI Light','10','bold'),bd=0)
    user_entry.place(x=480,y=130)

    Frame(window,width=250,height=2,bg='orchid1').place(x=480,y=150)
    
    #NewPassword
    passwordLabel=Label(window,text='New Password',font=('Microsoft Yahei UI Light','12','bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=480, y=180)

    newpass_entry=Entry(window,width=25,fg='magenta2',font=('Microsoft Yahei UI Light','10','bold'),bd=0)
    newpass_entry.place(x=480,y=210)

    Frame(window,width=250,height=2,bg='orchid1').place(x=480,y=230)

    #Confirm PasWord
    confpasswordLabel=Label(window,text='Confirm Password',font=('Microsoft Yahei UI Light','12','bold'),bg='white',fg='orchid1')
    confpasswordLabel.place(x=480, y=260)

    confpass_entry=Entry(window,width=25,fg='magenta2',font=('Microsoft Yahei UI Light','10','bold'),bd=0)
    confpass_entry.place(x=480,y=290)

    Frame(window,width=250,height=2,bg='orchid1').place(x=480,y=320)

    submitButton=Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Microsoft Yahei UI Light','16','bold'),
                        width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',
                        command=change_password)
    submitButton.place(x=480,y=370)
    window.mainloop()


def login_user():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    
    else:
        try: 
            conn=pymysql.connect(host='localhost',user='root',password='Root@123')
            mycursor=conn.cursor()

        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        
        query='use userdata'
        mycursor.execute(query)
        query='Select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid username or passwird')
        else:
            messagebox.showinfo('Welcome','Login is Sucessful')
            login_window.destroy()
            import instruction4

def signup_page():
    login_window.destroy()
    import signup3

def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
     openeye.config(file='images/openeye.png')
     passwordEntry.config(show='')
     eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI Part
login_window=Tk()
login_window.resizable(0,0)
login_window.title('VARTUAL QUEZE GAME')

bgImage=ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
bgLabel.pack()

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',20,'bold'),bg='White',fg='firebrick1')
heading.place(x=620,y=120)

#Username
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='grey4')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=1,bg='grey16')
frame1.place(x=580,y=222)

#Passworsd Entry

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='grey4')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=1,bg='grey16')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='images/openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=hide)
eyeButton.place(x=800,y=250)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                 cursor='hand2',font=('Microsoft Yahei UI Light',8,'bold'),fg='grey4',activeforeground='grey4',
                 command=forget_pass)
forgetButton.place(x=715,y=295)


loginButton=Button(login_window,text='Login',font=('Open sans',16,'bold'),fg='grey3',
                   bg='skyblue',activeforeground='grey4',activebackground='white',cursor='hand2',bd=0,width=19,
                   command=login_user)
loginButton.place(x=578,y=350)

orLabel=Label(login_window,text='---------------OR---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

#facebook_logo=PhotoImage(file='facebook.png')
#fbLabel=Label(login_window,image=facebook_logo,bg='white')
#fbLabel.place(x=640,y=440)

#google_logo=PhotoImage(file='google.png')
#googleLabel=Label(login_window,image=google_logo,bg='white')
#googleLabel.place(x=750,y=440)


signup=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signup.place(x=590,y=500)

newaccButton=Button(login_window,text='Create new one',font=('Open sans',9,'bold underline'),fg='blue',
                   bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,
                   command=signup_page)
newaccButton.place(x=727,y=500)

login_window.mainloop()