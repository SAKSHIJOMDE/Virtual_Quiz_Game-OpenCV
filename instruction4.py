from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def start_page():
    inst.destroy()
    import main1

inst=Tk()
inst.title('VARTUAL QUEZE GAME')
inst.resizable(False,False)

background=ImageTk.PhotoImage(file='images/ins.png')

bgLabel=Label(inst,image=background)
bgLabel.grid()

frame=Frame(inst,bg='white')
frame.place(x=554,y=100) 



StartButton=Button(inst,text='Start',font=('Open sans',25,'bold underline'),fg='gold1',
                   bg='deeppink1',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,
                   command=start_page)
StartButton.place(x=720,y=500)


inst.mainloop()