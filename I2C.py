from smbus import SMBus
from tkinter import *
import tkinter.font as tkinterfont

root=Tk()
root.geometry("500x200+600+300")
root.title("I2C LED controller")
myfont=tkinterfont.Font(family='Helvetica',size=12,weight="bold")

label1=Label(root,text="this is a simple I2C controller")
label2=Label(root,text="")
label3=Label(root,text="master=raspberry pi")
label4=Label(root,text="slave=arduino uno")
label5=Label(root,text="")

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()

addr=0x8
bus=SMBus(1)

def runProgramon():
    bus.write_byte(addr,0x1)

            
def runProgramoff():
    bus.write_byte(addr,0x0)

            
onButton=Button(root,text="ON",font=myfont,command=runProgramon,bg='green',height=1,width=5)
onButton.pack()
offButton=Button(root,text="OFF",font=myfont,command=runProgramoff,bg='red',height=1,width=5)
offButton.pack()

root.mainloop()