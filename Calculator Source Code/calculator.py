from tkinter import *
from tkinter import messagebox 

root=Tk()
root.title("Calculator")
root.geometry("700x650")
root.resizable(False,False)
Top = Frame(root,width = 400, height=600,relief=SUNKEN)
Top.pack(side=TOP)

f1 = Frame(root,width = 400, height = 600)
f1.pack(side=LEFT)

f2 = Frame(root,width = 400, height = 600)
f2.pack(side=TOP)

l1=Label(Top,font=('arial',50,'bold'),text="Calculator",fg="Steel Blue",bd=10,anchor='w')
l1.grid(row=0,column=0)

operator=""
count=0

def get_text(text):
    return text

def set_text(text):
    global count
    txtDisplay.insert(count,text)
    count+=1
    global operator
    operator+=get_text(str(text))
    return

def equals():
    #try block to check for ZeroDivisionError
    try: 
        global operator
        global count
        sumup =eval(str(operator))
        txtDisplay.delete('0',END)
        set_text(sumup)
        operator=str(sumup)
    except ZeroDivisionError:
        messagebox.showerror("ZeroError","Division by zero is not defined")
        

def clear():
    global operator
    txtDisplay.delete('0',END)
    operator=""

def delete():
    global operator
    operator=operator[0:-1]
    txtDisplay.delete('0',END)
    txtDisplay.insert('0',operator)


txtDisplay = Entry(Top,font=('arial',20,'bold'), bd=30, insertwidth=4, bg='white',justify='right')
txtDisplay.grid(columnspan=4)

b7= Button(f1, text="7", width = 4, height = 1,font=('arial',40,'bold'), command=lambda: set_text(7))
b7.grid(row=0,column=0)



b8 = Button(f1,text="8",width =4, height =1, font=('arial',40,'bold'),command=lambda: set_text(8))
b8.grid(row=0,column=1)

b9 = Button(f1,text="9",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(9))
b9.grid(row=0,column=2)


b_add = Button(f1,text="+",width =4, height =1, font=('arial',40,'bold'),command=lambda: set_text("+"))
b_add.grid(row=0,column=3)

b_mult = Button(f1,text= "*", width = 4, height =1, font=('arial',40,'bold'), command=lambda: set_text("*"))
b_mult.grid(row=0,column=4)

b4 = Button(f1,text="4",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(4))
b4.grid(row=1,column=0)

b5 = Button(f1,text="5",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(5))
b5.grid(row=1,column=1)

b6 = Button(f1,text="6",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(6))
b6.grid(row=1,column=2)

b_sub = Button(f1,text="-",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text("-"))
b_sub.grid(row=1,column=3)

b_div = Button(f1,text="/",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text("/"))
b_div.grid(row=1,column=4)

b1 = Button(f1,text="1",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(1))
b1.grid(row=2,column=0)

b2 = Button(f1,text="2",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(2))
b2.grid(row=2,column=1)

b3 = Button(f1,text="3",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(3))
b3.grid(row=2,column=2)

b0 = Button(f1,text="0",width = 4, height = 1, font=('arial',40,'bold'),command=lambda: set_text(0))
b0.grid(row=3,column=0,columnspan=3,sticky=W+E)

b_equal = Button(f1,text="=",width = 4, height = 1, font=('arial',40,'bold'),command=equals )
b_equal.grid(row=3,column=3,columnspan=3,sticky=W+E)

b_clear = Button(f1,text="C",width = 4, height = 1, font=('arial',40,'bold'),command=clear)
b_clear.grid(row=2,column=3)

b_del = Button(f1,text="Del",width = 4, height = 1, font=('arial',40,'bold'),command=delete)
b_del.grid(row=2,column=4)

root.mainloop()


