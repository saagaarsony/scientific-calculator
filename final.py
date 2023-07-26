import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox
from tkinter import *
import math

splesh = ttk.Window(themename='superhero')
splesh.geometry('500x500')
splesh.overrideredirect(True)
splesh.eval('tk::PlaceWindow  . center')



slbl=Label(splesh, text='WelCome To The Total',font=('corbel',15,'bold'))
slbl.pack(pady=80 )

Label(splesh, font=('corbel', 12), text="IMPORTANT SHORT-KEYS", fg='RED').place(x=40, y=200)
Label(splesh, font=('corbel', 8), text="*     PRESS ESCAPE FOR CLEAR SCREEN", fg='green',).place(x=10, y=240)
Label(splesh, font=('corbel', 8), text="*     PRESS DOUBLE ESCAPE FOR EXIT SCREEN", fg='green').place(x=10, y=280)
Label(splesh, font=('corbel', 8), text="*     PRESS ENTER FOR EQULE", fg='green').place(x=10, y=320)

def main_w():
 splesh.destroy()
 sa= ttk.Window(themename= 'pulse')
 sa.title("SS CALCULATOR")
 
 sa.geometry('323x475')
 sa.iconbitmap('S:\p project\icon\icon.ico')
 
 sa.eval('tk::PlaceWindow  . center')

 

 sa.resizable(False, False)

 menu1 = Menu(sa)
 sa.config(menu=menu1)

 def sciencetific():
    #slbl = Label(sa, text='I Am A Scientific Calculator').pack()
    sa.resizable(False,False)
    sa.geometry('410x530')

 def normal():
    #slbl1 = Label(sa, text='I am A Normal Calculator').pack() 
    sa.resizable(False,False)
    sa.geometry('325x445')

 smenu = Menu(menu1)
 menu1.add_cascade(label='MENU', menu=smenu)
 smenu.add_command(label='Scientific', command=sciencetific)
 smenu.add_command(label='Normal', command=normal)
 smenu.add_separator()
 smenu.add_command(label='Close Window', command=quit)
 
 
 entry = tk.Entry(sa,width=34, bd=10, font=("time new roman",10, 'bold'))
 entry.grid(row=0, column=0, columnspan=6, padx=2,pady=2)
 

 entry.bind('<Control-v>', lambda _:'break')

 entry.bind('<Control-c>', lambda _:'break')

 sa.bind('<Escape>', lambda _: clear())

 sa.bind('<Double-Escape>', lambda e: close(tkinter.messagebox.showwarning("Close Window","If you press ok the window will be closed"),close())) 

 entry.bind('<Return>', lambda _: equal())

 #entry.bind('<Key>', lambda _: 'break')
 def onclick(no):
  entry.focus_set()
  entry.insert(tk.END,no)
  
  
 def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showerror("Error","Some Thing Wrong")

 def operator_click(operator):
    current = entry.get()
    if len(current) == 0 or current[-1] in ['+', '-', '*', '/', '.']:
        return
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(operator))       
        
 def exit():
    sa.quit()

 def close():
   sa.destroy()  
   
 def backspace():
    current = entry.get()
    new = current[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, new)  

 def clear():
    entry.delete(0, tk.END)
    
 entry.bind( 'a' , lambda _:'break') 
 entry.bind( 'b' , lambda _:'break')
 entry.bind( 'c' , lambda _:'break')
 entry.bind( 'd' , lambda _:'break')
 entry.bind( 'e' , lambda _:'break')
 
 b7 = tk.Button(sa, text='7' , width=6, height=2, padx=4,pady=4, command=lambda: onclick(7)) 
 b7.grid(row=1, column=0, pady=4, padx=4)

 b8 = tk.Button(sa, text='8', width=6, height=2, padx=4,pady=4, command=lambda: onclick(8))
 b8.grid(row=1,column=1, pady=4, padx=4)

 b9 = tk.Button(sa,text='9', width=6, height=2,  padx=4,pady=4, command=lambda: onclick(9))
 b9.grid(row=1,column=2, pady=4, padx=4)

 add = tk.Button(sa, text='+', width=6, height=2, padx=4,pady=4, command=lambda: operator_click('+'))
 add.grid(row=1, column=3, pady=4, padx=4 )

 b4 = tk.Button(sa, text='4', width=6, height=2, padx=4,pady=4, command=lambda:onclick(4))
 b4.grid(row=2, column=0, pady=4, padx=4)

 b5 = tk.Button(sa,text='5', width=6, height=2, padx=4,pady=4, command=lambda:onclick(5))
 b5.grid(row=2,column=1, pady=4, padx=4)

 b6 = tk.Button(sa,text='6', width=6, height=2, padx=4,pady=4, command=lambda:onclick(6))
 b6.grid(row=2,column=2,pady=4, padx=4)

 sub = tk.Button(sa, text='-', width=6, height=2, padx=4,pady=4, command=lambda: operator_click('-'))
 sub.grid(row=2,column=3, pady=4, padx=4)

 b1 = tk.Button(sa, text='1', width=6, height=2, padx=4,pady=4, command=lambda:onclick(1))
 b1.grid(row=3, column=0, pady=4, padx=4)

 b2 = tk.Button(sa, text='2', width=6, height=2, padx=4,pady=4, command=lambda:onclick(2))
 b2.grid(row=3, column=1, pady=4, padx=4)

 b3 = tk.Button(sa, text='3', width=6, height=2, padx=4,pady=4, command=lambda:onclick(3))
 b3.grid(row=3, column=2, pady=4, padx=4)

 entry.bind( 'f' , lambda _:'break')
 entry.bind( 'g' , lambda _:'break')
 entry.bind( 'h' , lambda _:'break')
 entry.bind( 'i' , lambda _:'break')
 entry.bind( 'j' , lambda _:'break')
 entry.bind( 'k' , lambda _:'break')
 entry.bind( 'l' , lambda _:'break')

 mul = tk.Button(sa,text='*', width=6, height=2, padx=4,pady=4, command=lambda: operator_click('*'))
 mul.grid(row=3, column=3, pady=4, padx=4)

 b0 = tk.Button(sa,text='0', width=6, height=2, padx=4,pady=4, command=lambda: onclick(0))
 b0.grid(row=4, column=0, pady=4, padx=4)

 dot = tk.Button(sa,text='.', width=6, height=2, padx=4,pady=4, command=lambda:operator_click('.'))
 dot.grid(row=4, column=1, pady=4, padx=4)

 eq = tk.Button(sa, text='=', width=6, height=2, padx=4,pady=4, command=equal)
 eq.grid(row=4,column=2, pady=4, padx=4)

 div = tk.Button(sa, text='/', width=6, height=2, padx=4,pady=4, command=lambda:operator_click('/'))
 div.grid(row=4,column=3, pady=4, padx=4)
 
 entry.bind( 'm' , lambda _:'break')
 entry.bind( 'n' , lambda _:'break')
 entry.bind( 'o' , lambda _:'break')
 entry.bind( 'p' , lambda _:'break')
 entry.bind( 'q' , lambda _:'break')
 entry.bind( 'r' , lambda _:'break')
 entry.bind( 's' , lambda _:'break')
 entry.bind( 't' , lambda _:'break')
 entry.bind( 'v' , lambda _:'break')
 entry.bind( 'u' , lambda _:'break')
 entry.bind( 'w' , lambda _:'break')
 entry.bind( 'x' , lambda _:'break')
 entry.bind( 'y' , lambda _:'break')
 entry.bind( 'z' , lambda _:'break')

 bk = tk.Button(sa, text='<-', width=6, height=2, padx=4,pady=4, command=backspace)
 bk.grid(row=5, column=0, pady=4, padx=4)

 c = tk.Button(sa, text='Clear', width=6, height=2, padx=4,pady=4, command=clear)
 c.grid(row=5, column=1, pady=4, padx=4)

 ex = tk.Button(sa, text='Exit', width=14, height=2, padx=4,pady=4, command=exit)
 ex.grid(row=5, column=2, columnspan=2)

 def pi():
    entry.insert(tk.END, math.pi)

 pi = tk.Button(sa, text="π", width=6, height=2, padx=4, pady=4, command=pi)
 pi.grid(row=6, column=0, pady=4, padx=4)

 def sqrt():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(float(current)))

 sqrt = tk.Button(sa, text="√", width=6, height=2, padx=4, pady=4, command=sqrt)
 sqrt.grid(row=6, column=1, pady=4, padx=4) 

 def sin():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = math.sin(float(current))
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

 sin = tk.Button(sa, text="sin", width=6, height=2, padx=4, pady=4, command=sin)
 sin.grid(row=6, column=2, pady=4, padx=4)    

 def cos():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = math.cos(float(current))
        entry.insert(0, result)
    except:
        entry.insert(0, "Error") 

 cos = tk.Button(sa, text="cos", width=6, height=2, padx=4, pady=4, command=cos)
 cos.grid(row=6, column=3, pady=4, padx=4)         

 def tan():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = math.tan(float(current))
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

 tan = tk.Button(sa, text="tan", width=6, height=2, padx=4, pady=4, command=tan)
 tan.grid(row=1, column=5, pady=4, padx=10)    

 def square():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = float(current) ** 2
        entry.insert(0, result)
    except:
        entry.insert(0, "Error") 

 sqr = tk.Button(sa, text="sqr2", width=6, height=2, padx=4, pady=4, command=square)
 sqr.grid(row=2, column=5, pady=4, padx=10)  

 def square3():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = float(current) ** 3
        entry.insert(0, result)
    except:
        entry.insert(0, "Error") 

 sqr = tk.Button(sa, text="sqr3", width=6, height=2, padx=4, pady=4, command=square3)
 sqr.grid(row=3, column=5, pady=4, padx=10)

 def percent():
    current = entry.get()
    entry.delete(0, tk.END)
    try:
        result = float(current) / 100
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")              

 percent = tk.Button(sa, text="%", width=6, height=2, padx=4, pady=4, command=percent)
 percent.grid(row=4, column=5, pady=4, padx=10)

 def xy():
  entry.insert(tk.END, "**")

 xpy = tk.Button(sa, text="x^y", width=6, height=2, padx=4, pady=4, command=xy)
 xpy.grid(row=5, column=5, pady=4, padx=10) 

 def my_callback(event): 
     l1.config(text=event.char) 
     for widget in sa.winfo_children():  
        if isinstance(widget, tk.Button):
            if widget['text']==event.char or widget['text'].lower()==event.char:
               widget['relief']='sunken'   
         
 def my_release(event):
     for widget in sa.winfo_children():   
          if isinstance(widget, tk.Button):  
               widget['relief']='raised'  

 l1=tk.Label(sa,text='#',bg='yellow',width=2,font=('Times',26,'normal'))
 l1.grid(row=6,column=5,padx=2,pady=10,columnspan=3)


 sa.bind('<Key>',my_callback) 
 sa.bind("<KeyRelease>",my_release)
 
  

splesh.after(5000, main_w)

mainloop()