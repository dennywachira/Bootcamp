#simple calculator Project

from tkinter import *

root=Tk()
root.geometry("354x450")
root.title("Simple Calculator")

root.config(background='black')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
mytext=Entry(root,font=("open sans",12,'bold'),textvar=textin,width=25,bd=5,bg='white')
mytext.pack()

but1=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("open sans",12,'bold'))
but1.place(x=10,y=100)

but2=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("open sans",12,'bold'))
but2.place(x=10,y=170)

but3=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("open sans",12,'bold'))
but3.place(x=10,y=240)

but4=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("open sans",12,'bold'))
but4.place(x=75,y=100)

but5=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("open sans",12,'bold'))
but5.place(x=75,y=170)

but6=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("open sans",12,'bold'))
but6.place(x=75,y=240)

but7=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("open sans",12,'bold'))
but7.place(x=140,y=100)

but8=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("open sans",12,'bold'))
but8.place(x=140,y=170)

but9=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("open sans",12,'bold'))
but9.place(x=140,y=240)

but0=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("open sans",12,'bold'))
but0.place(x=10,y=310)

butdot=Button(root,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("open sans",12,'bold'))
butdot.place(x=75,y=310)

butpl=Button(root,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("open sans",12,'bold'))
butpl.place(x=205,y=100)

butsub=Button(root,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("open sans",12,'bold'))
butsub.place(x=205,y=170)

butml=Button(root,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("open sans",12,'bold'))
butml.place(x=205,y=240)

butdiv=Button(root,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("open sans",12,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(root,padx=14,pady=119,bd=4,bg='white',text="clear",command=clrbut,font=("open sans",12,'bold'))
butclear.place(x=270,y=100)

butequal=Button(root,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("open sans",12,'bold'))
butequal.place(x=10,y=380)
root.mainloop()