from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def start_page():
    inst.destroy()
    import signin2

inst=Tk()
inst.title('VIRTUAL QUIZE GAME')
inst.resizable(False,False)

background=ImageTk.PhotoImage(file='images/VartualQueze.png')

bgLabel=Label(inst,image=background)
bgLabel.grid()

frame=Frame(inst,bg='white')
frame.place(x=554,y=100)

StartButton=Button(inst,text='PLAY',font=('Open sans',20,'bold'),fg='gold1',
                   bg='deeppink1',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,
                   command=start_page)
StartButton.place(x=220,y=400)


inst.mainloop()